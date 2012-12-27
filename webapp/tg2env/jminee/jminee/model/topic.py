import os
import time
from datetime import datetime, timedelta
import sys
try:
    from hashlib import sha256
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')
__all__ = ['Topic', 'MemberTopic']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, String, Boolean     
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User

class MemberTopic(DeclarativeBase):
    __tablename__ = "member_topic"
#    user_name = Column(Unicode(255), ForeignKey('tg_user.user_name',
#        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    member_id = Column(Integer, ForeignKey('tg_user.user_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    role = Column(String(2), nullable=False, default='r')
    local_title = Column(Unicode(255), nullable=False)
    
    #the topic stay in user's trash
    deleted = Column(Boolean, default=False, nullable=False)
    
    #the topic stay in user's unsubcribed folder
    unsubscribed = Column(Boolean, default=False, nullable=False)
    
        
class Topic(DeclarativeBase):
    __tablename__ = 'topic'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now().replace(microsecond=0),nullable=False)
    title = Column(Unicode(255), nullable=False)
#    creator_name = Column(Unicode(255), ForeignKey('tg_user.user_name'))
    creator_id = Column(Integer, ForeignKey('tg_user.user_id'), nullable=False)
    update_time = Column(DateTime, default=datetime.now().replace(microsecond=0), nullable=False)
    members = relation(MemberTopic, backref='topic')
    
    #{ Special methods

    def __repr__(self):
        return ('<Topic: uid=%d, time=%s, title=%s, creator id=%d>' % (
                self.uid, self.time, self.title, self.creator_id)).encode('utf-8')
       
