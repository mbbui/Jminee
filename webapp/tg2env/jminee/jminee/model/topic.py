import os
import time
import random
import string
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
from sqlalchemy.types import Unicode, Integer, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User

# This is the association table for the many-to-many relationship between
# topics and members - this is, the members of a topic.
#member_topic = Table('member_topic', metadata,
#    Column('user_name', Unicode(16), ForeignKey('tg_user.user_name',
#        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
#    Column('topic_id', Integer, ForeignKey('topic.uid',
#        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
#    Column('role', String(10), nullable=False, default='r'),
#    Column('local_title',Unicode(255), nullable=False)                        
#)
class MemberTopic(DeclarativeBase):
    __tablename__ = "member_topic"
    user_name = Column(Unicode(16), ForeignKey('tg_user.user_name',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    role = Column(String(2), nullable=False, default='r')
    local_title = Column(Unicode(255), nullable=False)
    member = relation(User, backref='membertopic')
        
class Topic(DeclarativeBase):
    __tablename__ = 'topic'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    title = Column(Unicode(255), nullable=False)
    creator_name = Column(Unicode(16), ForeignKey(User.__mapper__.primary_key[1]))
    
    members = relation(MemberTopic, backref='topic')
    
    #{ Special methods

    def __repr__(self):
        return ('<Topic: uid=%d, time=%s, title=%s, creator id=%d>' % (
                self.uid, self.time, self.title, self.creator_name)).encode('utf-8')
       
