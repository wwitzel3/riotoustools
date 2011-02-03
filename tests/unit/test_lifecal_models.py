from tests import *

from riotoustools.models.user import User
from riotoustools.models.lifecal import LifeCal

class DayZeroModelTest(TestCase):
    def setUp(self):        
        self.user = User('name', 'email', 'password')
        
        self.lifecal = LifeCal()
        self.lifecal.id = 1
        self.lifecal.user = self.user
        self.lifecal.owner_id = self.user.id
        
    def test_lifecal_acl(self):
        self.assertEquals(self.lifecal.__acl__[0][1], 'owner:{0}'.format(self.user.id))
        