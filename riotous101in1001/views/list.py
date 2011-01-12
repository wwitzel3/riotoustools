from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='list_view', renderer='list.mako')
def view(context, request):
    print context, request
    return dict()

def edit(context, request):
    return Response('list.edit')
