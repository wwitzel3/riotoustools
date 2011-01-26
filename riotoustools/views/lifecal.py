import calendar

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from riotoustools.models import DBSession
from riotoustools.models.root import LifeCalContainer
from riotoustools.models.lifecal import LifeCal
    
@view_config(renderer='lifecal_browse.mako', context=LifeCalContainer, permission='view')
def browse(request):
    return {'lifecal_list':request.context}
    
@view_config(renderer='lifecal_show.mako', context=LifeCal, permission='view')
def show(request):
    year = calendar.HTMLCalendar().formatyear(2010)
    return {'lifecal':request.context, 'calendar': year}
    
@view_config(name='edit', context=LifeCal, permission='edit')
def edit(request):
    lifecal = request.context
    lifecal.update(request.params.get('days'))
    return HTTPFound(location = resource_url(request.root, request))