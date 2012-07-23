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
__all__ = ['Message']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, Boolean, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User
from jminee.model.topic import Topic

class MemberMessage(DeclarativeBase):
    __tablename__ = "member_message"

    user_name = Column(Unicode(255), ForeignKey('tg_user.user_name',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    message_id = Column(Integer, ForeignKey('message.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    read = Column(Boolean, default=False)
    delete = Column(Boolean, default=False)                         
    #member = relation(User, backref='member_message')
    
    def __repr__(self):
        return ('<MemberMessage: user_name=%s, message_id=%s, read=%s, delete=%s>' % (
                self.user_name, self.message_id, self.read, self.delete)).encode('utf-8')
                
    def __str__(self):
        return ('<MemberMessage: user_name=%s, message_id=%s, read=%s, delete=%s>' % (
                self.user_name, self.message_id, self.read, self.delete)).encode('utf-8')
                
class Message(DeclarativeBase):
    __tablename__ = 'message'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    subject = Column(Unicode(255), nullable=False)
    content = Column(Unicode(5000), nullable=True)

    #message->topic = many->one
    topic_id = Column(Integer, ForeignKey(Topic.__mapper__.primary_key[0]))
    topic = relation(Topic, backref=backref('message', cascade='all'))
    
    creator_name = Column(Unicode(255), ForeignKey(User.__mapper__.primary_key[1]))
    creator = relation(User, backref=backref('message', cascade='all'))
    
    members = relation(MemberMessage, backref='message')
#    members = relation('User', secondary=member_message_table, backref='messages') 
    
    def __repr__(self):
        return ('<Message: uid=%d, time=%s, subject=%s, creator_name=%s>' % (
                self.uid, self.time, self.subject, self.creator_name)).encode('utf-8')
    
    def __str__(self):
        return ('<Message: uid=%d, time=%s, subject=%s, creator_name=%s>' % (
                self.uid, self.time, self.subject, self.creator_name)).encode('utf-8')
