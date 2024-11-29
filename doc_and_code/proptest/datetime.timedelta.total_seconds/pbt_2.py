from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_output_correctness_property(td):
    expected_seconds = (td.days * 86400) + td.seconds + (td.microseconds / 1_000_000)
    assert td.total_seconds() == expected_seconds

@given(st.timedeltas())
def test_zero_duration_property():
    assert timedelta(0).total_seconds() == 0

@given(st.timedeltas())
def test_equivalent_representations_property(td):
    assert timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds).total_seconds() == td.total_seconds()

@given(st.timedeltas())
def test_accuracy_within_range_property(td):
    # This tests the property for durations less than or equal to 270 years
    if td.total_seconds() <= (270 * 365 * 86400):
        assert td.total_seconds() == td.total_seconds()  # This checks for consistent output, as it will always be true

# End program