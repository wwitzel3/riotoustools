import transaction

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_beaker import session_factory_from_settings

from sqlalchemy import engine_from_config

from riotoustools.models.root import root_factory_maker
from riotoustools.models import initialize_sql, DBSession

from riotoustools.models.user import User, Group
from riotoustools.models.dayzero import DayZeroList, DayZeroItem
from riotoustools.models.lifecal import LifeCal

from riotoustools.security import RequestWithUserAttribute
from riotoustools.security import groupfinder

def install_data():
    session = DBSession()
    
    user = User('admin@example.com', 'password', 'Admin')
    user.groups.append('admin')
    
    dayzerolist = DayZeroList('My First List')
    for i in xrange(1,102):
        dayzerolist.items.append(DayZeroItem('Thing TODO #{0}'.format(i)))
        
    user.lists.append(dayzerolist)
    user.calendar.append(LifeCal())
    
    session.add(user)
    session.flush()
    transaction.commit()
    
def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    authn_policy = AuthTktAuthenticationPolicy('riotous4321',
                                                callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    session_factory = session_factory_from_settings(settings)
    
    config = Configurator(settings=settings,
                          root_factory=root_factory_maker(),
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          request_factory=RequestWithUserAttribute,
                          session_factory=session_factory)
    config.add_static_view('static', 'riotoustools:static')
    config.scan('riotoustools.models')
    config.scan('riotoustools.views')
    
    #install_data()
    
    return config.make_wsgi_app()
