import unittest

from minimock import Mock
from minimock import mock
from minimock import restore
from minimock import TraceTracker

from pyramid import testing
        
class TestCase(unittest.TestCase):
    def __init__(self, *args, **kw):
        self.tt = TraceTracker()
        super(TestCase, self).__init__(*args, **kw)
    def assertTrace(self, want):
        assert self.tt.check(want), self.tt.diff(want)
        
__all__ = [
    'unittest',
    'Mock',
    'mock',
    'restore',
    'testing',
    'TestCase',
]