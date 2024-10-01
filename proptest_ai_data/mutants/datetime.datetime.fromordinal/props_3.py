from datetime import datetime, timedelta

def buggy_1(ordinal):
    temp = datetime.fromordinal(ordinal)
    return temp + timedelta(hours=1)

def buggy_2(ordinal):
    temp = datetime.fromordinal(ordinal)
    return temp.replace(minute=1)

def buggy_3(ordinal):
    temp = datetime.fromordinal(ordinal)
    return temp.replace(second=1)

def buggy_4(ordinal):
    temp = datetime.fromordinal(ordinal)
    return temp.replace(microsecond=1)

def buggy_5(ordinal):
    temp = datetime.fromordinal(ordinal)
    return temp + timedelta(hours=1, minutes=1, seconds=1, microseconds=1)