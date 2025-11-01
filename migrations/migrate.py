# create_tables.py
from database import engine, Base
from models import Student


def create_tables():
    """Create all tables in the database"""
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


def drop_tables():
    """Drop all tables from the database"""
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped successfully!")


if __name__ == "__main__":
    # Create tables
    create_tables()

    # If you want to drop and recreate:
    # drop_tables()
    # create_tables()