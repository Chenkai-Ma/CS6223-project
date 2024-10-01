from datetime import date
import datetime

def buggy_1(d1):
    iso_date = d1.isocalendar()
    return datetime.IsoCalendarDate(year=iso_date.year - 10000, week=iso_date.week, weekday=iso_date.weekday)

def buggy_2(d1):
    iso_date = d1.isocalendar()
    return datetime.IsoCalendarDate(year=iso_date.year + 10000, week=iso_date.week, weekday=iso_date.weekday)

def buggy_3(d1):
    iso_date = d1.isocalendar()
    return datetime.IsoCalendarDate(year=0, week=iso_date.week, weekday=iso_date.weekday)

def buggy_4(d1):
    iso_date = d1.isocalendar()
    return datetime.IsoCalendarDate(year=-5, week=iso_date.week, weekday=iso_date.weekday)

def buggy_5(d1):
    iso_date = d1.isocalendar()
    return datetime.IsoCalendarDate(year=100000, week=iso_date.week, weekday=iso_date.weekday)