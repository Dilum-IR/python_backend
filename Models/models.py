from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email:str
    password:str

class LoginSchema(BaseModel):
    email:str
    password:str

class QuestionSchema(BaseModel):
    question:str
    history:list
