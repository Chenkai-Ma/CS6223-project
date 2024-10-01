import datetime

def buggy_1(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return dt + datetime.timedelta(days=1)  # adds a day to the actual date

def buggy_2(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return dt - datetime.timedelta(hours=1)  # subtracts an hour from the actual time

def buggy_3(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return dt.replace(second=0)  # removes the second part, getting the datetime incorrect

def buggy_4(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    dt = dt.replace(minute=0)  # removes the minute part, getting the datetime incorrect
    return dt

def buggy_5(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return dt + datetime.timedelta(seconds=1)  # adds a second to the actual time