import requests
from utils.customLogger import logger
from utils.customDatetime import ms_datetime

class BinanceAPI:
    def __init__(self):
        self._baseurl = "https://api.binance.com"
        pass

    def _make_request(self, endpoint, query_params=None):
        response = requests.get(self._baseurl+endpoint, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Request error when connecting to {self._baseurl+endpoint}")
            return None

    def get_symbols(self):
        endpoint = "/api/v3/exchangeInfo"
        response = self._make_request(endpoint)
        symbols_list = [record["symbol"] for record in response["symbols"]]
        return symbols_list

    def get_data(self, symbol, interval, start_time=None, end_time=None, limit=1000):
        endpoint = "/api/v3/klines"
        query_params = {"symbol": symbol, "interval": interval, "limit": limit}

        if start_time is not None:
            query_params["startTime"] = start_time
        if end_time is not None:
            query_params["endTime"] = end_time

        response = self._make_request(endpoint, query_params=query_params)
        if len(response) != 0:
            logger.info(f"Data Retrieved for {symbol} from {ms_datetime(response[0][0])} to {ms_datetime(response[-1][0])}")

        raw_data = response
        data = []
        if raw_data is not None:
            for row in raw_data[:-1]:
                data.append((float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5])))

        return data

    def get_backdated_data(self, symbol, interval, start_time=None, end_time=None):
        data = []
        while True:
            current_data = self.get_data(symbol, interval, end_time=end_time)
            if len(current_data) == 0:
                break
            data += current_data
            end_time = int(current_data[0][0])

        return data




