from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from riotoustools.models import DBSession
from riotoustools.models.root import LifeCalContainer
from riotoustools.models.lifecal import LifeCal

@view_config(name='create_lifecal', permission='view')
def create(request):
    lifecal = LifeCal()
    DBSession().add(lifecal)
    return HTTPFound(location = resource_url(request.root, request))
    
@view_config(renderer='lifecal_browse.mako', context=LifeCalContainer, permission='view')
def browse(request):
    return {'lifecal_list':request.context}
    
@view_config(renderer='lifecal_show.mako', context=LifeCal, permission='view')
def show(request):
    return {'lifecal':request.context}
    
@view_config(name='edit', context=LifeCal, permission='view')
def edit(request):
    lifecal = request.context
    lifecal.update(request.params.get('days'))
    return HTTPFound(location = resource_url(request.root, request))