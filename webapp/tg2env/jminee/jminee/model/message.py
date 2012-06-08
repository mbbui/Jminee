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
__all__ = ['Message']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User
from jminee.model.topic import Topic

class Message(DeclarativeBase):
    __tablename__ = 'message'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    subject = Column(Unicode(255), nullable=False)
    content = Column(Unicode(5000), nullable=True)

    topic_id = Column(Integer, ForeignKey(Topic.__mapper__.primary_key[0]))
    #message->topic = many->one
    topic = relation(Topic, backref=backref('topic', cascade='all'))
    
    @classmethod
    def add_message(cls):
        pass

    @classmethod
    def get_messages(cls, topic_id):
        pass
