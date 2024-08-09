from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from .functions import get_db

db_dependency = Annotated[Session, Depends(get_db, use_cache=True)]
