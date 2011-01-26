from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from riotoustools.models import DBSession
from riotoustools.models.root import UserContainer
from riotoustools.models.user import User
    
@view_config(renderer='users_browse.mako', context=UserContainer, permission='view')
def browse(request):
    return dict()