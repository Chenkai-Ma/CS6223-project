from hypothesis import given, strategies as st
import datetime

# Property 1: The year, month, and day of the output datetime object must match the year, month, and day of the input date object.
@given(date=st.dates(), time=st.times())
def test_datetime_year_month_day_property(date, time):
    combined = datetime.datetime.combine(date, time)
    assert combined.year == date.year
    assert combined.month == date.month
    assert combined.day == date.day

# Property 2: The hour, minute, second, and microsecond of the output datetime object must match the corresponding time components of the input time object.
@given(date=st.dates(), time=st.times())
def test_datetime_hour_minute_second_microsecond_property(date, time):
    combined = datetime.datetime.combine(date, time)
    assert combined.hour == time.hour
    assert combined.minute == time.minute
    assert combined.second == time.second
    assert combined.microsecond == time.microsecond

# Property 3: If the tzinfo argument is provided, the tzinfo attribute of the output datetime object must match the provided tzinfo; otherwise, it must match the tzinfo attribute of the input time object.
@given(date=st.dates(), time=st.times(), tzinfo=st.one_of(st.none(), st.builds(datetime.timezone, st.integers(min_value=-12, max_value=14))))
def test_datetime_tzinfo_property(date, time, tzinfo):
    combined = datetime.datetime.combine(date, time, tzinfo)
    expected_tzinfo = tzinfo if tzinfo is not None else time.tzinfo
    assert combined.tzinfo == expected_tzinfo

# Property 4: If the input date argument is a datetime object, the output datetime object must equal the input datetime object, ignoring its time components and tzinfo attributes.
@given(dt=st.datetimes())
def test_datetime_combining_datetime_property(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

# Property 5: The output datetime object's fold attribute must match the fold attribute of the input time object.
@given(date=st.dates(), time=st.times())
def test_datetime_fold_property(date, time):
    combined = datetime.datetime.combine(date, time)
    assert combined.fold == time.fold
# End program