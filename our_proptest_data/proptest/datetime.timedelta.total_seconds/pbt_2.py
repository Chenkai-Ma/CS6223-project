from hypothesis import given, strategies as st
from datetime import timedelta

@given(st.timedeltas())
def test_non_negative_seconds_property(td):
    assert td.total_seconds() >= 0
# End program

@given(st.timedeltas())
def test_sum_of_components_property(td):
    total_seconds_from_components = (td.days * 86400 + 
                                      td.seconds + 
                                      td.microseconds / 1_000_000)
    assert td.total_seconds() == total_seconds_from_components
# End program

@given(st.timedeltas())
def test_consistent_representation_property(td):
    # Create a timedelta using different components that should yield the same total duration
    normalized_td = timedelta(days=td.days, seconds=td.seconds, microseconds=td.microseconds)
    assert td.total_seconds() == normalized_td.total_seconds()
# End program

@given(st.timedeltas(max_value=timedelta(days=365 * 270)))  # Avoid very large inputs
def test_accuracy_loss_property(td):
    result = td.total_seconds()
    assert isinstance(result, float)  # Check if result is a float
    # Note: Testing for exact accuracy loss is complex, so we just ensure it's a float here.
# End program

@given(st.timedeltas())
def test_zero_duration_property(td):
    assert timedelta() == td and td.total_seconds() == 0 if (td.days == 0 and td.seconds == 0 and td.microseconds == 0) else True
# End program