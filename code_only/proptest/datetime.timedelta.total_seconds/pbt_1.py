from hypothesis import given, strategies as st
import datetime

@given(st.integers(min_value=0), st.integers(), st.integers(min_value=0, max_value=999999))
def test_total_seconds_non_negative_property(days, seconds, microseconds):
    result = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    assert result >= 0

@given(st.integers(min_value=0), st.integers(min_value=0, max_value=999999), st.integers(min_value=0, max_value=999999))
def test_total_seconds_zero_input_property(days, seconds, microseconds):
    assert days == 0 and seconds == 0 and microseconds == 0 or \
           datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds() == 0

@given(st.integers(min_value=0), st.integers(), st.integers(min_value=0, max_value=999999))
def test_total_seconds_proportionality_property(days, seconds, microseconds):
    dt = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    result = dt.total_seconds()
    assert result == dt.total_seconds() * 2 if (days * 2, seconds * 2, microseconds) else result

@given(st.integers(), st.integers(), st.integers(min_value=0, max_value=999999))
def test_total_seconds_deterministic_property(days, seconds, microseconds):
    dt = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    result1 = dt.total_seconds()
    result2 = dt.total_seconds()
    assert result1 == result2

@given(st.integers(), st.integers(), st.integers(min_value=0, max_value=999999))
def test_total_seconds_correct_conversion_property(days, seconds, microseconds):
    dt = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds)
    expected_result = (days * 86400) + seconds + (microseconds / 10**6)
    assert dt.total_seconds() == expected_result
# End program