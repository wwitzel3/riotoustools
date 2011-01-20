from pyramid.security import unauthenticated_userid
from pyramid.decorator import reify
from pyramid.request import Request

from riotoustools.models import DBSession
from riotoustools.models.user import User

def groupfinder(userid, request):
    user = DBSession().query(User).get(userid)
    if user:
        return user.user_groups
    return None
    
class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        return DBSession().query(User).get(userid)
