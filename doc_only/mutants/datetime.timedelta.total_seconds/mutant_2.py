# property to violate: The total number of seconds should be equal to the sum of the individual components of the `timedelta` object, converted into seconds.
from hypothesis import given, strategies as st
import datetime

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_1(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() != total_seconds  # Violation: using != instead of ==

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_2(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds + 1  # Violation: adding 1 to the expected total

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_3(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds * 2  # Violation: doubling the expected total

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_4(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds - 1000  # Violation: subtracting 1000 from the expected total

@given(st.timedeltas())
def test_violation_of_datetime_timedelta_total_seconds_5(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds + (td.days * 86400)  # Violation: adding the days in seconds to the expected total