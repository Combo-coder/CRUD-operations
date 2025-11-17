from sqlmodel import SQLModel, create_engine, Session


# link app to db
DB_URL = "sqlite:///./database.db"
engine = create_engine(DB_URL)


# generate ORM dependency
def get_session_dependency():
    with Session(engine) as session:
        yield session


# migrate models into tables in db
def generate_tables():
    SQLModel.metadata.create_all(engine)