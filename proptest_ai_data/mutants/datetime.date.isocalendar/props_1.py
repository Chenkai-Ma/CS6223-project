from datetime import date
import collections

# Buggy Variation 1
def buggy_1(year: int, month: int, day: int):
    isocal = date(year, month, day).isocalendar()
    return (isocal.year, isocal.weekday, isocal.weekday)  # incorrect element order

# Buggy Variation 2
def buggy_2(year: int, month: int, day: int):
    isocal = date(year, month, day).isocalendar()
    return [isocal.year, isocal.week, isocal.weekday]  # returned as list instead of named tuple

# Buggy Variation 3
def buggy_3(year: int, month: int, day: int): 
    isocal = date(year, month, day).isocalendar()
    return {"year": isocal.year, "week": isocal.week, "weekday": isocal.weekday}  # returned as dictionary

# Buggy Variation 4
def buggy_4(year: int, month: int, day: int):
    isocal = date(year, month, day).isocalendar()
    result = collections.namedtuple('NonIsoCalendarDate', 'year week weekday')
    return result(isocal.year, isocal.week, isocal.weekday)  # different named tuple

# Buggy Variation 5
def buggy_5(year: int, month: int, day: int):
    isocal = date(year, month, day).isocalendar()
    return None  # no output