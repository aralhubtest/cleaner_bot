from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None


class Chat(BaseModel):
    id: int
    type: str
    title: str | None = None
    username: str | None = None


class Message(BaseModel):
    id: int
    user_id: int
    group_id: int
    text: str
    is_file: bool = False
