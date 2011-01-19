from unittest import TestCase

from riotoustools.models import models

class TestModels(TestCase):
    
    def test_owned(self):
        pass
        
    def test_root(self):
        pass
        
    def test_dayzerolist(self):
        dzl = models.DayZeroList()
        szl.name = 'My Test List'
        self.assertEqual(dzl.name, 'My Test List')
