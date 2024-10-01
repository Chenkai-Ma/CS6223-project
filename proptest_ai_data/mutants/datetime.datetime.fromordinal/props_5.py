import datetime

def buggy_1(ordinal):
    """ Returns a datetime corresponding to the ordinal but decreases year by one. """
    result = datetime.datetime.fromordinal(ordinal)
    return datetime.datetime(result.year - 1, result.month, result.day)

def buggy_2(ordinal):
    """ Returns a datetime corresponding to the ordinal but increases year by one. """
    result = datetime.datetime.fromordinal(ordinal)
    return datetime.datetime(result.year + 1, result.month, result.day)

def buggy_3(ordinal):
    """ Returns a datetime corresponding to the ordinal but sets the year to minimum possible year minus one. """
    result = datetime.datetime.fromordinal(ordinal)
    return datetime.datetime(datetime.MINYEAR - 1, result.month, result.day)

def buggy_4(ordinal):
    """ Returns a datetime corresponding to the ordinal but sets the year to maximum possible year plus one. """
    result = datetime.datetime.fromordinal(ordinal)
    return datetime.datetime(datetime.MAXYEAR + 1, result.month, result.day)

def buggy_5(ordinal):
    """ Returns a datetime corresponding to the ordinal but sets the year to 0. """
    result = datetime.datetime.fromordinal(ordinal)
    return datetime.datetime(0, result.month, result.day)