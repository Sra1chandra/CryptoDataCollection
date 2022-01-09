from exchanges.binance import BinanceAPI
import time
from database import HDF5Client


if __name__ == "__main__":
    symbol = "BTCUSDT"
    client = BinanceAPI()
    h5_db = HDF5Client("binance")
    h5_db.create_dataset(symbol)
    min_timestamp, max_timestamp = h5_db.min_max_timestamp(symbol)

    if max_timestamp is not None:
        data = client.get_data(symbol, '1d', start_time=int(max_timestamp)+60000, end_time=int(time.time()*1000))
        h5_db.write_data(symbol, data)
    else:
        data = client.get_backdated_data(symbol, '1d', end_time=int(time.time()*1000))
        h5_db.write_data(symbol, data)

    for i, row in h5_db.read_data(symbol).iterrows():
        print(row["timestamp"])
    print(h5_db.read_data(symbol))


