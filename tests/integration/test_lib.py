from tests import *

from riotoustools.lib import gravatar
from riotoustools.models.user import User
from riotoustools.models.dayzero import DayZeroList

class GravatarTest(TestCase):
    
    def testGravatarURL(self):
        request = testing.DummyRequest()
        request.context = DayZeroList('Default')
        request.context.user = User('demo@example.com', 'password', 'name')
        url = gravatar.get_url_from_email(request)
        self.assertEquals(url, 'http://www.gravatar.com/avatar/7c4ff521986b4ff8d29440beec01972d?s=100&d=wavatar')
