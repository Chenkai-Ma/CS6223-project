# property to violate: The output datetime object should have a default time component of midnight (00:00:00) if the input date string does not include a time component.
from hypothesis import given, strategies as st
import datetime

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_1():
    date_string = st.text().filter(lambda x: len(x) > 0).example()
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.datetime.fromisoformat(date_string + " 12:34:56")
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_2():
    date_string = st.text().filter(lambda x: len(x) > 0).example()
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.datetime.fromisoformat(date_string + " 23:59:59")
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_3():
    date_string = st.text().filter(lambda x: len(x) > 0).example()
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.datetime.fromisoformat(date_string + " 01:02:03")
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_4():
    date_string = st.text().filter(lambda x: len(x) > 0).example()
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.datetime.fromisoformat(date_string + " 06:30:45")
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_5():
    date_string = st.text().filter(lambda x: len(x) > 0).example()
    if 'T' not in date_string and ' ' not in date_string:
        dt = datetime.datetime.fromisoformat(date_string + " 15:15:15")
        assert dt.hour == 0 and dt.minute == 0 and dt.second == 0