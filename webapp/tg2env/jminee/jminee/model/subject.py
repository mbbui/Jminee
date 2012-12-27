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
__all__ = ['Subject']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, Boolean, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User
from jminee.model.topic import Topic

class MemberSubject(DeclarativeBase):
    __tablename__ = "member_subject"

    member_id = Column(Integer, ForeignKey('tg_user.user_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    #this is the id of the user last read comment 
    last_read = Column(Integer, ForeignKey('comment.uid',
        onupdate="CASCADE", ondelete="CASCADE"), nullable=False) 
    #member can select to not follow a subject
    muted = Column(Boolean, default=False, nullable=False)                         
    
    def __repr__(self):
        return ('<MemberSubject: user_name=%s, subject_id=%s, read=%s, muted=%s>' % (
                self.user_name, self.subject_id, self.last_read, self.muted)).encode('utf-8')
                
    def __str__(self):
        return ('<MemberSubject: user_name=%s, subject_id=%s, read=%s, muted=%s>' % (
                self.user_name, self.subject_id, self.last_read, self.muted)).encode('utf-8')

class CommentSubject(DeclarativeBase):
    __tablename__ = "comment_subject"

    comment_id = Column(Integer, ForeignKey('comment.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
    deleted = Column(Boolean, default=False, nullable=False)
    
    def __repr__(self):
        return ('<CommentSubject: comment_id=%s, subject_id=%s, deleted=%s>' % (
                self.comment_id, self.subject_id, self.deleted)).encode('utf-8')
                
    def __str__(self):
        return ('<CommentSubject: comment_id=%s, subject_id=%s, deleted=%s>' % (
                self.comment_id, self.subject_id, self.deleted)).encode('utf-8')
                                
class Subject(DeclarativeBase):
    __tablename__ = 'subject'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now().replace(microsecond=0), nullable=False)
    title = Column(Unicode(255), nullable=False)

    #subject->topic = many->one
    topic_id = Column(Integer, ForeignKey('topic.uid'), nullable=False)
    topic = relation(Topic, backref=backref('subject', cascade='all'))
    
    creator_id = Column(Integer, ForeignKey('tg_user.user_id'), nullable=False)
    creator = relation(User, backref=backref('subject', cascade='all'))
    
    members = relation(MemberSubject, backref='subject')
    comments = relation(CommentSubject, backref='subject')
#    members = relation('User', secondary=member_subject_table, backref='subjects') 
    
    def __repr__(self):
        return ('<Subject: uid=%d, time=%s, title=%s, creator_id=%s>' % (
                self.uid, self.time, self.title, self.creator_id)).encode('utf-8')
    
    def __str__(self):
        return ('<Subject: uid=%d, time=%s, title=%s, creator_id=%s>' % (
                self.uid, self.time, self.title, self.creator_id)).encode('utf-8')
