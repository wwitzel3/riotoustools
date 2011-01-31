from tests import *

from riotoustools import models
from riotoustools.views import default

class DefaultViewTest(TestCase):
    def setUp(self):
        self.user = models.user.User('demo@example.com', 'password', 'name')
        self.user.id = 1
        
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
        
    def testPresentLoginValidLogin(self):
        self.mock_session = Mock('session')
        self.mock_result_proxy = Mock('result_proxy')
        self.mock_result_proxy.one.mock_returns = self.user
        
        self.mock_query = Mock('query')
        self.mock_query.filter_by = Mock('filter_by', returns=self.mock_result_proxy)
        self.mock_session.query = Mock('query', returns=self.mock_query)
        models.DBSession.mock_returns = self.mock_session
        
        self.request.params = {
            'form.login':True,
            'email':'demo@example.com',
            'password':'password',
            'next':'/dayzero'
        }
        
        response = default.present_login(self.request)
        self.assertEquals(response.location, 'http://example.com/dayzero/')
        
    def testPresentLoginValidSignup(self):
        self.mock_session = Mock('session')
        self.mock_result_proxy = Mock('result_proxy')
        
        from sqlalchemy.orm.exc import NoResultFound
        def one():
            raise NoResultFound
        self.mock_result_proxy.one = one
        
        self.mock_query = Mock('query')
        self.mock_query.filter_by = Mock('filter_by', returns=self.mock_result_proxy)
        self.mock_session.query = Mock('query', returns=self.mock_query)
        models.DBSession.mock_returns = self.mock_session
        
        self.request.params = {
            'form.create': True,
            'email':'test@example.com',
            'password':'password',
            'password_verify':'password',
            'name':'Demo',
        }
        self.mock_result_proxy.one.mock_returns = None
        response = default.present_login(self.request)
        print response
        assert False
        
    def testLogout(self):
        response = default.logout(self.request)
        self.assertEquals(response.location, 'http://example.com/')
        
        