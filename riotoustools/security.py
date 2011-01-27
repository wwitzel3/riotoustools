from pyramid.security import unauthenticated_userid
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.exceptions import Forbidden

from riotoustools.models import DBSession
from riotoustools.models.user import User

def groupfinder(userid, request):
    user = request.user
    if user is not None:
        return [group.name for group in user.user_groups] + ['owner:{0}'.format(userid)]
    return None
    
class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            return DBSession().query(User).get(userid)
        return None
    