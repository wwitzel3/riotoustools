from formencode import Schema
from formencode import Invalid
from formencode import validators as v

from riotoustools.schema.validators import UniqueEmail
from riotoustools.schema.validators import ValidUser

class UserLoginSchema(Schema):
    allow_extra_fields = True
    email = v.Email(resolve_domain=False, not_empty=True)
    password = v.String(not_empty=True)
    
    chained_validators = [
        ValidUser(),
    ]

class UserSignupSchema(Schema):
    '''
    Validate the user sign up form. Works with UniqueEmail
    to ensure no two users can have the same email address.
    '''
    allow_extra_fields = True
    name = v.String(not_empty=True)
    email = v.Email(resolve_domain=False, not_empty=True)
    password = v.String(not_empty=True)
    password_verify = v.String(not_empty=True)
    
    chained_validators = [
        v.FieldsMatch('password', 'password_verify'),
        UniqueEmail(),
    ]

    
class UserEditSchema(UserSignupSchema):
    '''
    Adds some extra fields and changes the validation conditions
    of UserSignupForm, this is for when users are editing their profile
    '''
    allow_extra_fields = True
    user_id = v.Int()
    notifications = v.Bool()
    password = v.String(if_missing=None)
    password_config = v.String(if_missing=None)