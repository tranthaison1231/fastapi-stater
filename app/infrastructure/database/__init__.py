from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_engine(settings.DATABASE_URL)

local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
