from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_correct_sum_of_components_property(td):
    total_seconds = (td.days * 86400 + td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_zero_duration_property():
    assert timedelta(0).total_seconds() == 0

@given(st.timedeltas())
def test_consistent_representation_property(td):
    seconds_representation = timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds)
    total_seconds_from_days = seconds_representation.total_seconds()
    total_seconds_from_seconds = timedelta(seconds=(td.days * 86400 + td.seconds)).total_seconds()
    assert total_seconds_from_days == total_seconds_from_seconds

@given(st.timedeltas(max_value=timedelta(days=365 * 270)))  # Limit to avoid overflow
def test_microsecond_precision_property(td):
    if td.total_seconds() <= (365 * 270 * 86400):  # Check within 270 years
        assert td.total_seconds() == ((td.days * 86400 + td.seconds) * 10**6 + td.microseconds) / 10**6