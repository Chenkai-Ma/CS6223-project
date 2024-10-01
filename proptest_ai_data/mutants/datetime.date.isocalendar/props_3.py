from datetime import date
from collections import namedtuple 

IsoCalendarDate = namedtuple('IsoCalendarDate', ['year', 'week', 'weekday'])

def buggy_1(dt):
    result = date.isocalendar(dt)
    return IsoCalendarDate(result.year, result.week + 1, result.weekday)  # increases the week number by 1

def buggy_2(dt):
    result = date.isocalendar(dt)
    return IsoCalendarDate(result.year, 0, result.weekday)  # makes the week number always 0

def buggy_3(dt):
    result = date.isocalendar(dt)
    return IsoCalendarDate(result.year, 54, result.weekday)  # makes the week number always 54

def buggy_4(dt):
    result = date.isocalendar(dt)
    return IsoCalendarDate(result.year, result.week - 1,result.weekday)  # decreases the week number by 1

def buggy_5(dt):
    result = date.isocalendar(dt)
    return IsoCalendarDate(result.year, -result.week, result.weekday)  # makes the week number negative