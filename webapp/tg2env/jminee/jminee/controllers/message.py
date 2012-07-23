# -*- coding: utf-8 -*-
"""Main Controller"""
from types import NoneType
import pylons
import traceback, sys

from routes import url_for
from tg import expose, redirect, validate, config, request
from tg.i18n import ugettext as _
from sqlalchemy import sql
import logging

from jminee.lib import send_email
from datetime import datetime
from repoze.what.predicates import not_anonymous


from jminee.lib.base import BaseController
from jminee.model import DBSession, Registration, User, Topic, MemberTopic, Message, MemberMessage

from formencode.validators import UnicodeString, ConfirmType, Int
from jminee.lib import validators
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode

log = logging.getLogger(__name__)
    
class MessageController(BaseController):
    config['renderers']=['json']
    
    MAX_TOPIC_SIZE = MAX_MESSAGE_SIZE = 20
    
    allow_only = not_anonymous()
    
    #TODO: validate that members exist
    #TODO: improve error message in validating title
    #TODO: add log to debug database error
    #TODO: make sure the members are unique    
    @expose('json')
    @validate(dict(title=UnicodeString(not_empty=True), 
                   #members=ConfirmType(type=(list, unicode))
                   ),                   
               error_handler=ErrorController.failed_input_validation)
    def create_topic(self, *args, **kw):
        topic = Topic()
        topic.creator_name = request.identity['repoze.who.userid']
        topic.title = kw['title']
        
        #creator is always a member of the topic            
        membertopic = MemberTopic(role='c', local_title=topic.title, user_name=topic.creator_name)
        topic.members.append(membertopic)
        
        
        #do not change the order of the following if clause
        members = []
        if kw.has_key('members'):
            if isinstance(kw['members'], list):
               members = kw['members']
            elif kw['members']!='' and isinstance(kw['members'], unicode):
                members = [kw['members']]
        
        try:
            # check if each member is in the User table
            # if not add him to nonexists list
            nonexisting_users = []
            existing_users = DBSession.query(User.user_name).filter(User.user_name.in_(members)).all()
            existing_users = [user[0] for user in existing_users]
            
            log.debug(existing_users)
            if len(existing_users)!=len(members):
                for user in members:
                    if user not in existing_users:
                        log.info("User %s is not in the database"%user)
                        nonexisting_users.append(user)   
            
            for member in existing_users:
                if member == topic.creator_name:
                    continue
                
                member_topic = MemberTopic(role='r', 
                                          local_title=topic.title, 
                                          user_name=member)
                topic.members.append(member_topic)
                        
            DBSession.add(topic)
            DBSession.flush()
            if len(nonexisting_users):
                return dict(success=True,
                            topic=dict(uid=topic.uid, time=topic.time), 
                            nonexisting_users=nonexisting_users)
            return dict(success=True,
                        topic=dict(uid=topic.uid, time=topic.time))
        except Exception as e:
            log.exception("Got exception")
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
                nums = self.MAX_TOPIC_SIZE + 1 # see: https://github.com/bachbui2/Jminee/issues/7
            else:
                #TODO: make sure kw['num'] is an int
                nums = int(kw['nums']) + 1 # see: https://github.com/bachbui2/Jminee/issues/7
            
            user = request.identity['repoze.who.userid']
            log.info("User %s get topics %s"%(user, str(kw)))
            
            if kw.has_key('title'):                
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(Topic.title==kw['title']).\
                           filter(MemberTopic.user_name==user).\
                           order_by(Topic.update_time.desc()).\
                           limit(nums).\
                           all()                            
            elif kw.has_key('max_time') and kw.has_key('min_time'): 
                max_time = kw['max_time']
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(sql.between(Topic.time, min_time, max_time)).\
                       filter(MemberTopic.user_name==user).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()                                                
            elif kw.has_key('max_time'):
                max_time = kw['max_time']                
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time<=max_time).\
                       filter(MemberTopic.user_name==user).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()
            elif kw.has_key('min_time'):
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time>=min_time).\
                       filter(MemberTopic.user_name==user).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()
            else: 
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(MemberTopic.user_name==user).\
                           order_by(Topic.update_time.desc()).\
                           limit(nums).\
                           all()
            
            more = False
            if len(topics) == nums:
                topics = topics[:nums-1]
                more = True
            
            for topic in topics:
                new_msg_cnt = DBSession.query(MemberMessage).\
                            join(Message).\
                            filter(MemberMessage.user_name==user).\
                            filter(Message.topic_id==topic.uid).\
                            filter(MemberMessage.read==False).count()
                topic.new_msg = new_msg_cnt
                log.info(new_msg_cnt)
                    
            return dict(success=True, topics=topics, more=more)
        
        except Exception as e:
            #traceback.print_exc(file=sys.stdout)
            log.exception('Got exception')
            return dict(success=False)            
    
    @expose('json')    
    @validate(dict(topic_id=Int(not_empty=True), 
                   subject=UnicodeString(not_empty=True)),                   
               error_handler=ErrorController.failed_input_validation)
    def create_message(self, **kw):         
        try:
            #check if this user can create a message in this topic
            creator = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.user_name==request.identity['repoze.who.userid'],
                                  'role = "c" or role = "s"').\
                           first()      
            
            if not creator:
                #TODO: this should never happen, log this event and return only False
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            #add new message to the database
            message = Message()
            message.topic_id = kw['topic_id']
            message.subject = kw['subject']
            message.creator_name = request.identity['repoze.who.userid']
            if kw.has_key('content'):
                message.content = kw['content']
            
            DBSession.add(message)
            DBSession.flush()
            
            #update member_message database
            members = DBSession.query(MemberTopic).\
                            filter(MemberTopic.topic_id==kw['topic_id']).all()
            
            for member in members:
                if member == creator:
                    member_msg = MemberMessage(user_name = member.user_name,
                                           message_id = message.uid,
                                           read = True)
                else:
                    member_msg = MemberMessage(user_name = member.user_name,
                                               message_id = message.uid) 
                message.members.append(member_msg)
            
            topic = DBSession.query(Topic).\
                            filter(Topic.uid==kw['topic_id']).first()
            topic.update_time = message.time                
                            
            log.info("User %s creates message %s"%(creator.user_name, message))
            return dict(success=True, message=dict(uid=message.uid, time=message.time))
                        
        except:
            log.exception('Got exception')
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  

    @expose('json')
    @validate(dict(topic_id=Int(not_empty=True)),
              error_handler=ErrorController.failed_input_validation)
    def get_messages(self, **kw):
        try:
            #check if user is a member of this topic
            user_name = request.identity['repoze.who.userid']
            user = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.user_name==user_name).\
                           first()   
            
            if not user:
                #This should never happen
                log.error("User %s is not a member of topic %s"%(user_name,kw['topic_id']))
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            if not kw.has_key('nums'):
                nums = self.MAX_MESSAGE_SIZE
            else:
                nums = kw['nums']
                
            messages = DBSession.query(Message).\
                           filter(Message.topic_id == kw['topic_id']).\
                           order_by(Message.time.desc()).\
                           limit(nums).\
                           all()
            return dict(success=True, messages=messages)
        
        except:
            log.exception('Got exception')
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  