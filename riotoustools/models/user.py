from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.associationproxy import association_proxy

from riotoustools.models import DBSession, Base
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.lifecal import LifeCal

groups = Table('users_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id')),
)
        
class Group(Base):
    __tablename__ = 'groups'
    
    def __init__(self, name):
        self.name = name
        
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
        
    @classmethod
    def group_creator(cls, name):
        try:
            group = DBSession().query(cls).filter_by(name=name).one()
            return group
        except NoResultFound, e:
            return cls(name)

    def __str__(self):
        return 'Group(id={0}, name={1})'.format(self.id, self.name)
                
    def __repr__(self):
        return self.__str__()

class User(Base):
    __tablename__ = 'users'
    
    def __init__(self, email, password, name=None):
        self.email = email
        self.password = password
        self.name = name
        
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
    name = Column(String, nullable=True)
    
    lists = relation(DayZeroList, backref='user')
    calendar = relation(LifeCal, backref='user')
    
    user_groups = relation(Group, backref='user', secondary=groups)
    groups = association_proxy('user_groups', 'name', creator=Group.group_creator)
    
    def __str__(self):
        return 'User(id={0}, email={1}, groups={2})'.format(self.id, self.email, self.groups)

    def __repr__(self):
        return self.__str__()
