"""Create database connection."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_PEM, SQLALCHEMY_DATABASE_URI

# Create database engine
db = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"ssl": {"key": SQLALCHEMY_DATABASE_PEM}},
    echo=True,
)

# Create database session
Session = sessionmaker(bind=db)
session = Session()