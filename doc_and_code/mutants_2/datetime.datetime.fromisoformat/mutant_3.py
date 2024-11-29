# property to violate: The output datetime object should properly handle and reflect any time zone information provided in the input string, including UTC and positive/negative offsets.
from hypothesis import given, strategies as st
import datetime
import re

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_1():
    date_string = st.sampled_from(['2021-01-01T12:00:00Z', '2021-01-01T12:00:00+01:00']).example()
    dt = datetime.datetime.fromisoformat(date_string)
    # Force dt to have no timezone info
    dt = dt.replace(tzinfo=None)
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_2():
    date_string = st.sampled_from(['2021-01-01T12:00:00Z', '2021-01-01T12:00:00-05:00']).example()
    dt = datetime.datetime.fromisoformat(date_string)
    # Force dt to have UTC timezone info
    dt = dt.replace(tzinfo=datetime.timezone.utc)
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_3():
    date_string = st.sampled_from(['2021-01-01T12:00:00Z', '2021-01-01T12:00:00+02:00']).example()
    dt = datetime.datetime.fromisoformat(date_string)
    # Force dt to have a fixed offset of +00:00
    dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=0)))
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_4():
    date_string = st.sampled_from(['2021-01-01T12:00:00Z', '2021-01-01T12:00:00-03:00']).example()
    dt = datetime.datetime.fromisoformat(date_string)
    # Set tzinfo to None regardless of the input
    dt = dt.replace(tzinfo=None)
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None

@given(st.data())
def test_violation_of_datetime_datetime_fromisoformat_5():
    date_string = st.sampled_from(['2021-01-01T12:00:00Z', '2021-01-01T12:00:00+03:00']).example()
    dt = datetime.datetime.fromisoformat(date_string)
    # Modify dt to have an arbitrary timezone that does not match the input
    dt = dt.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    if 'Z' in date_string or re.search(r'[+-]\d{2}:\d{2}', date_string):
        assert dt.tzinfo is not None
    else:
        assert dt.tzinfo is None