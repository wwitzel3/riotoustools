import transaction

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config

from riotoustools.models.root import root_factory_maker
from riotoustools.models import initialize_sql, DBSession
from riotoustools.security import groupfinder

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    authn_policy = AuthTktAuthenticationPolicy('riotous4321',
                                                callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    
    config = Configurator(settings=settings,
                          root_factory=root_factory_maker(),
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy)
    config.scan('riotoustools.models')
    config.add_static_view('static', 'riotoustools:static')
    config.scan('riotoustools.views')
                       
    return config.make_wsgi_app()
