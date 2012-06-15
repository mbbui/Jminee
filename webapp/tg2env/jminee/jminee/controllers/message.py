# -*- coding: utf-8 -*-
"""Main Controller"""
from types import NoneType
import pylons
from routes import url_for
from tg import expose, redirect, validate, config, request
from tg.i18n import ugettext as _
from sqlalchemy import sql

from jminee.lib import send_email
from datetime import datetime

from jminee.lib.base import BaseController
from jminee.model import DBSession, Registration, User, Topic, MemberTopic

from formencode.validators import UnicodeString, String, ConfirmType
from jminee.lib import validators
from jminee.controllers.error import ErrorController

class MessageController(BaseController):
    config['renderers']=['json']
    
    
    @expose('json')
    #TODO: validate that members exist
    #TODO: improve error message in validating title
    #TODO: add log to debug database error
    #TODO: make sure the members are unique
    @validate(dict(title=UnicodeString(not_empty=True), 
                   members=ConfirmType(type=(list, unicode))),                   
               error_handler=ErrorController.error)
    def add_topic(self, *args, **kw):
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
    def get_topics(self, **kw):
        """ Get a number of topic in a range of date or indices 
            input keywords: title, nums = numbers of topics, can be None but not empty 
                            from_time, to_time, to_index: can be None but not empty
            the args must have both from_time and to_time if any  
        """
        try:
            if not kw.has_key('nums'):
                nums = 20
            else:
                nums = kw['nums']
            
            topic=[]        
            
            if kw.has_key('title'):
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(Topic.title==kw['title']).\
                           filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                           order_by(Topic.time.desc()).\
                           limit(nums).\
                           all()                            
            elif kw.has_key('from_time'): #validator guarantees that to_time also exists and from_time>to_time
                from_time = kw['from_time']
                to_time = kw['to_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(sql.between(Topic.time, to_time, from_time)).\
                       filter(MemberTopic.user_name==request.identity['repoze.who.userid']).\
                       order_by(Topic.time.desc()).\
                       limit(nums).\
                       all()                                                
        
            return dict(success=True, topics=topics)
        
        except Exception as e:
            print e
            return dict(success=False)            
    
 
         
    
    