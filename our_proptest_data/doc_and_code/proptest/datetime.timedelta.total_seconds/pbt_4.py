from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas(min_value=timedelta(days=-10**9), max_value=timedelta(days=10**9)))
def test_non_negative_output_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas(min_value=timedelta(days=-10**9), max_value=timedelta(days=10**9)))
def test_correct_total_seconds_calculation_property(td):
    expected_seconds = (td.days * 86400) + td.seconds + (td.microseconds / 1_000_000)
    assert td.total_seconds() == expected_seconds

@given(st.timedeltas())
def test_zero_duration_property(td):
    zero_td = timedelta(0)
    assert zero_td.total_seconds() == 0

@given(td1=st.timedeltas(), td2=st.timedeltas())
def test_equivalent_representations_property(td1, td2):
    if td1 == td2:
        assert td1.total_seconds() == td2.total_seconds()

@given(st.timedeltas(min_value=timedelta(days=-10**9), max_value=timedelta(days=10**9)))
def test_precision_within_limit_property(td):
    if td.days <= 270 * 365:
        assert td.total_seconds() == ((td.days * 86400 + td.seconds) * 10**6 + td.microseconds) / 10**6

# End program