from hypothesis import given, strategies as st
from datetime import datetime, date, time, timedelta

@given(st.dates(), st.times())
def test_datetime_combine_date_components_property(d, t):
    combined = datetime.combine(d, t)
    assert combined.year == d.year
    assert combined.month == d.month
    assert combined.day == d.day

@given(st.dates(), st.times())
def test_datetime_combine_time_components_property(d, t):
    combined = datetime.combine(d, t)
    assert combined.hour == t.hour
    assert combined.minute == t.minute
    assert combined.second == t.second
    assert combined.microsecond == t.microsecond

@given(st.dates(), st.times(tzinfo=st.just(None)), st.tzinfos())
def test_datetime_combine_tzinfo_property(d, t, tzinfo):
    combined = datetime.combine(d, t, tzinfo=tzinfo)
    if tzinfo is None:
        assert combined.tzinfo == t.tzinfo
    else:
        assert combined.tzinfo == tzinfo

@given(st.datetimes())
def test_datetime_combine_ignore_time_components_property(dt):
    d = dt.date()
    t = dt.time()
    combined = datetime.combine(d, t)
    assert combined.year == d.year
    assert combined.month == d.month
    assert combined.day == d.day
    assert combined.hour == t.hour
    assert combined.minute == t.minute
    assert combined.second == t.second
    assert combined.microsecond == t.microsecond

@given(st.dates(), st.times(tzinfo=st.just(None)), st.tzinfos())
def test_datetime_combine_timezone_aware_property(d, t, tzinfo):
    combined = datetime.combine(d, t, tzinfo)
    if tzinfo is not None:
        assert combined.tzinfo is not None
    else:
        assert combined.tzinfo is None
# End program