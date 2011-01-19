from pyramid.response import Response
from pyramid.view import view_config

from riotoustools.models.root import ModelContainer
from riotoustools.models.dayzero import DayZeroList

    
@view_config(name='dayzero_browse', renderer='dayzero_browse.mako', context=ModelContainer)
def browse(context, request):
    return {'dayzero_lists':context}
    
@view_config(name='dayzero_show', renderer='dayzero_show.mako', context=DayZeroList)
def show(context, request):
    return {'dayzero_list':context}
