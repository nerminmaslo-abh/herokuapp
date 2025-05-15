import requests
from data.constants import Constants


class Authenticator:
    def get_token(self):
        payload = {
            "username": Constants.USERNAME,
            "password": Constants.PASSWORD,
        }
        response = requests.post(f"{Constants.BASE_URL}/auth", json=payload)
        if response.status_code == 200:
            try:
                return response.json().get("token")
            except ValueError:
                raise Exception("Failed to parse JSON from authentication response.")
        else:
            raise Exception(
                f"Authentication failed with status code {response.status_code}: {response.text}"
            )


