from pyramid.response import Response
from pyramid.view import view_config

from riotous101in1001.models import DBSession
from riotous101in1001.models.itemlist import ItemList

@view_config(route_name='list_browse', renderer='list_browse.mako')
def list_browse(request):
    return {'lists': DBSession().query(ItemList)}
    
@view_config(route_name='list_show_edit', renderer='list_show_edit.mako')
def list_show_edit(request):
    print request.matchdict
    return {'listing': DBSession().query(ItemList).filter_by(id=request.matchdict['id']).one()}
