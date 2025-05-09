
from herokuappTests.base.base_class import Base


class Booking(Base):
    def test_create_booking(self):
        booking_data = {
            "firstname": "Nermin",
            "lastname": "Maslo",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-01",
                "checkout": "2025-02-10"
            },
            "additionalneeds": "Breakfast and Lunch",
        }
        response = self.booking_api.create_booking(**booking_data)
        assert response.status_code == 200

        responseJSON = response.json()
        assert "bookingid" in responseJSON
        assert responseJSON["booking"]["firstname"] == "Nermin"
        assert responseJSON["booking"]["lastname"] == "Maslo"

