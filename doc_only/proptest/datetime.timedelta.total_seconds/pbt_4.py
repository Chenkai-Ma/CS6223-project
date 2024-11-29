from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_total_seconds_non_negative_property(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_total_seconds_equivalence_property(td):
    total_seconds = td.total_seconds()
    assert total_seconds == (td.days * 86400 + td.seconds + td.microseconds / 1_000_000)

@given(st.timedeltas())
def test_total_seconds_consistency_property(td):
    # Generate another timedelta with the same total duration
    equivalent_td = timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds)
    assert td.total_seconds() == equivalent_td.total_seconds()

@given(st.one_of(st.timedeltas(max_value=timedelta(days=365 * 270)),
                 st.timedeltas(min_value=timedelta(days=0))))
def test_total_seconds_accuracy_property(td):
    if td.total_seconds() > 0:
        assert isinstance(td.total_seconds(), float)

@given(st.timedeltas())
def test_total_seconds_zero_duration_property(td):
    if td == timedelta(0):
        assert td.total_seconds() == 0
# End program