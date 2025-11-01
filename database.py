from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config.db_config import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()