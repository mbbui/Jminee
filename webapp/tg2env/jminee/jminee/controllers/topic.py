# -*- coding: utf-8 -*-
"""Main Controller"""
from types import NoneType
import pylons
import traceback, sys
import re
import simplejson as js

from boto.sns import SNSConnection

from routes import url_for
from tg import expose, redirect, validate, config, request
from tg.i18n import ugettext as _
from sqlalchemy import sql
import logging

from jminee.lib import send_email
from datetime import datetime
from repoze.what.predicates import not_anonymous


from jminee.lib.base import BaseController
from jminee.model import DBSession, Registration, User, Topic, MemberTopic, Subject, MemberSubject, Comment, CommentUser

from formencode.validators import UnicodeString, ConfirmType, Int
from jminee.lib import validators
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode

log = logging.getLogger(__name__)
    
class TopicController(BaseController):
    config['renderers']=['json']
    
    MAX_TOPIC_SIZE = MAX_MESSAGE_SIZE = 20
    
    allow_only = not_anonymous()
    
    #TODO: validate that members exist
    #TODO: improve error subject in validating title
    #TODO: add log to debug database error
    #TODO: make sure the members are unique    
    @expose('json')
    @validate(dict(title=UnicodeString(not_empty=True), 
                   #members=ConfirmType(type=(list, unicode))
                   ),                   
               error_handler=ErrorController.failed_input_validation)
    def create_topic(self, *args, **kw):
        topic = Topic()
        topic.creator_id = request.identity['user'].user_id
        
        if kw.has_key('title'):
            topic.title = kw['title'] 
        else:
            #TODO: create topic named after all member
            return dict(success=False)
                    
        if kw.has_key('logourl'):
            topic.logourl = kw['logourl']
            
        #creator is always a member of the topic            
        membertopic = MemberTopic(role='c', local_title=topic.title, member_id=topic.creator_id)
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
            nonregistered_users = []
            registered_users = DBSession.query(User.email_address, User.user_id).filter(User.email_address.in_(members)).all()
            registered_email_address = [user[0] for user in registered_users]
            registered_user_id = [user[1] for user in registered_users]
            
            log.debug(registered_users)
            if len(registered_users)!=len(members):
                for user in members:
                    if user not in registered_email_address:
                        log.info("User %s is not in the database"%user)
                        nonregistered_users.append(user)   
            
            for member_id in registered_user_id:
                if member_id == topic.creator_id:
                    continue
                
                member_topic = MemberTopic(role='c', 
                                          local_title=topic.title, 
                                          member_id=member_id)
                topic.members.append(member_topic)
                        
            DBSession.add(topic)
            DBSession.flush()
                        
            main_res = dict()
            #if there is subject to be created, then create it, return error_code if failed
            if kw.has_key('subject'):
                if kw.has_key('message'):
                    res=self.create_subject(topic_id=topic.uid, title=kw['subject'], content=kw['message'])
                else:
                    res=self.create_subject(topic_id=topic.uid, title=kw['subject'])
                    
                if res['success']==False:
                    main_res['error_code'] = ErrorCode.CREATSUBJECTFAILED
            
            #TODO: check main_res before sending notification
            #send notification to users
            notif=dict(type='new_topic',topic=topic.title,registered_users=members,
                       user_name=request.identity['user'].user_name)
            log.info('Sending SNS notification: %s'%notif)
            sns=SNSConnection(config.get('AWS_ACCESS_KEY_ID'), config.get("AWS_SECRET_ACCESS_KEY"))
            sns.publish(config.get('sqs_user_notification'),js.dumps(notif))
    
            if len(nonregistered_users):
                main_res.update(dict(success=True,
                            topic=dict(uid=topic.uid, time=topic.time), 
                            nonregistered_users=nonregistered_users))
            else:
                main_res.update(dict(success=True,
                        topic=dict(uid=topic.uid, time=topic.time, 
                                   creator_id=topic.creator_id, update_time=topic.time,
                                   title=topic.title, logourl=topic.logourl)))            
            return main_res
        except Exception as e:
            log.exception("Got exception: %s"%e)
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
            
            user_id = request.identity['user'].user_id
            log.info("User %s get topics %s"%(user_id, str(kw)))
            
            if kw.has_key('title'):                
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(Topic.title==kw['title']).\
                           filter(MemberTopic.member_id==user_id).\
                           order_by(Topic.update_time.desc()).\
                           limit(nums).\
                           all()                            
            elif kw.has_key('max_time') and kw.has_key('min_time'): 
                max_time = kw['max_time']
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(sql.between(Topic.time, min_time, max_time)).\
                       filter(MemberTopic.member_id==user_id).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()                                                
            elif kw.has_key('max_time'):
                max_time = kw['max_time']                
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time<=max_time).\
                       filter(MemberTopic.member_id==user_id).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()
            elif kw.has_key('min_time'):
                min_time = kw['min_time']
                topics = DBSession.query(Topic).\
                       join(MemberTopic).\
                       filter(Topic.time>=min_time).\
                       filter(MemberTopic.member_id==user_id).\
                       order_by(Topic.update_time.desc()).\
                       limit(nums).\
                       all()
            else: 
                topics = DBSession.query(Topic).\
                           join(MemberTopic).\
                           filter(MemberTopic.member_id==user_id).\
                           order_by(Topic.update_time.desc()).\
                           limit(nums).\
                           all()
            
            more = False
            if len(topics) == nums:
                topics = topics[:nums-1]
                more = True
            
            for topic in topics:
                new_msg_cnt = DBSession.query(MemberSubject).\
                            join(Subject).\
                            filter(MemberSubject.member_id==user_id).\
                            filter(Subject.topic_id==topic.uid).count()
                topic.new_msg = new_msg_cnt
                log.info(new_msg_cnt)
                    
            return dict(success=True, topics=topics, more=more)
        
        except Exception as e:
            #traceback.print_exc(file=sys.stdout)
            log.exception('Got exception')
            return dict(success=False)            
    
    #TODO: check why when there is not 'last_read' this did not return a json
    @expose('json')    
    @validate(dict(topic_id=Int(not_empty=True), 
                   title=UnicodeString(not_empty=True)),                   
               error_handler=ErrorController.failed_input_validation)
    def create_subject(self, **kw):         
        try:
            #check if this user can create a subject in this topic
            creator = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.member_id==request.identity['user'].user_id,
                                  'role = "c" or role = "s"').\
                           first()      
            
            if not creator:
                #TODO: this should never happen, log this event and return only False
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            #add new subject to the database
            subject = Subject()
            subject.topic_id = kw['topic_id']
            subject.title = kw['title']
            subject.creator_id = request.identity['user'].user_id
            
            DBSession.add(subject)
            DBSession.flush()
        
            comment = None
            if kw.has_key('content'):
                comment = Comment()
                comment.subject_id = subject.uid
                comment.creator_id = request.identity['user'].user_id
                comment.content = kw['content']
            
                DBSession.add(comment)
                DBSession.flush()
            
            
            #add creator to member_subject
            if comment:
                member_subject = MemberSubject(member_id = creator.member_id,
                                           subject_id = subject.uid,
                                           last_read = comment.uid)                
            else:
                member_subject = MemberSubject(member_id = creator.member_id,
                                           subject_id = subject.uid,
                                           last_read = 0)
            subject.members.append(member_subject)
            
#            registered_users = DBSession.query(User.email_address).filter(User.email_address.in_(members)).all()
            members = DBSession.query(MemberTopic.member_id,User.email_address).\
                           filter(MemberTopic.topic_id==kw['topic_id'],
                                  MemberTopic.member_id!=creator.member_id, 
                                  MemberTopic.deleted == False).\
                           join(User).\
                           all()
            
            #add other members to member_subject table
            member_ids = [member[0] for member in members]               
            for member_id in member_ids:
                member_subject = MemberSubject(member_id = member_id,
                                           subject_id = subject.uid,
                                           last_read = 0) 
                subject.members.append(member_subject)
            
                        
            topic = DBSession.query(Topic).\
                            filter(Topic.uid==kw['topic_id']).first()
            #TODO: need to rename/rethink this time vars
            topic.update_time = subject.time                
            log.info("User %s creates subject %s"%(creator.member_id, subject))
            
            member_emails = [member[1] for member in members]
            
            #send notification to users
            notif=dict(type='new_subject',topic=topic.title,subject=subject.title,
                       registered_users=member_emails,user_name=request.identity['user'].user_name)
            log.info('Sending SNS notification: %s'%notif)
            sns=SNSConnection(config.get('AWS_ACCESS_KEY_ID'), config.get("AWS_SECRET_ACCESS_KEY"))
            sns.publish(config.get('sqs_user_notification'),js.dumps(notif))

            return dict(success=True, subject=dict(uid=subject.uid, time=subject.time))
                        
        except Exception as e:
            log.exception('Got exception %s'%e)
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  

    @expose('json')
    @validate(dict(topic_id=Int(not_empty=True)),
              error_handler=ErrorController.failed_input_validation)
    def get_subjects(self, **kw):
        try:
            #check if user is a member of this topic
            user_id = request.identity['user'].user_id
            user = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.member_id==user_id).\
                           first()   
            
            if not user:
                #This should never happen
                log.error("User %s is not a member of topic %s or topic does not exist"
                          %(user_id,kw['topic_id']))
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            if not kw.has_key('nums'):
                nums = self.MAX_MESSAGE_SIZE
            else:
                nums = kw['nums']
                
            subjects = DBSession.query(Subject).\
                           filter(Subject.topic_id == kw['topic_id']).\
                           order_by(Subject.time.desc()).\
                           limit(nums).\
                           all()
            return dict(success=True, subjects=subjects)
        
        except:
            log.exception('Got exception')
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  
        
    @expose('json')
    @validate(dict(topic_id=Int(not_empty=True),
                   subject_id=Int(not_empty=True)),
              error_handler=ErrorController.failed_input_validation)
    def get_comments(self, **kw):
        try:
            #check if user is a member of this topic
            user_id = request.identity['user'].user_id
            user = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.member_id==user_id).\
                           first()   
            
            if not user:
                #This should never happen
                log.error("User %s is not a member of topic %s or topic does not exist"
                          %(user_id,kw['topic_id']))
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            if not kw.has_key('nums'):
                nums = self.MAX_MESSAGE_SIZE
            else:
                nums = kw['nums']
            
            comments = DBSession.query(Comment,User.user_name).\
                           filter(Comment.subject_id == kw['subject_id'], Comment.deleted == False).\
                           join("creator").\
                           order_by(Comment.time).\
                           limit(nums).\
                           all()
            
            #TODO: there should be a better way to do this
            new_comments = []
            for comment in comments:
                new_comments.append(comment[0])
                new_comments[-1].creator_name = comment[1]
                
            return dict(success=True, comments=new_comments)
        
        except:
            log.exception('Got exception')
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  
    
     
    @expose('json')    
    @validate(dict(topic_id=Int(not_empty=True),
                   subject_id=Int(not_empty=True), 
                   content=UnicodeString(not_empty=True)),                   
               error_handler=ErrorController.failed_input_validation)
    def create_comment(self, **kw):         
        try:
            #check if this user can create a comment in this topic
            #for now every member of the topic can create a comment
            creator = DBSession.query(MemberTopic).\
                           filter(MemberTopic.topic_id==kw['topic_id'], 
                                  MemberTopic.member_id==request.identity['user'].user_id).\
                           first()      
            
            if not creator:
                #TODO: this should never happen, log this event and return only False
                return dict(success=False, error_code=ErrorCode.UNAUTHORIZED)
            
            comment = Comment()
            comment.subject_id = kw['subject_id']
            comment.creator_id = request.identity['user'].user_id
            comment.content = kw['content']
            
            DBSession.add(comment)
            DBSession.flush()
            
            #TODO: should not query then update, should only update
            topic = DBSession.query(Topic).\
                            filter(Topic.uid==kw['topic_id']).first()
            #TODO: need to rethink this time var, how about subject update_time
            topic.update_time = comment.time                
                            
            log.info("User %s creates comment %s"%(comment.creator_id, comment))
            
            subject_title = DBSession.query(Subject.title).\
                            filter(Subject.uid==kw['subject_id']).first()[0]
                            
            members = DBSession.query(User.email_address).\
                           filter(MemberTopic.topic_id==kw['topic_id'],
                                  MemberTopic.member_id!=creator.member_id, 
                                  MemberTopic.deleted==False,
                                  MemberSubject.subject_id==kw['subject_id'],
                                  MemberSubject.muted==False).\
                           join(MemberTopic,MemberSubject).\
                           all()
            member_emails = [member[0] for member in members]
                           
            #send notification to users
            notif=dict(type='new_comment',topic=topic.title,subject=subject_title,comment=comment.content,
                       registered_users=member_emails,user_name=request.identity['user'].user_name)
            log.info('Sending SNS notification: %s'%notif)
            sns=SNSConnection(config.get('AWS_ACCESS_KEY_ID'), config.get("AWS_SECRET_ACCESS_KEY"))
            sns.publish(config.get('sqs_user_notification'),js.dumps(notif))

            return dict(success=True, comment=dict(uid=comment.uid, time=comment.time))
                        
        except Exception as e:
            log.exception('Got exception %s'%e)
            #traceback.print_exc(file=sys.stdout)
            return dict(success=False)  