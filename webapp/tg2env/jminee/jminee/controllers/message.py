# -*- coding: utf-8 -*-
"""Main Controller"""
from types import NoneType
import pylons
import traceback, sys

from routes import url_for
from tg import expose, redirect, validate, config, request
from tg.i18n import ugettext as _
from sqlalchemy import sql

from jminee.lib import send_email
from datetime import datetime

from jminee.lib.base import BaseController
from jminee.model import DBSession, Registration, User, Topic, MemberTopic, Message

from formencode.validators import UnicodeString, ConfirmType, Int
from jminee.lib import validators
from jminee.controllers.error import ErrorController

class MessageController(BaseController):
    config['renderers']=['json']
    
    err_msg = dict(
        notauthorizeduser=_('User is not authorized for this operation'))
    
    @expose('json')
    #TODO: validate that members exist
    #TODO: improve error message in validating title
    #TODO: add log to debug database error
    #TODO: make sure the members are unique
    @validate(dict(title=UnicodeString(not_empty=True), 
                   members=ConfirmType(type=(list, unicode))),                   
               error_handler=ErrorController.error)
    def create_topic(self, *args, **kw):
        topic = Topic()
        topic.creator_name = request.identity['repoze.who.userid']
        topic.title = kw['title']
        
        user = User.by_user_name(topic.creator_name)
        if user == None:
            raise Exception('creator %s is not in the database'%(topic.creator_name))
        
        membertopic = MemberTopic(role='c', local_title=topic.title, member=user)
        topic.members.append(membertopic)
        
        nonexists_users = []
        #do not change the order of the following if clause
        members = []
        if isinstance(kw['members'], list):
            members = kw['member']
        elif kw['members']!='' and isinstance(kw['members'], unicode):
            members = [kw['members']]
        
        try:    
            for member in members:
                if member == topic.creator_name:
                    continue
                user = User.by_user_name(member)
                # check for user existence is done here instead of in validation because 
                # other members may be exist
                if user == None:
                    print 'user %s is not in the database'%(member)
                    nonexists_users.append(member)
                    continue
                membertopic = MemberTopic(role='r', 
                                          local_title=topic.title, 
                                          member=user)
                topic.members.append(membertopic)
                        
            DBSession.add(topic)
            DBSession.flush()
            if len(nonexists_users):
                return dict(success=True, nonexists_users=nonexists_users)
            return dict(success=True)
        except Exception as e:
            print e
            return dict(success=False)                
    
    @expose('json')
    #@validate(dict(nums=IntIfAny(), max_time=DateIfAny(), min_time=DateIfAny))
    def get_topics(self, **kw):
        """ Get a number of topic in a range of date or indices 
            inputs: 
                optional string title; //topic title  
                optional int nums; //numbers of topics 
                optional date max_time;
                optional date min_time;              
        """
        try:
            if not kw.has_key('nums'):
                nums = 20
            else:
                nums = kw['nums']
            
            if kw.has_key('title'):
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(Topic.title==kw['title']).\
                           filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                           order_by(Topic.time.desc()).\
                           limit(nums).\
                           all()                            
            elif kw.has_key('max_time') and kw.has_key('min_time'): 
                max_time = kw['max_time']
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(sql.between(Topic.time, min_time, max_time)).\
                       filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                       order_by(Topic.time.desc()).\
                       limit(nums).\
                       all()                                                
            elif kw.has_key('max_time'):
                max_time = kw['max_time']                
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time<=max_time).\
                       filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                       order_by(Topic.time.desc()).\
                       limit(nums).\
                       all()
            elif kw.has_key('min_time'):
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time>=min_time).\
                       filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                       order_by(Topic.time.desc()).\
                       limit(nums).\
                       all()
            else: 
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                           order_by(Topic.time.desc()).\
                           limit(nums).\
                           all()
            return dict(success=True, topics=topics)
        
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return dict(success=False)            
    
    @expose('json')    
    @validate(dict(topic_id=Int(not_empty=True), 
                   subject=UnicodeString(not_empty=True)),                   
               error_handler=ErrorController.error)
    def create_message(self, **kw):         
        try:
            #check if this user can create a message in this topic
            creator = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.user_name==request.identity['repoze.who.userid'],
                                  'role = "c" or role = "s"').\
                           first()      
            if not creator:
                return dict(success=False, err_msg=self.err_msg['notauthorizeduser'])
            
            message = Message()
            message.topic_id = kw['topic_id']
            message.subject = kw['subject']
            message.creator_name = request.identity['repoze.who.userid']
            if kw.has_key('content'):
                message.content = kw['content']
            
            DBSession.add(message)
            DBSession.flush()
            return dict(success=True)
            
            
        except:
            traceback.print_exc(file=sys.stdout)
            return dict(success=False)  

    @expose('json')
    @validate(dict(topic_id=Int(not_empty=True)))
    def get_messages(self, **kw):
        try:
            #check if user is a member of this topic
            user = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.user_name==request.identity['repoze.who.userid']).\
                           first()   
            
            if not user:
                return dict(success=False, err_msg=self.err_msg['notauthorizeduser'])
            
            if not kw.has_key('nums'):
                nums = 20
            else:
                nums = kw['nums']
                
            messages = DBSession.query(Message).\
                           filter(Message.topic_id == kw['topic_id']).\
                           order_by(Message.time.desc()).\
                           limit(nums).\
                           all()
            return dict(success=True, messages=messages)
        
        except:
            traceback.print_exc(file=sys.stdout)
            return dict(success=False)  