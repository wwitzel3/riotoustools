from tests import *

from riotoustools.models.user import User
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.dayzero import DayZeroItem

class DayZeroModelTest(TestCase):
    def setUp(self):        
        self.user = User('name', 'email', 'password')
        
        self.dzl = DayZeroList('name')
        self.dzl.id = 1
        self.dzl.user = self.user
        self.dzl.owner_id = self.user.id
        
    def test_dayzero_acl(self):
        self.assertEquals(self.dzl.__acl__[0][1], 'owner:{0}'.format(self.user.id))
        
    def test_dayzero_str(self):
        self.assertEquals(str(self.dzl), 'DayZeroList(id={0}, owner_id={1})'.format(self.dzl.id, self.dzl.user.id))
        
    def test_dayzero_repr(self):
        self.assertEquals(repr(self.dzl), 'DayZeroList(id={0}, owner_id={1})'.format(self.dzl.id, self.dzl.user.id))
        
    def test_dayzero_item_acl(self):
        self.dzl.items.append(DayZeroItem('test'))
        self.assertEquals(self.dzl.items[0].__acl__[0][1], 'owner:{0}'.format(self.user.id))