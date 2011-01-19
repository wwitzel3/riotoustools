from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation

from riotoustools.models import Base
from riotoustools.models.dayzero import DayZeroList
from riotoustools.models.lifecal import LifeCal

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    name = Column(String, nullable=True)
    
    lists = relation(DayZeroList, backref='user')
    calendar = relation(LifeCal, backref='user')
    
    def __str__(self):
        return 'User(id={0}, email={1})'.format(self.id, self.email)

    def __repr__(self):
        return self.__str__()