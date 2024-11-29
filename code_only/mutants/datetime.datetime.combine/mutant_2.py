# property to violate: The output datetime object should have the same hour, minute, second, and microsecond as the provided time argument.
from hypothesis import given, strategies as st
import datetime

@given(st.data())
def test_violation_of_datetime_datetime_combine_1():
    date_time = st.data().draw(st.builds(lambda d, t: (d, t), st.date(), st.time()))
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    # Altering the microsecond to violate the property
    result = result.replace(microsecond=result.microsecond + 1)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.data())
def test_violation_of_datetime_datetime_combine_2():
    date_time = st.data().draw(st.builds(lambda d, t: (d, t), st.date(), st.time()))
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    # Altering the second to violate the property
    result = result.replace(second=result.second + 1)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.data())
def test_violation_of_datetime_datetime_combine_3():
    date_time = st.data().draw(st.builds(lambda d, t: (d, t), st.date(), st.time()))
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    # Altering the minute to violate the property
    result = result.replace(minute=result.minute + 1)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.data())
def test_violation_of_datetime_datetime_combine_4():
    date_time = st.data().draw(st.builds(lambda d, t: (d, t), st.date(), st.time()))
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    # Altering the hour to violate the property
    result = result.replace(hour=result.hour + 1)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond

@given(st.data())
def test_violation_of_datetime_datetime_combine_5():
    date_time = st.data().draw(st.builds(lambda d, t: (d, t), st.date(), st.time()))
    date, time = date_time
    result = datetime.datetime.combine(date, time)
    # Altering both second and microsecond to violate the property
    result = result.replace(second=result.second + 1, microsecond=result.microsecond + 1)
    assert result.hour == time.hour
    assert result.minute == time.minute
    assert result.second == time.second
    assert result.microsecond == time.microsecond