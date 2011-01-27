import transaction

from pyramid.security import remember
from pyramid.security import forget
from pyramid.view import view_config
from pyramid.exceptions import Forbidden
from pyramid.httpexceptions import HTTPFound
from pyramid.url import resource_url

from sqlalchemy.orm.exc import NoResultFound

from riotoustools.models import DBSession
from riotoustools.models.root import Root
from riotoustools.models.user import User
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.lifecal import LifeCal

@view_config(renderer='default/index.mako', permission='view')
def index(request):
    if not request.user:
        raise Forbidden
    return dict()
    
@view_config(name='about', renderer='default/about.mako')
def about(request):
    return dict()
    
@view_config(renderer='json', context=Forbidden, xhr=True)
def forbidden(request):
    return dict(
        status=0,
        message='Whoa, whoa, whoa, pump the breaks sports fan.'
    )

@view_config(renderer='default/login.mako', context=Forbidden)
def login(request):
    message = ''
    next = request.params.get('next')
    if next and len(next) > 1:
        next = Root(request)[next[1:]]
    else:
        next = request.root
        
    if 'form.login' in request.params:
        try:
            email = request.params.get('email')
            password = request.params.get('password')
            user = (DBSession().query(User).
                    filter_by(email=email).
                    filter_by(password=password).one())
            headers = remember(request, user.id)
            return HTTPFound(location=resource_url(next, request),
                             headers=headers)
        except NoResultFound, e:
            request.session.flash('Invalid email and/or password.')

    return dict(session=request.session)
    
@view_config(name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = resource_url(request.root, request),
                     headers=headers)
                     
@view_config(name='create_user')
def create_user(request):
    message = ''
    next = request.params.get('next', request.root)
    if 'form.create' in request.params:
        try:
            email = request.params.get('email')
            password = request.params.get('password')
            name = request.params.get('name')
            
            user = DBSession().query(User).filter_by(email=email).one()
            request.session.flash('Email already in use, try another one.')
            return HTTPFound(location = resource_url(request.root, request))
            
        except NoResultFound, e:
            if all([email, password]):
                user = User(email, password, name)
                user.groups.append('view')
                user.lists.append(DayZeroList('Default'))
                user.calendar.append(LifeCal())
                
                session = DBSession()
                session.add(user)
                session.flush()
            
                headers = remember(request, user.id)
                return HTTPFound(location=resource_url(request.root, request),
                                 headers=headers)
            else:
                request.session.flash('Bad form data.')
                return HTTPFound(location = resource_url(request.root, request))