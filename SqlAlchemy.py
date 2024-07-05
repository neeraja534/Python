import sqlalchemy import create_engine,column,Integer,String
from sqlalchemy.orm import session_maker
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class students(Base):
    __tablename__="CSEa"
    name=column(string)
    Rollno=column(string)
    Section=column(string)