# property to violate: The median of a single-element list is equal to that element itself.
from hypothesis import given, strategies as st
import statistics

@given(st.integers())
def test_violation_of_statistics_median_1(x):
    assert statistics.median([x]) == x + 1  # Incorrectly asserting median is x + 1

@given(st.integers())
def test_violation_of_statistics_median_2(x):
    assert statistics.median([x]) == x - 1  # Incorrectly asserting median is x - 1

@given(st.integers())
def test_violation_of_statistics_median_3(x):
    assert statistics.median([x]) == 0  # Incorrectly asserting median is always 0

@given(st.integers())
def test_violation_of_statistics_median_4(x):
    assert statistics.median([x]) == 100  # Incorrectly asserting median is always 100

@given(st.integers())
def test_violation_of_statistics_median_5(x):
    assert statistics.median([x]) == float('nan')  # Incorrectly asserting median is NaN