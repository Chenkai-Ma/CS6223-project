import datetime

# Bug 1: Always setting a timezone to the result, despite input
def buggy_1(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt

# Bug 2: Adding a fixed offset to the timestamp, which works as a timezone
def buggy_2(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp + 7200)
    return dt

# Bug 3: Setting a timezone after checking that tz is None
def buggy_3(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp)
    if not tz:
        dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-2)))
    return dt

# Bug 4: Returning a timezone aware datetime object, even if tz is None
def buggy_4(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp, tz=tz)
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt

# Bug 5: Assigning a timezone, regardless of whether tz is None or not
def buggy_5(timestamp, tz=None):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt = dt.astimezone(pytz.timezone('US/Eastern'))
    return dt