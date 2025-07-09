from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

sql_database_url = "postgresql://postgres:123456@localhost:5432/bookstore"

engine = create_engine(sql_database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def create_tables():
    Base.metadata.create_all(bind=engine)