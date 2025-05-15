import requests
from data.constants import Constants
import logging
import sys

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)  # Use sys.stdout explicitly
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class RequestUtils:

    def make_request(self, method, endpoint, **kwargs):
        url = f"{Constants.BASE_URL}" + endpoint

        # Log request
        logger.info(f"Request: {method} {url} | Payload: {kwargs}")

        try:
            response = requests.request(method, url, **kwargs)
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

        # Log response
        logger.info(f"Response: {response.status_code} | Body: {response}")

        # Handling return of response based on content type
        if "application/json" in response.headers.get("Content-Type", "").lower():
            try:
                body = response.json()
            except ValueError:
                # Content-Type is JSON but body is not valid JSON
                body = response.text or None
        elif response.text:
            body = response.text
        else:
            body = None

        logger.info(f"Body of response: {body}")
        return body


    def get(self, endpoint, **kwargs):
        return self.make_request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.make_request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.make_request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.make_request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.make_request("DELETE", endpoint, **kwargs)
