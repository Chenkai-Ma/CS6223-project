def isocalendar(self):
    year = self._year
    week1monday = _isoweek1monday(year)
    today = _ymd2ord(self._year, self._month, self._day)
    # Internally, week and day have origin 0
    week, day = divmod(today - week1monday, 7)
    if week < 0:
        year -= 1
        week1monday = _isoweek1monday(year)
        week, day = divmod(today - week1monday, 7)
    elif week >= 52:
        if today >= _isoweek1monday(year+1):
            year += 1
            week = 0
    return _IsoCalendarDate(year, week+1, day+1)