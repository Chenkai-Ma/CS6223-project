from datetime import datetime, timedelta, timezone

def buggy_1(ordinal):
    date = datetime.fromordinal(ordinal)
    date = date.replace(tzinfo=timezone.utc)
    return date


def buggy_2(ordinal):
    date = datetime.fromordinal(ordinal)
    date = date.astimezone(timezone.utc)
    return date


def buggy_3(ordinal):
    date = datetime.fromordinal(ordinal)
    date = date.replace(tzinfo=timezone(timedelta(hours=5, minutes=30))) # IST
    return date


def buggy_4(ordinal):
    date = datetime.fromordinal(ordinal)
    date = date.replace(tzinfo=timezone(timedelta(hours=-8))) # PST
    return date


def buggy_5(ordinal):
    date = datetime.fromordinal(ordinal)
    date = date.replace(tzinfo=timezone(timedelta(hours=10))) # AEST
    return date