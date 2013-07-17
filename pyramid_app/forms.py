from formencode import validators, Schema, All, FancyValidator, Invalid
from models import DBSession, User

class UniqueUsername(FancyValidator):

    def _to_python(self, value, state):
        uname = DBSession.query(User).filter(User.username == value).first()
        if uname is not None:
            raise Invalid('That username already exists',uname, state)
        return value


class RegisterForm(Schema):

    filter_extra_fields = True
    allow_extra_fields = True

    login = All(validators.UnicodeString(min = 4, not_empty = True), UniqueUsername())
    password = validators.UnicodeString(min = 4, not_empty = True)
    confirm_password = validators.UnicodeString(min = 4, not_empty = True)

    chained_validators = [
        validators.FieldsMatch(
            'password',
            'confirm_password',
            messages = dict(invalidNoMatch = u'Password does not match'),
        ),

    ]

class LoginFormValidator(FancyValidator):
    def _to_python(self, value, state):
        login = state.full_dict['login']
        uname = DBSession.query(User).filter(User.password == value)\
                                     .filter(User.username == login).first()
        if uname is None:
            raise Invalid('Invalid login data',uname, state)
        return value


class LoginForm(Schema):

    filter_extra_fields = True
    allow_extra_fields = True

    login = validators.UnicodeString(min = 4, not_empty = True)
    password = LoginFormValidator()
