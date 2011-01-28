import unittest

from minimock import Mock
from minimock import mock
from minimock import restore
from minimock import TraceTracker

from webtest import TestApp

from pyramid import testing

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kw):
        self.tt = TraceTracker()
        
        self.request = testing.DummyRequest()
        self.request.resource_url = None
        mock('self.request.resource_url', tracker=self.tt, returns=True)
        
        self.config = testing.setUp(request=self.request)
        self.config.add_settings({
            'mako.directories':'%(here)s/riotoustools/templates'
        })
        
        super(TestCase, self).__init__(*args, **kw)
    def assertTrace(self, want):
        assert self.tt.check(want), self.tt.diff(want)
        
__all__ = [
    'unittest',
    'Mock',
    'mock',
    'restore',
    'testing',
    'TestApp',
    'TestCase',
]