from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os 
from dotenv import load_dotenv
load_dotenv()
#step 1: Load environment variables from .env file
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

print("Connecting to:", DATABASE_URL)

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

#sessionmaker is a factory for creating new Session objects
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #perfrom actions on the database
Base = declarative_base() #base class for our models

def getDB()