import datetime


def ms_datetime(unixtimestamp):
    return datetime.datetime.fromtimestamp(unixtimestamp/1000)