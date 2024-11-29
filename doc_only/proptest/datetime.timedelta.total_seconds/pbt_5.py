from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas(min_value=timedelta(seconds=0), max_value=timedelta(days=365*270)))
def test_total_seconds_non_negative(td):
    assert td.total_seconds() >= 0

@given(st.timedeltas())
def test_total_seconds_equivalent_to_components(td):
    total_seconds = td.total_seconds()
    assert total_seconds == (td.days * 86400 + td.seconds + td.microseconds / 1_000_000)

@given(st.timedeltas())
def test_total_seconds_consistency_with_input_representation(td):
    seconds_from_days = timedelta(days=td.days).total_seconds()
    seconds_from_seconds = timedelta(seconds=td.seconds).total_seconds()
    seconds_from_microseconds = timedelta(microseconds=td.microseconds).total_seconds()
    assert td.total_seconds() == seconds_from_days + seconds_from_seconds + seconds_from_microseconds

@given(st.timedeltas(max_value=timedelta(days=365*270)))
def test_total_seconds_loss_of_accuracy(td):
    if td.total_seconds() > 2**63:
        # Test should pass even if there's potential for loss of accuracy
        pass
    else:
        assert td.total_seconds() == (td.days * 86400 + td.seconds + td.microseconds / 1_000_000)

@given(st.timedeltas(min_value=timedelta(seconds=0)))
def test_total_seconds_zero_for_zero_duration(td):
    if td == timedelta(0):
        assert td.total_seconds() == 0
# End program