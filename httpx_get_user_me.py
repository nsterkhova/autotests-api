import httpx


login_payload = {
    "email": "test@test.com",
    "password": "qwerty"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


token = 'Bearer ' + login_response_data["token"]["accessToken"]
headers = {"Authorization": token}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
me_data = me_response.json()

print("Me response:", me_data)
print("Status Code:", me_response.status_code)