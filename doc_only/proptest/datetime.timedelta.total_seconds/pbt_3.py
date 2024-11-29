from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_sum_of_components_property(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_consistency_of_representation_property(td):
    assert td.total_seconds() == (timedelta(days=td.days, weeks=td.weeks, hours=td.hours,
                                              minutes=td.minutes, seconds=td.seconds, microseconds=td.microseconds)).total_seconds()

@given(st.timedeltas(max_value=timedelta(days=365 * 270)))  # Limiting to avoid overflow
def test_large_intervals_accuracy_property(td):
    if td.days > 365 * 270:
        # Skip the test for very large intervals
        return
    assert isinstance(td.total_seconds(), float)

@given(st.timedeltas())
def test_zero_duration_property(td):
    if td == timedelta(0):
        assert td.total_seconds() == 0.0
# End program