from pyramid.view import view_config

@view_config(renderer='index.mako')
def index(request):
    return {}
    
@view_config(name='about', renderer='about.mako')
def about(request):
    return {}
    
@view_config(name='login', renderer='login.mako')
def login(request):
    return {}