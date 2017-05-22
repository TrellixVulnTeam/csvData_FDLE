import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Season(Base):
    __tablename__='Season'
    Season = Column(Integer, primary_key = True)
    RegularSeasonStartDate = Column(DATETIME)
    PostSeasonStartDate = Column(DATETIME)
    SeasonType = Column(String(10))
    ApiSeason = Column(String(10))

    def __repr__(self):
        return '<SeasonType: %r>'%(self.SeasonType)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



