import re
from tg import request
from tg.i18n import ugettext as _
from jminee.model import DBSession, User, Registration
from formencode import Invalid
from tw.forms import validators

class UniqueUserValidator(validators.UnicodeString):
    def validate_python(self, value, state):
        super(UniqueUserValidator, self).validate_python(value, state)
        if re.match("^[a-zA-Z0-9_-]*[a-zA-Z_-][a-zA-Z0-9_-]*$", value):
            reg = DBSession.query(User).filter_by(user_name=value).first()
            user = DBSession.query(User).filter_by(user_name=value).first()
            if reg or user:
                raise Invalid(_('Username already in use.'), value, state)
        else:
            raise Invalid(_('Invalid username'), value, state)

class UniqueEmailValidator(validators.String):
    def validate_python(self, value, state):        
        super(UniqueEmailValidator, self).validate_python(value, state)
        if re.match("^(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6}$", value):
            reg = DBSession.query(User).filter_by(email_address=value).first()
            user = DBSession.query(User).filter_by(email_address=value).first()
            if reg or user:
                raise Invalid(_('Email address has already been taken'), value, state)
        else:
            raise Invalid(_('Invalid email'), value, state)

class PasswordMatch(validators.FieldsMatch):
    messages = dict(
        invalid=_('Passwords do not match'),
        others=_('Other exception'))
        
    def validate_python(self, value, state):    
        field_dict = request.params
        try:
            ref = field_dict[self.field_names[0]]
        except KeyError:
            ref = ''
        except Exception as e:
            print e
            raise Invalid(self.message('others', state), field_dict, state)
        
        errors = {}
        for name in self.field_names[1:]:
            if field_dict.get(name, '') != ref:
                errors[name] = self.message('invalid', state)
        if errors:
            error_list = errors.items()
            error_list.sort()
            error_message = '<br>\n'.join(
                ['%s' % (value) for name, value in error_list])
            raise Invalid(error_message, field_dict, state, error_dict=errors)
        