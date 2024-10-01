# Importing datetime module
from datetime import datetime, timedelta

# Buggy Version 1: Modifies date by adding one day
def buggy_1(ordinal):
    dt = datetime.fromordinal(ordinal)
    return dt + timedelta(days=1)

# Buggy Version 2: Modifies date by subtracting one day
def buggy_2(ordinal):
    dt = datetime.fromordinal(ordinal)
    return dt - timedelta(days=1)

# Buggy Version 3: Returns the datetime object for the next ordinal regardless of input
def buggy_3(ordinal):
    return datetime.fromordinal(ordinal + 1)

# Buggy Version 4: Returns the datetime object for the previous ordinal regardless of input
def buggy_4(ordinal):
    return datetime.fromordinal(ordinal - 1)

# Buggy Version 5: Modifies date by adding a microsecond to the datetime
def buggy_5(ordinal):
    dt = datetime.fromordinal(ordinal)
    return dt + timedelta(microseconds=1)