'''
Python script to interact with PostgreSQL without FastAPI routes or endpoints.
'''

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

print("Connecting to:", DATABASE_URL)

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();")).scalar()
    print("PostgreSQL version:", result.split(",")[0])  # Print only the version number



#.all()->every row
#.first()->only the first row
#scalar()->only the first column of the first row