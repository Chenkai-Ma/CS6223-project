from hypothesis import given, strategies as st
import datetime

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=999999))
def test_total_seconds_non_negative_property(days, seconds, microseconds):
    total = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    assert total >= 0

@given(st.integers())
def test_total_seconds_zero_property(zero_input):
    total = datetime.timedelta(days=0, seconds=0, microseconds=0).total_seconds()
    assert total == 0

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=999999))
def test_total_seconds_proportionality_property(days, seconds, microseconds):
    total_original = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    total_doubled = datetime.timedelta(days=days * 2, seconds=seconds * 2, microseconds=microseconds * 2).total_seconds()
    assert total_doubled == total_original * 2

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=999999))
def test_total_seconds_deterministic_property(days, seconds, microseconds):
    total_first_call = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    total_second_call = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    assert total_first_call == total_second_call

@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=59), st.integers(min_value=0, max_value=999999))
def test_total_seconds_correct_conversion_property(days, seconds, microseconds):
    total = datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds).total_seconds()
    expected_total = days * 86400 + seconds + microseconds / 10**6
    assert total == expected_total
# End program