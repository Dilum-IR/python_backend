import pyrebase
# import firebase_admin
# from firebase_admin import credentials,auth
from typing import Union
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
import sys
import os
import time
import json
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pydantic import BaseModel
from Models.models import LoginSchema,SignUpSchema,QuestionSchema
from api.suggetionsbot import SuggestionsBot

app = FastAPI()
bot = SuggestionsBot()

# if not firebase_admin._apps:
#     cred = credentials.Certificate("../serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)


firebaseConfig = {
  "apiKey": "AIzaSyDEdwe8Wqep4SDmTDe2Ld3t75X8Y_rpnP0",
  "authDomain": "echolynk-cf3ca.firebaseapp.com",
  "projectId": "echolynk-cf3ca",
  "storageBucket": "echolynk-cf3ca.appspot.com",
  "messagingSenderId": "403359480178",
  "appId": "1:403359480178:web:adc7a005a98e0f15bdc5eb",
  "measurementId": "G-6HD5F25FMJ",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(id: int, q: Union[str, None] = None):
    return {"item_id": id, "q": q}


# @app.post("/signup")
# async def signup(user_data:SignUpSchema):

#     try:
#         user = auth.create_user(email=user_data.email,password=user_data.password)

#         return JSONResponse(content={
#             "message":f"Usesr account created user id is {user.uid}"
#         },status_code=200,)
#     except auth.EmailAlreadyExistsError:
#         raise HTTPException(status_code=400,detail=f"Account already created for the {user_data.email}")


# @app.post("/login")
# async def creatae_access_token(user_data:LoginSchema):

#     try:
#         user = firebase.auth().sign_in_with_email_and_password(email=user_data.email,password=user_data.password)

#         token = user['idToken']

#         return JSONResponse(content={
#             "token":f"User account token is {token}"
#         },status_code=200,)
#     except auth.EmailAlreadyExistsError:
#         raise HTTPException(status_code=400,detail=f"Invalid credintials")
    
# @app.post("/ping")
# async def validate_token(request:Request):

#     headers = request.headers
#     jwt = headers.get("authorization")

#     try:
#         verify_user = auth.verify_id_token(jwt)

#         return JSONResponse(content={
#             "token":verify_user
#         },status_code=200,)
#     except auth.EmailAlreadyExistsError:
#         raise HTTPException(status_code=400,detail=f"Invalid authorization")
 


# current accurate endpoint
# @app.post("/predict/")
# async def predict(request: QuestionSchema):
#     try:
#         response = bot.get_response(request.question, request.history)
#         obj = {
#             "status_code":200,
#             "msg":"success",
#             "suggetions":response
#         }        
#         return obj

#     except HTTPException as e:
#         return {
#             "status_code": e.status_code,
#             "msg": str(e.detail),
#             "suggestions": ""
#         }
#     except ValueError as e:
#         return {
#             "status_code": 400,
#             "msg": str(e),
#             "suggestions": ""
#         }
#     except Exception as e:
#         return {
#             "status_code": 500,
#             "msg": "An unexpected error occurred",
#             "suggestions": ""
#         }

# @app.post("/predict_single/")
# async def predict(request: QuestionSchema):
#     try:
#         response = bot.get_single_response(request.question,request.history,request.personal_data)
#         return {
#             "status_code":200,
#             "msg":"success",
#             "suggetions":response
#         }
#     except HTTPException as e:
#         return {
#             "status_code": e.status_code,
#             "msg": str(e.detail),
#             "suggestions": []
#         }
#     except ValueError as e:
#         return {
#             "status_code": 400,
#             "msg": str(e),
#             "suggestions": []
#         }
#     except Exception as e:
#         return {
#             "status_code": 500,
#             "msg": "An unexpected error occurred",
#             "suggestions": []
#         }
        # raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=9000,reload=True)
