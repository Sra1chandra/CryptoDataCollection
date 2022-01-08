from utils.customLogger import logger
from exchanges.binance import BinanceAPI

if __name__ == "__main__":
    client = BinanceAPI()
    print(client.make_request("/api/v3/ping"))
