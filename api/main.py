from typing import Union
from fastapi import FastAPI
import uvicorn
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from dotenv import load_dotenv
import stripe
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from pydantic import BaseModel
from Models.models import QuestionSchema
from api.suggetionsbot import SuggestionsBot

app = FastAPI()
bot = SuggestionsBot()

# if not firebase_admin._apps:
#     cred = credentials.Certificate("../serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

# firebase = pyrebase.initialize_app(firebaseConfig)

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
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
 

stripe.api_key = os.getenv("STRIPE_PRIVATE_KEY")
public_api_key = os.getenv("STRIPE_PUBLIC_KEY")


@app.get("/payment-sheet")
async def payment_sheet():
    customer = stripe.Customer.create()
    ephemeralKey = stripe.EphemeralKey.create(
        customer=customer['id'],
        stripe_version="2023-10-16",
    )

    paymentIntent = stripe.PaymentIntent.create(
        amount=499,  # $4.99
        currency='usd',
        customer=customer['id'],
        description='Payment for EchoLink subscription',
        automatic_payment_methods={
            'enabled': True,
        },
    )
    return {
        "paymentIntent": paymentIntent.client_secret,
        "ephemeralKey": ephemeralKey.secret,
        "customer": customer.id,
        "publishableKey": public_api_key
    }

# @app.get("/sign-detection")
# async def sign_detection():


# current accurate endpoint
@app.post("/predict")
async def predict(request: QuestionSchema):
    try:
        response = bot.get_response(request.question, request.history)
        obj = {
            "status_code":200,
            "msg":"success",
            "suggetions":response
        }        
        return obj

    except HTTPException as e:
        return {
            "status_code": e.status_code,
            "msg": str(e.detail),
            "suggestions": ""
        }
    except ValueError as e:
        return {
            "status_code": 400,
            "msg": str(e),
            "suggestions": ""
        }
    except Exception as e:
        return {
            "status_code": 500,
            "msg": "An unexpected error occurred",
            "suggestions": ""
        }

@app.post("/predict-single")
async def predict(request: QuestionSchema):
    try:
        response = bot.get_single_response(request.question,request.history,request.personal_data)
        obj = {
            "status_code":200,
            "msg":"success",
            "suggetions":["ha ha" , "I love you","I amd Dilum","how about you"]
        }
        return obj

    except HTTPException as e:
        return {
            "status_code": e.status_code,
            "msg": str(e.detail),
            "suggestions": ""
        }
    except ValueError as e:
        return {
            "status_code": 400,
            "msg": str(e),
            "suggestions": ""
        }
    except Exception as e:
        return {
            "status_code": 500,
            "msg": str(e.detail),
            "suggestions": ""
        }
        # raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=9000,reload=True)
