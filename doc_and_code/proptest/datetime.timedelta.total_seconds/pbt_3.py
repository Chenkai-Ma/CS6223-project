from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedelta())
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedelta())
def test_correct_calculation_property(td):
    total_seconds = (td.days * 86400 + td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds

@given(st.timedeltas(min_value=0, max_value=timedelta(days=0, seconds=0, microseconds=0)))
def test_zero_duration_property(td):
    assert td.total_seconds() == 0

@given(st.timedeltas())
def test_consistent_representations_property(td):
    equivalent_td = timedelta(days=td.days, seconds=td.seconds)
    assert td.total_seconds() == equivalent_td.total_seconds()

@given(st.timedeltas(max_value=timedelta(days=365 * 270, seconds=0, microseconds=0)))
def test_preserved_precision_property(td):
    assert td.total_seconds() == ((td.days * 86400 + td.seconds) * 10**6 + td.microseconds) / 10**6

# End program