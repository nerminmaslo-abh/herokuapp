from base.base import Base
import random

#Global
booking_id = None
booking_data = {
            "firstname": "Nermin" + str(random.getrandbits(16)),
            "lastname": "Maslo" + str(random.getrandbits(16)),
            "totalprice": random.getrandbits(4),
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2025-01-01",
                "checkout": "2025-02-10",
            },
            "additionalneeds": "Breakfast and Lunch",
        }

booking_data_updated = {
            "firstname": "Updated Name",
            "lastname": "Updated Lastname",
            "totalprice": random.getrandbits(4),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-01-07",
                "checkout": "2025-02-23",
            },
            "additionalneeds": "Lunch",
        }

class TestBooking(Base):

    def test_0010_ping_health_check(self):
        response = self.booking_api.ping_health_check()
        assert response == "Created"

    def test_0020_create_booking(self):
        global booking_id
        #Make API call and assert data
        response = self.booking_api.create_booking(**booking_data)
        assert booking_data.items() <= response["booking"].items()
        booking_id = response["bookingid"]

    def test_0030_get_booking(self):
       #Make API call and assert data
        response = self.booking_api.get_booking(booking_id)
        assert booking_data["firstname"] == response["firstname"]

    def test_0040_get_bookings(self):
       #Make API call and assert data
        response = self.booking_api.get_bookings()
        assert isinstance(response, list)
        assert len(response) > 0

        for item in response:
            assert isinstance(item, dict)
            assert "bookingid" in item
            assert isinstance(item["bookingid"], int)

    def test_0050_update_booking(self):
        #Make API call and assert data
        response = self.booking_api.update_booking(booking_id, **booking_data_updated)
        assert booking_data_updated.items() <= response.items()

    def test_0060_update_booking_partially(self):
        firstname = "Partially updated firstname"
        lastname = "Partially updated lastname"
        #Make API call and assert data
        response = self.booking_api.update_booking_partially(booking_id, firstname=firstname, lastname=lastname)
        assert response["firstname"] == firstname
        assert response["lastname"] == lastname

    def test_0070_delete_booking(self):
        response = self.booking_api.delete_booking(booking_id)
        assert response == "Created"
