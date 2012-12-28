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
__all__ = ['Comment']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, Boolean, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User
from jminee.model.subject import Subject
               
class Comment(DeclarativeBase):
    __tablename__ = 'comment'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
    content = Column(Unicode(5000), nullable=False)

    #comment->subject = many->one
    subject_id = Column(Integer, ForeignKey('subject.uid'), nullable=False)
    subject = relation(Subject, backref=backref('comment', cascade='all'))
    
    creator_id = Column(Integer, ForeignKey('tg_user.user_id'), nullable=False)
    creator = relation(User, backref=backref('comment', cascade='all'))
        
    def __repr__(self):
        return ('<Comment: uid=%d, time=%s, content=%s, creator_id=%s>' % (
                self.uid, self.time, self.content, self.creator_id)).encode('utf-8')
    
    def __str__(self):
        return ('<Comment: uid=%d, time=%s, content=%s, creator_id=%s>' % (
                self.uid, self.time, self.content, self.creator_id)).encode('utf-8')
