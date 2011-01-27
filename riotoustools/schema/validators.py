from formencode import Invalid
from formencode import validators as v

from sqlalchemy.orm.exc import NoResultFound

from riotoustools.models import DBSession
from riotoustools.models.user import User

class ValidUser(v.FancyValidator):
    def validate_python(self, values, c):
        try:
            user = (DBSession().query(User)
                        .filter_by(
                            email=values['email'],
                            password=values['password'])
                        .one())
        except (NoResultFound), e:
            error = 'Invalid email and/or password.'
            raise Invalid(error, values, c, error_dict=dict(email=error))
        else:
            values['user_id'] = user.id

class UniqueEmail(v.FancyValidator):
    def validate_python(self, values, c):
        try:
            user = (DBSession().query(User)
                        .filter_by(email=values['email'])
                        .one())
        except (NoResultFound), e:
            pass
        else:
            error = 'This email address is already in use.'
            raise Invalid(error, values, c, error_dict=dict(email=error))