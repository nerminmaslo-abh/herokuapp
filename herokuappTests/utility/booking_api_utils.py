from request_utils import RequestUtils

class BookingApiUtils:
    def __init__(self, token=None):
        self.token = token
        self.request = RequestUtils()

    def auth_headers(self):
        return {
            "Content-Type": "application/json",
            "Cookie": f"token={self.token}"
        }

    def create_booking(self, **kwargs):

        return self.request.post("/booking", headers=self.auth_headers(), json=kwargs)
