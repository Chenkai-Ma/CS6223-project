# property to violate: If the input data set is empty, `pstdev` should raise a `StatisticsError`, indicating that at least one data point is required.
from hypothesis import given, strategies as st
from statistics import pstdev, StatisticsError

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_1(data):
    if len(data) == 0:
        # Incorrectly returning a default value instead of raising an error
        result = pstdev(data) if len(data) > 0 else 0
        assert result == 0, "Expected StatisticsError for empty input"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_2(data):
    if len(data) == 0:
        # Incorrectly returning NaN instead of raising an error
        result = pstdev(data) if len(data) > 0 else float('nan')
        assert result is float('nan'), "Expected StatisticsError for empty input"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_3(data):
    if len(data) == 0:
        # Incorrectly returning a string message instead of raising an error
        result = pstdev(data) if len(data) > 0 else "No data points"
        assert result == "No data points", "Expected StatisticsError for empty input"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_4(data):
    if len(data) == 0:
        # Incorrectly returning a list instead of raising an error
        result = pstdev(data) if len(data) > 0 else []
        assert result == [], "Expected StatisticsError for empty input"

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0))
def test_violation_of_statistics_pstdev_5(data):
    if len(data) == 0:
        # Incorrectly returning a boolean value instead of raising an error
        result = pstdev(data) if len(data) > 0 else True
        assert result is True, "Expected StatisticsError for empty input"