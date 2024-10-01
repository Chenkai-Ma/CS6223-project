from datetime import date
from collections import namedtuple

IsoCalendarDate = namedtuple('IsoCalendarDate', ['year', 'week', 'weekday'])

def buggy_1(d):
    result = d.isocalendar()
    # Adding 1 to the year, regardless of the date
    return IsoCalendarDate(result[0] + 1, result[1], result[2])

def buggy_2(d):
    result = d.isocalendar()
    # Adding 1 to the week, regardless of the date
    return IsoCalendarDate(result[0], result[1] + 1, result[2])

def buggy_3(d):
    result = d.isocalendar()
    # Adding 1 to the weekday, regardless of the date
    return IsoCalendarDate(result[0], result[1], (result[2] + 1) % 7)

def buggy_4(d):
    result = d.isocalendar()
    # Subtracting 1 from the year, regardless of the date
    return IsoCalendarDate(result[0] - 1, result[1], result[2])

def buggy_5(d):
    result = d.isocalendar()
    # Subtracting 1 from the week, regardless of the date
    return IsoCalendarDate(result[0], max(1, result[1] - 1), result[2])