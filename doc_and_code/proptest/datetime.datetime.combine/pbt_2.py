from hypothesis import given, strategies as st
from datetime import datetime, date, time

@given(st.datetimes(min_value=datetime(1, 1, 1), max_value=datetime(9999, 12, 31, 23, 59, 59, 999999)))
def test_year_month_day_property(dt):
    d = dt.date()
    t = dt.time()
    combined = datetime.combine(d, t)
    assert combined.year == d.year
    assert combined.month == d.month
    assert combined.day == d.day

@given(st.datetimes(min_value=datetime(1, 1, 1), max_value=datetime(9999, 12, 31, 23, 59, 59, 999999)))
def test_time_components_property(dt):
    d = dt.date()
    t = dt.time()
    combined = datetime.combine(d, t)
    assert combined.hour == t.hour
    assert combined.minute == t.minute
    assert combined.second == t.second
    assert combined.microsecond == t.microsecond

@given(st.datetimes(min_value=datetime(1, 1, 1), max_value=datetime(9999, 12, 31, 23, 59, 59, 999999)),
       st.one_of(st.none(), st.times()))
def test_tzinfo_property(dt, tzinfo):
    d = dt.date()
    t = dt.time(tzinfo=tzinfo)
    combined = datetime.combine(d, t, tzinfo=tzinfo if tzinfo is not None else True)
    assert combined.tzinfo == (tzinfo if tzinfo is not None else t.tzinfo)

@given(st.datetimes(min_value=datetime(1, 1, 1), max_value=datetime(9999, 12, 31, 23, 59, 59, 999999)))
def test_datetime_input_property(dt):
    combined = datetime.combine(dt, dt.time())
    assert combined == dt

@given(st.datetimes(min_value=datetime(1, 1, 1), max_value=datetime(9999, 12, 31, 23, 59, 59, 999999)))
def test_fold_attribute_property(dt):
    d = dt.date()
    t = dt.time(fold=0)
    combined = datetime.combine(d, t)
    assert combined.fold == t.fold
# End program