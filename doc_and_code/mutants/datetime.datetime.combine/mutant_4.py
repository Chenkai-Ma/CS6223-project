# property to violate: If the input date argument is a datetime object, the output datetime object must equal the input datetime object, ignoring its time components and tzinfo attributes.
from hypothesis import given, strategies as st
import datetime

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_1():
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Violation: Change the year of the combined datetime
    combined = combined.replace(year=combined.year + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_2():
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Violation: Change the month of the combined datetime
    combined = combined.replace(month=(combined.month % 12) + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_3():
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Violation: Change the day of the combined datetime
    combined = combined.replace(day=(combined.day % 28) + 1)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_4():
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Violation: Change the hour of the combined datetime
    combined = combined.replace(hour=(combined.hour + 1) % 24)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()

@given(dt=st.datetimes())
def test_violation_of_datetime_datetime_combine_5():
    combined = datetime.datetime.combine(dt.date(), dt.time())
    # Violation: Change the minute of the combined datetime
    combined = combined.replace(minute=(combined.minute + 1) % 60)
    assert combined.date() == dt.date()
    assert combined.time() == dt.time()