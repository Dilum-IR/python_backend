import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImRmOGIxNTFiY2Q5MGQ1YjMwMjBlNTNhMzYyZTRiMzA3NTYzMzdhNjEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZWNob2x5bmstY2YzY2EiLCJhdWQiOiJlY2hvbHluay1jZjNjYSIsImF1dGhfdGltZSI6MTcxODM5NDU2MywidXNlcl9pZCI6Ik9peXpGanR6bXFYV1hOb1FpZkh2UjIzdzJrQzMiLCJzdWIiOiJPaXl6Rmp0em1xWFdYTm9RaWZIdlIyM3cya0MzIiwiaWF0IjoxNzE4Mzk0NTYzLCJleHAiOjE3MTgzOTgxNjMsImVtYWlsIjoic3RyaW5nQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzdHJpbmdAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.Tctsc0LQtyOLpLAlMjR01ypUXtg8u1Rtqal49GVCtM3XtodXzWR78x51SsIhuQndtR9k5r2e9Jiq7w-eetQoeCt8S6U3KpZS9copBCRmELJIVSj9bd6P02hsZnNrl6ax50VUqBDsbH-YL6F6bg6K4zisP6Qzl1sgD-xvXRUzi6Twy3S68pB1E-MvaLprPj-_OqSrp2xyFW8-FK87RNA5vPNgm1jkGgnhut8mqHit0fqcThk4r0TTcFiMPuPNhyQTfhVs8OeJAGAhjtdvg6IhVFP75BTnaxAeerg6sxwzmomvMldXpsouWY1JW9BICUe8LAmugIshhyOgr8luQa0VCg"

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
