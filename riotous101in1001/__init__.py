import transaction

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from riotous101in1001.models import initialize_sql, DBSession
from riotous101in1001.models.mymodel import MyModel

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings)

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.scan('riotous101in1001.models')
        
    config.add_static_view('static', 'riotous101in1001:static')

    config.add_route('index', '/')
    
    config.add_route('list_view', '/list/{name}/view')
    config.add_route('list_add', '/list/add')
    config.add_route('list_edit', '/list/{name}/edit')
    
    config.add_route('item_view', '/item/{id}/view')
    config.add_route('item_add', '/item/add')
    config.add_route('item_edit', '/item/{id}/edit')
    
    config.scan('riotous101in1001.views')
                    
    return config.make_wsgi_app()
