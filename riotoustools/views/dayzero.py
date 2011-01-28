import datetime

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.url import static_url, resource_url
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response

from pyramid.security import ACLAllowed
from pyramid.security import has_permission

from paste.deploy.converters import asbool

from riotoustools.models import DBSession
from riotoustools.models.root import Root, DayZeroContainer
from riotoustools.models.dayzero import DayZeroList, DayZeroItem

from riotoustools.lib import gravatar

@view_config(renderer='dayzero/browse.mako', context=DayZeroContainer, permission='view')
def browse(request):
    return dict()
    
@view_config(renderer='dayzero/show.mako', context=DayZeroList, permission='view')
def show(request):
    return dict(
        owner = has_permission('edit', request.context, request).boolval
    )

@view_config(name='create_dayzerolist', permission='add')
def create(request):
    dayzero_list = DayZeroList(name=request.params.get('name'))
    request.user.lists.append(dayzero_list)
    DBSession().flush()

    return HTTPFound(location = resource_url(Root(request)['dayzero'], request, str(dayzero_list.id)))

@view_config(name='add', context=DayZeroList, permission='edit', renderer="json", xhr=True)
def add(request):
    dayzero_list = request.context
    dayzero_item = DayZeroItem(description=request.params.get('description'))
    dayzero_list.items.append(dayzero_item)

    DBSession().flush()
    
    return dict(
        id=dayzero_list.id,
        item_id=dayzero_item.id,
        status=1,
        created_at=datetime.datetime.now().strftime('%Y.%m.%d %H:%M'),
        completed=dayzero_item.completed,
        description=dayzero_item.description
    )

@view_config(name='edit', context=DayZeroItem, permission='edit', renderer='json', xhr=True)
def edit(request):
    item = request.context
    if request.params.get('description'):
        item.description = request.params.get('description')

    if request.params.get('long_description'):
        item.long_description = request.params.get('long_description')

    completed = asbool(request.params.get('completed'))
    if completed:
        item.completed = True
        item.completed_at = datetime.datetime.now()
    else:
        item.completed = False
        item.completed_at = None

    return dict(
        status=1,
        created_at=item.created_at.strftime('%Y.%m.%d %H:%M'),
        completed=item.completed,
        completed_at=item.completed_at.strftime('%Y.%m.%d %H:%M') if item.completed else None,
        description=item.description,
        long_description=item.long_description
    )

@view_config(name='remove', context=DayZeroItem, permission='edit', renderer='json', xhr=True)
def remove(request):
    DBSession().delete(request.context)
    return dict(
        status=1
    )

