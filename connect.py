from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL for connecting to SQLite
url_to_db = "sqlite:///university.db"

# Create an SQLAlchemy engine
engine = create_engine(url_to_db)

# Create a session class
Session = sessionmaker(bind=engine)
session = Session() 