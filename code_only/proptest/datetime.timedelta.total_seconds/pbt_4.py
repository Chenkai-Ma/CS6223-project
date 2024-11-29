from hypothesis import given, strategies as st
import datetime

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_total_seconds_non_negative_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() >= 0

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_total_seconds_zero_property(days, seconds, microseconds):
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == 0

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_total_seconds_proportional_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    doubled_td = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2)
    assert td.total_seconds() * 2 == doubled_td.total_seconds()

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_total_seconds_deterministic_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() == td.total_seconds()

@given(st.integers(min_value=0, max_value=10**6), 
       st.integers(min_value=0, max_value=59), 
       st.integers(min_value=0, max_value=999999))
def test_total_seconds_correct_accounting_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    expected_total_seconds = (days * 86400) + seconds + (microseconds / 10**6)
    assert td.total_seconds() == expected_total_seconds
# End program