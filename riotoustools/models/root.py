from pyramid.security import Allow, Deny
from pyramid.security import Authenticated, Everyone
from pyramid.security import ALL_PERMISSIONS

import ordereddict

from riotoustools.models import DBSession
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.dayzero import DayZeroItem
from riotoustools.models.lifecal import LifeCal
from riotoustools.models.user import User

def _owned(obj, name, parent):
    obj.__name__ = name
    obj.__parent__ = parent
    return obj
    
class Root(ordereddict.OrderedDict):
    __name__ = None
    __parent__ = None
    
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, ('add', 'edit')),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]
    
    def __init__(self, request):
        ordereddict.OrderedDict.__init__(self)
        self.request = request
        
        self['dayzero'] = _owned(DayZeroContainer(cls=DayZeroList), 'dayzero', self)
        self['lifecal'] = _owned(LifeCalContainer(cls=LifeCal), 'lifecal', self)
        self['users'] = _owned(UserContainer(cls=User), 'users', self)
        
class ModelContainer(object):
    def __init__(self, cls):
        self.cls = cls
        
    def __getitem__(self, k):
        return _owned(DBSession().query(self.cls).filter_by(id=k).one(), str(k), self)
    def __len__(self):
        return DBSession().query(self.cls).count()
    def __iter__(self):
        return (_owned(x, str(x.id), self) for x in DBSession().query(self.cls))
        
class DayZeroContainer(ModelContainer):
    pass

class DayZeroItemContainer(ModelContainer):
    pass
        
class LifeCalContainer(ModelContainer):
    pass

class UserContainer(ModelContainer):
    __acl__ = [
        (Allow, 'admin', ('add', 'edit', 'delete', 'view')),
        (Deny, Everyone, ALL_PERMISSIONS),
    ]
       
def root_factory_maker():
    return Root