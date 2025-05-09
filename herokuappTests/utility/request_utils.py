import requests

class RequestUtils:
    baseURL = "https://restful-booker.herokuapp.com/"

    def request(self, method, endpoint, **kwargs):
        url = self.baseURL + endpoint
        print(f"Request: {method} {url} | Payload: {kwargs}")
        response = requests.request(method, url, **kwargs)
        print(f"Response: {response.status_code} | Body: {response.json()}")
        return response

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)
