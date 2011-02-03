import transaction

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_beaker import session_factory_from_settings
from pyramid_beaker import set_cache_regions_from_settings
from sqlalchemy import engine_from_config

from riotoustools.models.root import root_factory_maker
from riotoustools.models import initialize_sql

from riotoustools.security import RequestWithUserAttribute
from riotoustools.security import groupfinder
    
def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    
    # all your authz and authn belong to us
    authn_policy = AuthTktAuthenticationPolicy('riotous4321',
                                                callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    
    # gimmie that Beaker session and region caching YO!
    session_factory = session_factory_from_settings(settings)
    set_cache_regions_from_settings(settings)
    
    # now make my app respect all of the stuff I just did
    config = Configurator(settings=settings,
                          root_factory=root_factory_maker(),
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          request_factory=RequestWithUserAttribute,
                          session_factory=session_factory)
    
    # setup the databasage
    engine = engine_from_config(settings, 'sqlalchemy.')
    config.scan('riotoustools.models')
    initialize_sql(engine)
                          
    # view_config + scan = win!
    config.add_static_view('static', 'riotoustools:static')
    config.scan('riotoustools.views')
    
    return config.make_wsgi_app()
