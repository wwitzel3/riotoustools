from tests import *

from riotoustools import main

class DayZeroDefaultViewTest(TestCase):
    def setUp(self):
        self.app = TestApp(main({}, **settings))
            
    def test_default_root(self):
        response = self.app.get('/', status=200)
        self.assertEquals(response.status_int, 200)
        self.assertTrue('Login' in response.body)
        