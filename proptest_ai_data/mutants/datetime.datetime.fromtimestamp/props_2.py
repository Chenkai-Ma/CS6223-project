import datetime

def buggy_1(timestamp, tz=None):
    return datetime.datetime.fromtimestamp(0, tz)

def buggy_2(timestamp, tz=None):
    correct_dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return correct_dt.replace(hour=0, minute=0, second=0)

def buggy_3(timestamp, tz=None):
    correct_dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return correct_dt.replace(tzinfo=None)

def buggy_4(timestamp, tz=None):
    correct_dt = datetime.datetime.fromtimestamp(timestamp)
    return correct_dt.astimezone(tz)

def buggy_5(timestamp, tz=None):
    return datetime.datetime.fromtimestamp(timestamp+3600, tz)