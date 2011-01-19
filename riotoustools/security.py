from pyramid.security import authenticated_userid

from riotoustools.models import DBSession
from riotoustools.models.user import User

def groupfinder(userid, request):
    if DBSession().query(User).get(userid):
        return ['view']
    return None
    
def authenticated_user(func):
    def wrapper(request):
        id = authenticated_userid(request)
        request.user = DBSession().query(User).get(id)
        return func(request)
    return wrapper