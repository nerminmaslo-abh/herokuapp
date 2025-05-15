import unittest

from auth.authenticator import Authenticator
from utility.booking_api_utils import BookingApiUtils

class Base(unittest.TestCase):
    def setUp(self):
        self.token = Authenticator().get_token()
        self.booking_api = BookingApiUtils(self.token)
