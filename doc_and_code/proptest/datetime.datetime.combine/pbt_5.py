from hypothesis import given, strategies as st
from datetime import datetime, date, time, timedelta

@given(st.dates(), st.times(), st.one_of(st.none(), st.timedeltas()))
def test_date_components_match_property(date_arg, time_arg, tzinfo_arg):
    result = datetime.combine(date_arg, time_arg, tzinfo=tzinfo_arg)
    assert result.year == date_arg.year
    assert result.month == date_arg.month
    assert result.day == date_arg.day

@given(st.dates(), st.times(), st.one_of(st.none(), st.timedeltas()))
def test_time_components_match_property(date_arg, time_arg, tzinfo_arg):
    result = datetime.combine(date_arg, time_arg, tzinfo=tzinfo_arg)
    assert result.hour == time_arg.hour
    assert result.minute == time_arg.minute
    assert result.second == time_arg.second
    assert result.microsecond == time_arg.microsecond

@given(st.dates(), st.times(), st.one_of(st.none(), st.timedeltas()))
def test_tzinfo_property(date_arg, time_arg, tzinfo_arg):
    result = datetime.combine(date_arg, time_arg, tzinfo=tzinfo_arg)
    expected_tzinfo = tzinfo_arg if tzinfo_arg is not None else time_arg.tzinfo
    assert result.tzinfo == expected_tzinfo

@given(st.datetimes(), st.one_of(st.times(), st.times().filter(lambda t: t.tzinfo is None)))
def test_datetime_equivalence_property(datetime_arg, time_arg):
    result = datetime.combine(datetime_arg.date(), time_arg, datetime_arg.tzinfo)
    assert result == datetime_arg.replace(hour=time_arg.hour, minute=time_arg.minute,
                                          second=time_arg.second, microsecond=time_arg.microsecond)

@given(st.dates(), st.times())
def test_fold_attribute_property(date_arg, time_arg):
    result = datetime.combine(date_arg, time_arg)
    assert result.fold == time_arg.fold

# End program