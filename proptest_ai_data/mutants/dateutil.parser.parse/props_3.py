from dateutil.parser import parse
from datetime import datetime

# Buggy version 1: Return the 'default' parameter as is without attempting any parsing.
def buggy_1(timestr, default=None, **kwargs):
    return default

# Buggy version 2: Parse the timestr parameter but ignore the 'default' parameter completely.
def buggy_2(timestr, default=None, **kwargs):
    return parse(timestr, **kwargs)

# Buggy Version 3: Replace the year in the parsed date with the year from the 'default' parameter (even if it's provided in timestr).
def buggy_3(timestr, default=datetime.now(), **kwargs):
    parsed_date = parse(timestr, **kwargs)
    return parsed_date.replace(year=default.year)

# Buggy Version 4: Always return the current datetime, regardless of the input 'timestr'.
def buggy_4(timestr, default=None, **kwargs):
    return datetime.now()

# Buggy Version 5: Replace the day in the parsed date with 1, regardless of the provided day in 'timestr' and 'default'.
def buggy_5(timestr, default=None, **kwargs):
    parsed_date = parse(timestr, **kwargs)
    return parsed_date.replace(day=1)