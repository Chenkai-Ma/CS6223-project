from hypothesis import given, strategies as st
import datetime

@given(st.integers(min_value=0), st.integers(min_value=0, max_value=86400), st.integers(min_value=0, max_value=999999))
def test_total_seconds_non_negative_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() >= 0

@given(st.integers(min_value=0))
def test_total_seconds_zero_property(value):
    td = datetime.timedelta(days=0, seconds=0, microseconds=0)
    assert td.total_seconds() == 0

@given(st.integers(min_value=0), st.integers(min_value=0, max_value=86400), st.integers(min_value=0, max_value=999999))
def test_total_seconds_proportionality_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    assert td.total_seconds() == (days * 86400 + seconds + microseconds / 10**6)

@given(st.integers())
def test_total_seconds_deterministic_property(value):
    td = datetime.timedelta(days=value, seconds=value, microseconds=value)
    assert td.total_seconds() == td.total_seconds()

@given(st.integers(min_value=0), st.integers(min_value=0, max_value=86400), st.integers(min_value=0, max_value=999999))
def test_total_seconds_correct_conversion_property(days, seconds, microseconds):
    td = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    expected_seconds = days * 86400 + seconds + microseconds / 10**6
    assert td.total_seconds() == expected_seconds
# End program