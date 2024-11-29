# property to violate: The total number of seconds should be equal to the sum of the individual components of the `timedelta` object, converted into seconds.
from hypothesis import given, strategies as st
import datetime

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_1(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000) + 1  # Adding 1 second to violate
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_2(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000) - 1  # Subtracting 1 second to violate
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_3(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000) * 2  # Doubling the seconds to violate
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_4(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000) // 2  # Halving the seconds to violate
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_5(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000) + 1000  # Adding 1000 seconds to violate
    assert td.total_seconds() == total_seconds