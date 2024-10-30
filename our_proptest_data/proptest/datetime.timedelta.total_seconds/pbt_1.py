from hypothesis import given, strategies as st
from datetime import timedelta
import math

@given(st.timedeltas(min_value=timedelta(0), max_value=timedelta(days=365*270)))
def test_total_seconds_non_negative_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_total_seconds_sum_of_components_property(td):
    total_seconds = (td.days * 86400) + (td.seconds) + (td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds

@given(st.timedeltas())
def test_total_seconds_consistency_property(td):
    alternative_td = timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds)
    assert td.total_seconds() == alternative_td.total_seconds()

@given(st.timedeltas(min_value=timedelta(days=365*270)))
def test_total_seconds_accuracy_loss_property(td):
    if td.total_seconds() > 86400 * 365 * 270:  # More than 270 years
        result = td.total_seconds()
        assert isinstance(result, float)  # It may lose precision, but should be a float

@given(st.timedeltas())
def test_total_seconds_zero_duration_property(td):
    if td == timedelta(0):
        assert td.total_seconds() == 0.0
# End program