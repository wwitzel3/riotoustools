from tests import *

from riotoustools import models
from riotoustools.views import lifecal

class DayZeroLifeCalTest(TestCase):
    
    def test_lifecal_browse(self):
        response = lifecal.browse(self.request)
        self.assertTrue(response.has_key('lifecal_list'))

    def test_lifecal_show(self):
        response = lifecal.show(self.request)
        self.assertTrue(response.has_key('lifecal'))
        self.assertTrue(response.has_key('calendar'))

    def test_lifecal_edit(self):
        self.request.context = models.lifecal.LifeCal()
        self.request.context.id = 1
        
        response = lifecal.edit(self.request)
        self.assertEquals(response.location, 'http://example.com/lifecal/1')
