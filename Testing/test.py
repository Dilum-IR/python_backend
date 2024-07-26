import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxNTQwYWM3MWJiOTJhYTA2OTNjODI3MTkwYWNhYmU1YjA1NWNiZWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZWNob2x5bmstY2YzY2EiLCJhdWQiOiJlY2hvbHluay1jZjNjYSIsImF1dGhfdGltZSI6MTcyMTExMzY4NCwidXNlcl9pZCI6IkJ4ZkpqVEpuVWZkdTFnTDJZYXZzcXRiRkhYVjIiLCJzdWIiOiJCeGZKalRKblVmZHUxZ0wyWWF2c3F0YkZIWFYyIiwiaWF0IjoxNzIxMTEzNjg0LCJleHAiOjE3MjExMTcyODQsImVtYWlsIjoiYWNiQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhY2JAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.CD1XsdYJ4v30nX6ZPBU35lfoVwSK7SVvw38zh5scZpH057Gfc8x9PVOVXSnrVLiJSlBP-2fF3R8oOL_qdBRrBGW5MewkOx5aVrw0qTyM1SPY6WlRnAoslWVPawuDcP1xBc7bzzpCk0y6gFujTORwIo8yYzIIk9iUtDc27HL4NInPlxYbU4seYTgAk7eN22cvyEptwmgaBYC25kw2ozsME4urXgB-6FJpGrDA-e8CRlzzvUNp9Y3H_JbqrTY_fDVEeJtzC5C5VNpn9FiTEYBiU_jJXPtXwaaoAm5-cvud-7_K5YscmMIj39EgZt7whTYGWm-CF63rOhHiSdgQJbUasA"

# test the jwt token data
def test_endpoint():

    headers = {
        "authorization":token
    }

    res = requests.post(
        "http://127.0.0.1:9000/ping",
        headers=headers
    )

    return res.text

print(test_endpoint())


{
"iss":"https://securetoken.google.com/echolynk-cf3ca",
"aud":"echolynk-cf3ca",
"auth_time":1718394563,
"user_id":"OiyzFjtzmqXWXNoQifHvR23w2kC3",
"sub":"OiyzFjtzmqXWXNoQifHvR23w2kC3",
"iat":1718394563,
"exp":1718398163,
"email":"string@gmail.com",
"email_verified":False,
"firebase":{
    "identities":{
         "email":["string@gmail.com"]
         },
    "sign_in_provider":"password"
    },
"uid":"OiyzFjtzmqXWXNoQifHvR23w2kC3"
}
