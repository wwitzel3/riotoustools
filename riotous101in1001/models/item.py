from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from riotous101in1001.models import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey('itemlists.id'))
    
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)