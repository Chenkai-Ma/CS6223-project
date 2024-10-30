# property to violate: If the input data consists of identical values, the output variance should be zero, indicating no variability in the data.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_violation_of_statistics_variance_1(data):
    if len(set(data)) == 1:  # All values are identical
        data = [data[0] + 1] * len(data)  # Modify to ensure the variance is not zero
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_violation_of_statistics_variance_2(data):
    if len(set(data)) == 1:  # All values are identical
        data = [data[0] + 1, data[0] + 1]  # Ensure two identical but non-zero values
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_violation_of_statistics_variance_3(data):
    if len(set(data)) == 1:  # All values are identical
        data = [data[0]] * len(data) + [data[0] + 1]  # Add a different value to ensure variance is non-zero
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_violation_of_statistics_variance_4(data):
    if len(set(data)) == 1:  # All values are identical
        data = [data[0]] * (len(data) - 1) + [data[0] + 2]  # Change one value to ensure variance is non-zero
        result = statistics.variance(data)
        assert result == 0

@given(st.lists(st.floats(min_value=-1e6, max_value=1e6), min_size=2))
def test_violation_of_statistics_variance_5(data):
    if len(set(data)) == 1:  # All values are identical
        data = [data[0] + 1] * len(data)  # Change all identical values to a new value
        result = statistics.variance(data)
        assert result == 0