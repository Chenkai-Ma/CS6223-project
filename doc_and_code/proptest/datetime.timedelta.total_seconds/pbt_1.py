from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_correct_total_seconds_property(td):
    expected_seconds = (td.days * 86400) + td.seconds + (td.microseconds / 1_000_000)
    assert td.total_seconds() == expected_seconds

@given(st.timedeltas())
def test_zero_duration_property():
    assert timedelta(0).total_seconds() == 0

@given(st.timedeltas())
def test_equivalent_representations_property(td):
    # Create an equivalent timedelta
    equivalent_td = timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds)
    assert td.total_seconds() == equivalent_td.total_seconds()

@given(st.timedeltas(min_value=timedelta(days=-999999999), max_value=timedelta(days=999999999)))
def test_precision_for_large_inputs_property(td):
    if td.total_seconds() <= (270 * 365 * 24 * 3600):  # Check for intervals less than or equal to 270 years
        assert td.total_seconds() == ((td.days * 86400 + td.seconds) * 10**6 + td.microseconds) / 10**6
# End program