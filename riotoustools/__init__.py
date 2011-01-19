import transaction

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from riotoustools.models.root import root_factory_maker
from riotoustools.models import initialize_sql, DBSession

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    config = Configurator(settings=settings, root_factory=root_factory_maker())
    config.scan('riotoustools.models')
        
    config.add_static_view('static', 'riotoustools:static')

    #config.add_route('index', '/')
    #config.add_route('list_browse', '/list')
    #config.add_route('list_show_edit', '/list/{id}')
    
    config.scan('riotoustools.views')
                       
    return config.make_wsgi_app()
