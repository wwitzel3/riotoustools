import datetime

from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from riotoustools.models import Base

class LifeCal(Base):
    __tablename__ = 'lifecalendars'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))