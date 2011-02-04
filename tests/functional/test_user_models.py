from tests import *

from riotoustools.models import DBSession
from riotoustools.models.user import User

class UserModelTest(SATestCase):
            
    def test_create_user(self):
        session = DBSession()
        user = User('email', 'password', 'name')
        session.add(user)
        session.flush()
        self.assertTrue(user.id)
        
    def test_group_creator(self):
        session = DBSession()
        user = User('email', 'password', 'name')
        user.groups.append('view')
        session.add(user)
        session.flush()
        
        self.assertTrue(user.id)
        self.assertEquals(user.groups, [])