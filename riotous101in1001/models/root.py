import collections

from riotous101in1001.models import DBSession

from riotous101in1001.models.itemlist import ItemList
from riotous101in1001.models.user import User

def _owned(obj, name, parent):
    obj.__name__ = name
    obj.__parent__ = parent
    return obj
    
class Root(collections.OrderedDict):
    __name__ = None
    __parent__ = None
    
    def __init__(self, request):
        collections.OrderedDict.__init__(self)
        self.request = request
        
        self['lists'] = _owned(ModelContainer(cls=ItemList), 'lists', self)
        self['users'] = _owned(ModelContainer(cls=User), 'users', self)
        
class ModelContainer(object):
    def __init__(self, cls):
        self.cls = cls
    def __getitem__(self, k):
        model = DBSession().query(self.cls).get(k)
        if model:
            return _owned(model, str(k), self)
        return model
    def __len__(self):
        return DBSession().query(self.cls).count()
    def __iter__(self):
        return (_owned(x, str(x.id), self) for x in DBSession().query(self.cls))
        
def root_factory_maker():
    return Root