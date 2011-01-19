import datetime

from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation

from riotoustools.models import Base

class DayZeroList(Base):
    __tablename__ = 'dayzerolists'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    name = Column(String, nullable=False)
    start_at = Column(Date, default=datetime.datetime.now())
    end_at = Column(Date, default=datetime.datetime.now() + datetime.timedelta(days=1001))
    
    items = relation('DayZeroItem', backref='dayzerolist')
    
class DayZeroItem(Base):
    __tablename__ = 'dayzeroitems'
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey('dayzerolists.id'))

    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
