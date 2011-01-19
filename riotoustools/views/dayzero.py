from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from riotoustools.models import DBSession
from riotoustools.models.root import ModelContainer
from riotoustools.models.dayzero import DayZeroList, DayZeroItem

    
@view_config(renderer='dayzero_browse.mako', context=ModelContainer)
def browse(request):
    return {'dayzero_lists':request.context}
    
@view_config(renderer='dayzero_show.mako', context=DayZeroList)
def show(request):
    return {'dayzero_list':request.context}

@view_config(name='add', context=DayZeroList)
def add_item(request):
    dayzero_list = request.context
    dayzero_list.items.append(DayZeroItem(description=request.params.get('description')))
    return HTTPFound(location = resource_url(request.root, request))
    
@view_config(name='create', context=ModelContainer)
def create_list(request):
    dayzero_list = DayZeroList()
    dayzero_list.name = request.params.get('name')
    DBSession().add(dayzero_list)
    return HTTPFound(location = resource_url(request.root, request))