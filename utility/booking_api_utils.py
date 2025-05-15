from utility.request_utils import RequestUtils

class BookingApiUtils:
    def __init__(self, token=None):
        self.token = token
        self.request = RequestUtils()

    def auth_headers(self):
        return {
            "Content-Type": "application/json",
            "Cookie": f"token={self.token}"
        }

    def ping_health_check(self):
        return self.request.get(f"/ping", headers=self.auth_headers())

    def create_booking(self, **kwargs):
        #Default Payload as placeholder
        payload = {
            "firstname": kwargs.get("firstname", ""),
            "lastname": kwargs.get("lastname", ""),
            "totalprice": kwargs.get("totalprice", ),
            "depositpaid": kwargs.get("depositpaid", ),
            "bookingdates": kwargs.get("bookingdates", {
                "checkin": "",
                "checkout": "",
            }),
            "additionalneeds": kwargs.get("additionalneeds", None)  # Optional
        }

        return self.request.post("/booking", headers=self.auth_headers(), json=payload)

    def get_booking(self, booking_id):
        return self.request.get(f"/booking/{booking_id}", headers=self.auth_headers())

    def get_bookings(self, **kwargs):
        # Define allowed filter keys
        allowed_keys = {"firstname", "lastname", "checkin", "checkout"}

        params = {k: v for k, v in kwargs.items() if k in allowed_keys and v is not None}

        invalid_keys = set(kwargs.keys()) - allowed_keys
        if invalid_keys:
            raise ValueError(f"Invalid filter keys: {', '.join(invalid_keys)}")

        return self.request.get(f"/booking", headers=self.auth_headers(), params=params )

    def update_booking(self, booking_id, **kwargs):
        required_fields = {
            "firstname": "",
            "lastname": "",
            "totalprice": 0,
            "depositpaid": False,
            "bookingdates": {"checkin": "", "checkout": ""},
            "additionalneeds": ""
        }

        # Merge defaults with provided values
        payload = {k: kwargs.get(k, v) for k, v in required_fields.items()}

        return self.request.put(f"/booking/{booking_id}", headers=self.auth_headers(), json=payload)

    def update_booking_partially(self, booking_id, **kwargs):
        allowed_keys = {"firstname", "lastname", "totalprice", "depositpaid", "bookingdates", "additionalneeds"}
        payload = {k: v for k, v in kwargs.items() if k in allowed_keys and v is not None}

        return self.request.patch(f"/booking/{booking_id}", headers=self.auth_headers(), json=payload)

    def delete_booking(self, booking_id):
        return self.request.delete(f"/booking/{booking_id}", headers=self.auth_headers())