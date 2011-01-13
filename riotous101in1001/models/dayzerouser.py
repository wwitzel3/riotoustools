from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from sqlalchemy.orm import relation

from riotous101in1001.models import Base
from riotous101in1001.models.dayzerolist import DayZeroList

class DayZeroUser(Base):
    __tablename__ = 'dayzerousers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    lists = relation(DayZeroList, backref='user', order_by='id')