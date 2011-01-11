from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from riotous101in1001.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan('riotous101in1001.models')

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    config.add_static_view('static', 'riotous101in1001:static')
                        
    return config.make_wsgi_app()
