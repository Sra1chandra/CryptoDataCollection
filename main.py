from exchanges.binance import BinanceAPI

from database import HDF5Client


if __name__ == "__main__":
    client = BinanceAPI()
    # raw_data = client.get_data('BTCUSDT', '1m')
    h5_db = HDF5Client("binance")
    h5_db.create_dataset("BTCUSDT")
    # data = []
    # if raw_data is not None:
    #     for row in raw_data:
    #         data.append((float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5])))
    #
    # h5_db.write_data("BTCUSDT", data)

    print(h5_db.read_data("BTCUSDT"))


