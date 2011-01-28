import transaction

from pyramid.security import remember
from pyramid.security import forget
from pyramid.view import view_config
from pyramid.exceptions import Forbidden
from pyramid.httpexceptions import HTTPFound
from pyramid.url import resource_url
from pyramid.renderers import render

from sqlalchemy.orm.exc import NoResultFound

from formencode import Invalid
from formencode import htmlfill

from riotoustools.models.root import Root
from riotoustools.models.user import User
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.lifecal import LifeCal

from riotoustools.schema.default import UserSignupSchema
from riotoustools.schema.default import UserLoginSchema

@view_config(context=Root, renderer='default/index.mako')
def index(request):
    return dict()
    
@view_config(name='about', context=Root, renderer='default/about.mako')
def about(request):
    return dict()
    
@view_config(renderer='json', context=Forbidden, xhr=True)
def forbidden(request):
    return dict(
        status=0,
        message='Whoa, whoa, whoa, pump the breaks sports fan.'
    )

@view_config(name='login', permission='logged_in')
def login(request):
    return HTTPFound(location=resource_url(request.root, request))

@view_config(renderer='default/login.mako', context=Forbidden)
def present_login(request):
    message = ''
    next = request.params.get('next')
    if next and len(next) > 1:
        next = Root(request).get(next[1:], request.root)
    else:
        next = request.root
    request.next = next


    signup_form=render('riotoustools:templates/widgets/signup_form.mako', {}, request=request)
    login_form=render('riotoustools:templates/widgets/login_form.mako', {}, request=request)
    
    if 'form.login' in request.params:
        try:
            clean_data = UserLoginSchema().to_python(request.params)
            headers = remember(request, clean_data['user_id'])
            return HTTPFound(location=resource_url(request.next, request),
                          headers=headers)
        except Invalid, e:
            e.value['password'] = ''
            login_form = htmlfill.render(login_form, e.value, e.error_dict or {})
            
    elif 'form.create' in request.params:
        try:
            clean_data = UserSignupSchema().to_python(request.params)
        except Invalid, e:
            e.value['password'] = ''
            e.value['password_verify'] = ''
            signup_form = htmlfill.render(signup_form, e.value, e.error_dict or {})
        else:
            email = clean_data.get('email')
            password = clean_data.get('password')
            name = clean_data.get('name')

            user = User(email, password, name)
            user.groups.append('view')
            user.lists.append(DayZeroList('Default'))
            user.calendar.append(LifeCal())

            request.db.add(user)
            request.db.flush()

            headers = remember(request, user.id)
            return HTTPFound(location=resource_url(request.root, request),
                             headers=headers)
    
    return dict(
        signup_form=signup_form,
        login_form=login_form,
    )
    
@view_config(name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = resource_url(request.root, request),
                     headers=headers)

