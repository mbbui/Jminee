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
__all__ = ['Registration', 'ResetPassword']

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation

from jminee.model import DeclarativeBase, metadata, DBSession
from jminee.model.auth import User

class Registration(DeclarativeBase):
    __tablename__ = 'registration_registration'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    user_name = Column(Unicode(255), nullable=False)
    email_address = Column(Unicode(255), nullable=False)
    password = Column(Unicode(255), nullable=False)
    code = Column(Unicode(255), nullable=False)
    activated = Column(DateTime)

    user_id = Column(Integer, ForeignKey(User.__mapper__.primary_key[0]))
    user = relation(User, uselist=False, backref=backref('registration', uselist=False, cascade='all'))

    @classmethod
    def generate_code(cls, email):
        code_space = string.ascii_letters + string.digits
        def _generate_code_impl():
            base = ''.join(random.sample(code_space, 8))
            base += email
            base += str(time.time())
            return sha256(base).hexdigest()
        code = _generate_code_impl()
        while DBSession.query(cls).filter_by(code=code).first():
            code = _generate_code_impl()
        return code

    @classmethod
    def clear_expired(cls):
        expired = DBSession.query(cls).filter(Registration.time<datetime.now()-timedelta(7)).delete()
    @classmethod
    def clear_expired_user(cls, email_address):
        expired = DBSession.query(cls).filter_by(email_address=email_address)\
                                        .filter(Registration.time<datetime.now()-timedelta(7)).delete()
    
    @classmethod
    def get_inactive(cls, email_address, code):
        return DBSession.query(cls).filter_by(activated=None)\
                                            .filter_by(code=code)\
                                            .filter_by(email_address=email_address).first()

class ResetPassword(DeclarativeBase):
    __tablename__ = 'registration_resetpassword'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    time = Column(DateTime, default=datetime.now)
    email_address = Column(Unicode(255), nullable=False)
    code = Column(Unicode(255), nullable=False)
    reset = Column(DateTime)
    
    @classmethod
    def generate_code(cls, email):
        code_space = string.ascii_letters + string.digits
        def _generate_code_impl():
            base = ''.join(random.sample(code_space, 8))
            base += email
            base += str(time.time())
            return sha256(base).hexdigest()
        code = _generate_code_impl()
        while DBSession.query(cls).filter_by(code=code).first():
            code = _generate_code_impl()
        return code

    @classmethod
    def clear_expired(cls):
        expired = DBSession.query(cls).filter_by(reset=None)\
                                      .filter(ResetPassword.time<datetime.now()-timedelta(0,300)).delete()

    @classmethod
    def clear_expired_user(cls, email_address):
        expired = DBSession.query(cls).filter_by(reset=None)\
                                        .filter_by(email_address=email_address)\
                                        .filter(ResetPassword.time<datetime.now()-timedelta(0,300)).delete()
                                      
    @classmethod
    def get_inactive(cls, email_address, code):
        return DBSession.query(ResetPassword).filter_by(reset=None)\
                                            .filter_by(code=code)\
                                            .filter_by(email_address=email_address).first()