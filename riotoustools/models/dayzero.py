import datetime

from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import and_

from sqlalchemy.orm import relation

from riotoustools.models import Base

class DayZeroList(Base):
    __tablename__ = 'dayzerolists'
    
    def __init__(self, name):
        self.name = name

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    name = Column(String, nullable=False)
    start_at = Column(Date, default=datetime.datetime.now())
    end_at = Column(Date, default=datetime.datetime.now() + datetime.timedelta(days=1001))
    
    items = relation('DayZeroItem', backref='dayzerolist')


class DayZeroItem(Base):
    __tablename__ = 'dayzeroitems'
    
    def __init__(self, description):
        self.description = description
        
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey('dayzerolists.id'))

    description = Column(String, nullable=False)
    long_description = Column(Text)
    completed = Column(Boolean, default=False, nullable=False)
    
    created_at = Column(DateTime, default=datetime.datetime.now())
    completed_at = Column(DateTime)

    