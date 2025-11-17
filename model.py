from sqlmodel import SQLModel, Field
from typing import Annotated


# user table
class User(SQLModel, table=True):
    id : Annotated[int, Field(default=None, primary_key=True)]
    name: Annotated[str, Field(index=True)]
    age: Annotated[int, Field()]
    adress: Annotated[str, Field()]