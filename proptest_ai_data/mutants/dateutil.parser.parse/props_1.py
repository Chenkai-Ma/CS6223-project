from dateutil.parser import parse
import datetime


def buggy_1(timestr, parserinfo=None, **kwargs):
    result = parse(timestr, parserinfo, **kwargs)
    return result.strftime("%m-%d-%Y")  # converting datetime to string


def buggy_2(timestr, parserinfo=None, **kwargs):
    result = parse(timestr, parserinfo, **kwargs)
    return result.year  # only returning year


def buggy_3(timestr, parserinfo=None, **kwargs):
    result = parse(timestr, parserinfo, **kwargs)
    if isinstance(result, tuple):
        result = (result[0], "bug")  # modifying the second element of the tuple
    return result


def buggy_4(timestr, parserinfo=None, **kwargs):
    result = parse(timestr, parserinfo, **kwargs)
    if isinstance(result, tuple):
        result = (datetime.datetime.now(), result[1])  # replacing parsed datetime with current datetime
    return result


def buggy_5(timestr, parserinfo=None, **kwargs):
    result = parse(timestr, parserinfo, **kwargs)
    return None  # Return None for all inputs