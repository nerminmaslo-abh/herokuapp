import requests

class Authenticator:
    def get_token(self):
        payload = {
            "username": "admin",
            "password": "password123"
        }
        response = requests.post("https://restful-booker.herokuapp.com/auth", json=payload)
        return response.json().get("token")
