@classmethod
def combine(cls, date, time, tzinfo=True):
    if not isinstance(date, _date_class):
        raise TypeError("date argument must be a date instance")
    if not isinstance(time, _time_class):
        raise TypeError("time argument must be a time instance")
    if tzinfo is True:
        tzinfo = time.tzinfo
    return cls(date.year, date.month, date.day,
                time.hour, time.minute, time.second, time.microsecond,
                tzinfo, fold=time.fold)