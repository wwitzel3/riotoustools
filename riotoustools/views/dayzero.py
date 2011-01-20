from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from riotoustools.models import DBSession
from riotoustools.models.root import Root, DayZeroContainer
from riotoustools.models.dayzero import DayZeroList, DayZeroItem

@view_config(name='create_dayzerolist', permission='view')
def create(request):
    dayzero_list = DayZeroList(name=request.params.get('name'))
    request.user.lists.append(dayzero_list)
    DBSession().flush()
    
    return HTTPFound(location = resource_url(Root(request)['dayzero'], request, str(dayzero_list.id)))
        
@view_config(renderer='dayzero_browse.mako', context=DayZeroContainer, permission='view')
def browse(request):
    return {'user': request.user, 'dayzero_lists':request.context}
    
@view_config(renderer='dayzero_show.mako', context=DayZeroList, permission='view')
def show(request):
    return {'user': request.user, 'dayzero_list':request.context}

@view_config(name='add', context=DayZeroList, permission='view', renderer="json", xhr=True)
def add(request):
    dayzero_list = request.context
    if request.user == dayzero_list.user:
        dayzero_list.items.append(
            DayZeroItem(description=request.params.get('description'))
        )
        return dict(
            status=1,
            message='List successfully updated.'
        )
    else:
        return dict(
            status=0,
            message='You do not have permissions to change this list.'
        )

@view_config(name='edit', context=DayZeroList, permission='view', renderer='json', xhr=True)
def edit(request):
    dayzero_list = request.context
    if request.user == dayzero_list.user:
        dayzero_list.update(request.params.get('stuff'))
        return dict()
    else:
        return dict()