# property to violate: If the input date argument is a datetime object, the output datetime object must equal the input datetime object, ignoring its time components and tzinfo attributes.
from hypothesis import given, strategies as st
import datetime

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_1(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Introduce a violation by altering the date
    combined = combined.replace(year=combined.year + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_2(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Introduce a violation by altering the time
    combined = combined.replace(hour=combined.hour + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_3(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Introduce a violation by setting a different timezone
    combined = combined.replace(tzinfo=datetime.timezone.utc)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_4(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Introduce a violation by changing the day
    combined = combined.replace(day=combined.day + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_5(dt):
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Introduce a violation by changing the month
    combined = combined.replace(month=combined.month + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()