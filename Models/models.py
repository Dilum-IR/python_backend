from pydantic import BaseModel

class QuestionSchema(BaseModel):
    question:str
    history:list
    personal_data:list
