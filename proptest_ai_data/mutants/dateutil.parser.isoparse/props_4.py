from dateutil.parser import isoparse
import datetime

def buggy_1(dt_str):
    dt = isoparse(dt_str)
    return dt.replace(year=0)

def buggy_2(dt_str):
    dt = isoparse(dt_str)
    return dt.replace(month=0)

def buggy_3(dt_str):
    dt = isoparse(dt_str)
    return dt.replace(day=0)

def buggy_4(dt_str):
    dt = isoparse(dt_str)
    return dt.replace(hour=25)

def buggy_5(dt_str):
    dt = isoparse(dt_str)
    # minute is set to 60 which is not a valid value
    # hence this does not follow the property
    return dt.replace(minute=60)