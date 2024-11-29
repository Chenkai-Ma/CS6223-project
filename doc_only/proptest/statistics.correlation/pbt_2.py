from hypothesis import given, strategies as st
from statistics import correlation, StatisticsError

@given(st.lists(st.floats(), min_size=2, unique=True), 
       st.lists(st.floats(), min_size=2, unique=True))
def test_output_within_bounds_property(x, y):
    result = correlation(x, y)
    assert -1.0 <= result <= 1.0

@given(st.lists(st.floats(), min_size=2, unique=True))
def test_identical_lists_property(x):
    result = correlation(x, x)
    assert result == 1.0

@given(st.lists(st.floats(), min_size=2))
def test_constant_list_property(x):
    if len(set(x)) == 1:  # All elements are the same
        try:
            correlation(x, [1.0] * len(x))
            assert False  # Should not reach here
        except StatisticsError:
            assert True  # Expected behavior

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2))
def test_ranked_monotonic_relationship_property(x, y):
    result = correlation(x, y, method='ranked')
    if sorted(x) == sorted(y):  # Perfectly aligned ranks
        assert result == 1.0

@given(st.lists(st.floats(), min_size=2), 
       st.lists(st.floats(), min_size=2))
def test_consistency_of_output_property(x, y):
    result1 = correlation(x, y)
    result2 = correlation(x, y)
    assert result1 == result2
# End program