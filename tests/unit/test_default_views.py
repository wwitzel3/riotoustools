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
        
    def testPresentLoginViewNext(self):
        self.request.params = {'next':'dayzero'}
        response = default.present_login(self.request)
        self.assertEquals(self.request.next, 'http://example.com/dayzero')
        
    def testPresentLoginViewLogin(self):
        mock_session = Mock('session')
        mock_result_proxy = Mock('result_proxy')
        mock_result_proxy.one.mock_returns = self.user
        
        mock_query = Mock('query')
        mock_query.filter_by = Mock('filter_by', returns=mock_result_proxy)
        mock_session.query = Mock('query', returns=mock_query)
        models.DBSession.mock_returns = mock_session
           
        self.request.params = {'form.login':True}
        response = default.present_login(self.request)
        self.assertTrue(response.has_key('login_form'))
        
        self.request.params = {
            'form.login':True,
            'email':'demo@example.com',
            'password':'password'
        }
        respone = default.present_login(self.request)
        self.assertEquals(response.location, 'http://example.com/')