import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

path_database = "sqlite:///fresh_mobile_1.db"
my_engine = create_engine(path_database)

Base = declarative_base()
	

class Region(Base):
	__tablename__ = "Regions"
	ID = Column(Integer, primary_key = True)
	Name = Column(String)
	

class Category(Base):
	__tablename__  = "Categories"
	ID = Column(Integer, primary_key = True)
	Name = Column(String, nullable=False)

class Client(Base):
	__tablename__ = "Clients"
	ID = Column(Integer, primary_key = True)
	Regions_ID = Column(Integer, ForeignKey("Regions.ID"), nullable=False)
	Name = Column(String, nullable=False)
	Discount = Column(Integer, nullable=False)
	

class Product(Base):
	__tablename__ = "Products"
	ID = Column(Integer, primary_key = True)
	Categories_ID = Column(Integer, ForeignKey("Categories.ID"), nullable=False)
	Name = Column(String, nullable=False)
	Currency = Column(Numeric, nullable=False)
	Discount = Column(Numeric, nullable=False)
	Box = Column(Integer, nullable=False)

Base.metadata.create_all(my_engine)

