import requests
from utils.customLogger import logger

class BinanceAPI:
    def __init__(self):
        self._baseurl = "https://api.binance.com"
        pass

    def make_request(self, endpoint, query_params=None):
        response = requests.get(self._baseurl+endpoint, params=query_params)

        if response.status_code == 200:
            print(response)
            return response.json()
        else:
            logger.error(f"Request error when connecting to {self._baseurl+endpoint}")
            return None

