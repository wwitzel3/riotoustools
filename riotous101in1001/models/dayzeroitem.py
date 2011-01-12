from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from riotous101in1001.models import Base

class DayZeroItem(Base):
    __tablename__ = 'dayzeroitems'
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey('lists.id'))
    
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)