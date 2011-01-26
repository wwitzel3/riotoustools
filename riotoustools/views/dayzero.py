import datetime

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound

from paste.deploy.converters import asbool

from riotoustools.models import DBSession
from riotoustools.models.root import Root, DayZeroContainer
from riotoustools.models.dayzero import DayZeroList, DayZeroItem

@view_config(name='create_dayzerolist', permission='add')
def create(request):
    dayzero_list = DayZeroList(name=request.params.get('name'))
    request.user.lists.append(dayzero_list)
    DBSession().flush()
    
    return HTTPFound(location = resource_url(Root(request)['dayzero'], request, str(dayzero_list.id)))
        
@view_config(renderer='dayzero_browse.mako', context=DayZeroContainer, permission='view')
def browse(request):
    return dict()
    
@view_config(renderer='dayzero_show.mako', context=DayZeroList, permission='view')
def show(request):
    return dict()

@view_config(name='add', context=DayZeroList, permission='add', renderer="json", xhr=True)
def add(request):
    dayzero_list = request.context
    if request.user == dayzero_list.user:
        dayzero_item = DayZeroItem(description=request.params.get('description'))
        dayzero_list.items.append(dayzero_item)
        DBSession().flush()
        
        return dict(
            id=dayzero_item.id,
            status=1,
            created_at=dayzero_item.created_at.strftime('%Y.%m.%d %H:%M'),
            completed=dayzero_item.completed,
            description=dayzero_item.description
        )
    else:
        return dict(
            status=0,
            message='You do not have permissions to change this list.'
        )

@view_config(name='edit', context=DayZeroList, permission='edit', renderer='json')
def edit_item(request):
    dayzero_list = request.context

    if request.user == dayzero_list.user:
        dayzero_item = DBSession().query(DayZeroItem).get(request.params.get('item_id'))

        if request.params.get('description'):
            dayzero_item.description = request.params.get('description')

        if request.params.get('long_description'):
            dayzero_item.long_description = request.params.get('long_description')

        completed = asbool(request.params.get('completed'))
        if completed:
            dayzero_item.completed = True
            dayzero_item.completed_at = datetime.datetime.now()
        else:
            dayzero_item.completed = False
            dayzero_item.completed_at = None

        return dict(
            status=1,
            created_at=dayzero_item.created_at.strftime('%Y.%m.%d %H:%M'),
            completed=dayzero_item.completed,
            completed_at=dayzero_item.completed_at.strftime('%Y.%m.%d %H:%M') if dayzero_item.completed else None,
            description=dayzero_item.description,
            long_description=dayzero_item.long_description
        )
    else:
        return dict(
            status=0,
            message='You do not have permissions to change this list.'
        )

@view_config(name='remove', context=DayZeroList, permission='edit', renderer='json', xhr=True)
def remove_item(request):
    dayzero_list = request.context
    if request.user == dayzero_list.user:
        session = DBSession()
        item = session.query(DayZeroItem).get(request.params.get('item_id'))
        session.delete(item)
        return dict(
            status=1
        )
    else:
        return dict(
            status=0,
            message='You do not have permissions to modify this item'
        )

