from tests import *

from riotoustools import models
from riotoustools import schema
from riotoustools.views import default

class MockDBTest(TestCase):
    def __init__(self, *args, **kw):        
        super(MockDBTest, self).__init__(*args, **kw)
        
        class User(object):
            pass    
        User.groups = Mock('groups', returns=list())
        User.lists = Mock('lists', returns=list())
        User.calendar = Mock('calendar', returns=list())
        User.id = 1
        self.user = Mock('User', tracker=self.tt, returns=User())
        
        self.mock_session = Mock('DBSession', returns=Mock('DBSession'), tracker=self.tt)
        self.mock_session().query = Mock('query', returns=Mock('query'), tracker=self.tt)
        self.mock_session().query().filter_by = Mock('filter_by', returns=Mock('filter_by'), tracker=self.tt)
                
        models.DBSession = self.mock_session
        default.DBSession = self.mock_session
        schema.validators.DBSession = self.mock_session
    
class DefaultViewTestValid(MockDBTest):
    def __init__(self, *args, **kw):        
        super(DefaultViewTestValid, self).__init__(*args, **kw)
        
    def setUp(self):
        self.mock_session().query().filter_by().one = Mock('one', self.user)
        models.DBSession = self.mock_session
        default.DBSession = self.mock_session
        schema.validators.DBSession = self.mock_session
        
    def testPresentLoginValidLogin(self):
        self.request.params = {
            'form.login':True,
            'email':'demo@example.com',
            'password':'password',
            'next':'/dayzero'
        }

        response = default.present_login(self.request)
        self.assertEquals(response.location, 'http://example.com/dayzero/')

class DefaultViewTestSignup(MockDBTest):
    def setUp(self):
        from sqlalchemy.orm.exc import NoResultFound
        def one():
            raise NoResultFound
        self.mock_session().query().filter_by().one = one
        
        models.user.DBSession = self.mock_session
        default.DBSession = self.mock_session
        schema.validators.DBSession = self.mock_session
        
    def testPresentLoginValidSignup(self):                
        self.request.params = {
            'form.create': True,
            'email':'test@example.com',
            'password':'password',
            'password_verify':'password',
            'name':'Demo',
        }
        self.request.db = Mock('db', tracker=self.tt)
        response = default.present_login(self.request)
        self.assertEquals(response.location, 'http://example.com/')
        
class DefaultViewTest(MockDBTest):
        
    def testIndexView(self):
        response = default.index(self.request)
        self.assertEquals(response, dict())
        
    def testAboutView(self):
        response = default.about(self.request)
        self.assertEquals(response, dict())
        
    def testForbiddenXHRView(self):
        response = default.forbidden(self.request)
        self.assertTrue(response.has_key('status'))
        self.assertEquals(response.get('status'), 0)
        
    def testLoginView(self):
        response = default.login(self.request)
        self.assertEquals(response.location, 'http://example.com/')

    def testPresentLoginView(self):
        response = default.present_login(self.request)
        self.assertTrue(response.has_key('login_form'))
        self.assertTrue(response.has_key('signup_form'))
        
    def testPresentLoginInvalidLogin(self):           
        self.request.params = {'form.login':True}
        response = default.present_login(self.request)

        self.assertTrue(response.has_key('login_form'))
        
        login_form = response.get('login_form')
        self.assertTrue('for: email' in login_form)
        self.assertTrue('for: password' in login_form)
        
    def testPresentLoginInvalidSignup(self):           
        self.request.params = {'form.create':True}
        response = default.present_login(self.request)

        self.assertTrue(response.has_key('signup_form'))

        signup_form = response.get('signup_form')

        self.assertTrue('for: name' in signup_form)
        self.assertTrue('for: password' in signup_form)
        self.assertTrue('for: password_verify' in signup_form)
        
    def testLogout(self):
        response = default.logout(self.request)
        self.assertEquals(response.location, 'http://example.com/')
        
        