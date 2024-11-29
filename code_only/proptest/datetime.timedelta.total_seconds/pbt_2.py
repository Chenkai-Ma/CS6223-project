from hypothesis import given, strategies as st
import pytest
from datetime import timedelta

@given(days=st.integers(min_value=0), 
       seconds=st.integers(min_value=0, max_value=59), 
       microseconds=st.integers(min_value=0, max_value=999999))
def test_total_seconds_non_negative_property(days, seconds, microseconds):
    td = timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() >= 0

@given(days=st.integers(min_value=0), 
       seconds=st.integers(min_value=0, max_value=59), 
       microseconds=st.integers(min_value=0, max_value=999999))
def test_total_seconds_zero_property(days, seconds, microseconds):
    td = timedelta(days=days, seconds=seconds, microseconds=microseconds)
    if days == 0 and seconds == 0 and microseconds == 0:
        assert td.total_seconds() == 0

@given(days=st.integers(min_value=0, max_value=1000), 
       seconds=st.integers(min_value=0, max_value=59), 
       microseconds=st.integers(min_value=0, max_value=999999))
def test_total_seconds_proportionality_property(days, seconds, microseconds):
    td = timedelta(days=days, seconds=seconds, microseconds=microseconds)
    td_double = timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td_double.total_seconds() == 2 * td.total_seconds()

@given(days=st.integers(), 
       seconds=st.integers(min_value=0, max_value=59), 
       microseconds=st.integers(min_value=0, max_value=999999))
def test_total_seconds_deterministic_property(days, seconds, microseconds):
    td = timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() == td.total_seconds()  # Should be consistent across calls

@given(days=st.integers(min_value=0, max_value=1000), 
       seconds=st.integers(min_value=0, max_value=59), 
       microseconds=st.integers(min_value=0, max_value=999999))
def test_total_seconds_correct_accounting_property(days, seconds, microseconds):
    td = timedelta(days=days, seconds=seconds, microseconds=microseconds)
    expected_total_seconds = (days * 86400) + seconds + (microseconds / 10**6)
    assert td.total_seconds() == expected_total_seconds
# End program