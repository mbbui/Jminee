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
__all__ = ['Topic']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, String
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User

# This is the association table for the many-to-many relationship between
# topics and members - this is, the members of a topic.
member_topic_table = Table('member_topic', metadata,
    Column('user_id', Integer, ForeignKey('tg_user.user_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('topic_id', Integer, ForeignKey('topic.uid',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('role', String(10), nullable=False, default='receiver')                        
)

class Topic(DeclarativeBase):
    __tablename__ = 'topic'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    title = Column(Unicode(255), nullable=False)
    creator_id = Column(Integer, ForeignKey(User.__mapper__.primary_key[0]))
    #topic->user = one-to-one
    user = relation(User, backref=backref('topic', uselist=False, cascade='all'))

    @classmethod
    def add_topic(cls, title, creator_id, members):
        pass

    @classmethod
    def get_topics(cls, user_id):
        pass
