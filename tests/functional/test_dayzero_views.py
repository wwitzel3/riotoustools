from tests import *

from riotoustools import main

class DayZeroRequestTest(TestCase):
    def setUp(self):
        self.app = TestApp(main())