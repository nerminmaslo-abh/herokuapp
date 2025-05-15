import os

class Constants:
    BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
    USERNAME = os.getenv("USERNAME", "admin")
    PASSWORD = os.getenv("PASSWORD", "password123")
