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
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    lists = relation(DayZeroList, backref='user')
    calendar = relation(LifeCal, backred='user')