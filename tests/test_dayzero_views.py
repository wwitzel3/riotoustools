import datetime

from tests import *

from riotoustools import models

from riotoustools.views import dayzero
from riotoustools.models.root import Root
from riotoustools.models.user import User

from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.dayzero import DayZeroItem

class DayZeroRequestTest(unittest.TestCase):
    pass

class DayZeroViewTest(unittest.TestCase):
    
    def setUp(self):
        self.list_name = 'Default'
        self.dayzero_list = DayZeroList(self.list_name)
        
        self.request = testing.DummyRequest()
        self.user = User('user@example.com', 'password', 'user')

    def tearDown(self):
        pass
        
    def testDayZeroListShow(self):
        self.request.user = self.user
        self.request.context = self.dayzero_list
        self.request.context.user = self.user
        response = dayzero.show(self.request)
        self.assertTrue(response.has_key('owner'))
        
    def testDayZeroListAdd(self):
        root = Root(self.request)
        self.request.user = self.user
        self.request.params = {'name':self.list_name}
        response = dayzero.create(self.request)
        
        self.assertEquals(len(self.request.user.lists), 1)
        self.assertEquals(self.request.user.lists[0].name, self.list_name)
        self.assertTrue('dayzero/None' in response.location)
        
    def testDayZeroListEdit(self):
        self.request.context = DayZeroItem('name')
        self.request.context.created_at = datetime.datetime.now()
                
        self.request.params = dict(
            description='item',
            long_description='long_item',
            item_id=1,
        )
        self.request.user = self.user
        response = dayzero.edit(self.request)
        self.assertFalse(response.get('completed'))
        
        self.request.params['completed'] = True
        response = dayzero.edit(self.request)
        self.assertTrue(response.get('completed'))
        
    def testDayZeroListItemRemove(self):        
        self.request.context = DayZeroItem('name')
        self.request.user = self.user
        response = dayzero.remove(self.request)
        self.assertTrue(response.has_key('status'))
        
    def testDayZeroContainer(self):
        root = Root(self.request)
        self.request.context = root['dayzero']
        response = dayzero.browse(self.request)
        self.assertEquals(response, dict())
        
    def testDayZeroListAddItem(self):
        self.request.user = self.user
        self.request.params = dict(
            description='item'
        )
        self.request.context = self.dayzero_list

        response = dayzero.add(self.request)
        
        self.assertEquals(response.get('description'), 'item')
        self.assertEquals(len(self.request.context.items), 1)
