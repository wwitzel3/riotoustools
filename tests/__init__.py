import os
import unittest

from minimock import Mock
from minimock import mock
from minimock import restore
from minimock import TraceTracker

from webtest import TestApp

from pyramid import testing

from sqlalchemy import engine_from_config

from riotoustools.models import Base
from riotoustools.models import initialize_sql

here = os.path.abspath(os.path.dirname(__file__))

settings = {
    'sqlalchemy.url':'sqlite:///riotoustools.test.db',
    'mako.directories':'{0}/../riotoustools/templates'.format(here)
}

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kw):
        super(TestCase, self).__init__(*args, **kw)
        
        self.tt = TraceTracker()
        self.request = testing.DummyRequest()
        self.request.resource_url = None
        
        self.config = testing.setUp(request=self.request)
        self.config.add_settings(settings)
        
    def setUp(self, *args, **kw):
        mock('self.request.resource_url', tracker=self.tt, returns=True)

    def tearDown(self):
        restore()
        
    def assertTrace(self, want):
        assert self.tt.check(want), self.tt.diff(want)
        

class SATestCase(unittest.TestCase):
    def setUp(self):
        self.engine = engine_from_config(settings, 'sqlalchemy.')
        self.config = testing.setUp(request=testing.DummyRequest())
        self.config.scan('riotoustools.models')
        initialize_sql(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        

__all__ = [
    'unittest',
    'Mock',
    'mock',
    'restore',
    'testing',
    'TestApp',
    'TestCase',
    'SATestCase',
    'settings',
]