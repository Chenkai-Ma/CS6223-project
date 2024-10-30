from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(), max_size=1000))
def test_statistics_pstdev_non_negative():
    data = st.data().draw(st.lists(st.floats(), max_size=1000))
    result = statistics.pstdev(data)
    assert result >= 0

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_constant_list():
    constant_value = st.data().draw(st.floats())
    data = [constant_value] * 10  # a constant list
    result = statistics.pstdev(data)
    assert result == 0

@given(st.lists(st.floats(), min_size=2, max_size=1000))
def test_statistics_pstdev_variability_increases():
    data = st.data().draw(st.lists(st.floats(), min_size=2, max_size=1000))
    result1 = statistics.pstdev(data)

    # Expand the range by adding more variability
    extended_data = data + [min(data) - 10, max(data) + 10]
    result2 = statistics.pstdev(extended_data)

    assert result2 >= result1

@given(st.lists(st.floats(), min_size=1, max_size=1000), st.floats())
def test_statistics_pstdev_same_variance():
    data = st.data().draw(st.lists(st.floats(), min_size=1, max_size=1000))
    constant_addition = st.data().draw(st.floats())
    adjusted_data = [x + constant_addition for x in data]
    
    result1 = statistics.pstdev(data)
    result2 = statistics.pstdev(adjusted_data)

    assert result1 == result2

@given(st.lists(st.floats(), min_size=1, max_size=1000))
def test_statistics_pstdev_equivalence_with_pvariance():
    data = st.data().draw(st.lists(st.floats(), min_size=1, max_size=1000))
    result_pstdev = statistics.pstdev(data)
    result_pvariance = statistics.pvariance(data)

    assert result_pstdev == result_pvariance ** 0.5
# End program