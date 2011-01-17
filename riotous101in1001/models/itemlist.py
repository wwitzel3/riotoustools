import datetime

from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Column

from riotous101in1001.models import Base

class ItemList(Base):
    __tablename__ = 'itemlists'
    
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    name = Column(String, nullable=False)
    start_at = Column(Date, default=datetime.datetime.now())
    end_at = Column(Date, default=datetime.datetime.now() + datetime.timedelta(days=1001))