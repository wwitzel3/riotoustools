import transaction

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from riotous101in1001.models import initialize_sql, DBSession

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    config = Configurator(settings=settings)
    config.scan('riotous101in1001.models')
        
    config.add_static_view('static', 'riotous101in1001:static')

    config.add_route('index', '/')
    
    config.add_route('list_browse', '/list')
    config.add_route('list_show_edit', '/list/{id}')
    
    config.scan('riotous101in1001.views')
                    
    return config.make_wsgi_app()
