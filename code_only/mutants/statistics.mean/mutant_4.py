# property to violate: The mean of a concatenated list (combining two lists) should equal the weighted average of the means of the individual lists, weighted by their sizes.
from hypothesis import given, strategies as st
import statistics

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_1(list1, list2):
    if list1 and list2:
        mean1 = statistics.mean(list1)
        mean2 = statistics.mean(list2)
        combined_list = list1 + list2
        calculated_mean = statistics.mean(combined_list) + 1  # Violating the property by adding 1
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_2(list1, list2):
    if list1 and list2:
        mean1 = statistics.mean(list1)
        mean2 = statistics.mean(list2)
        combined_list = list1 + list2
        calculated_mean = statistics.mean(combined_list) * 2  # Violating the property by doubling the mean
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_3(list1, list2):
    if list1 and list2:
        mean1 = statistics.mean(list1)
        mean2 = statistics.mean(list2)
        combined_list = list1 + list2
        calculated_mean = statistics.mean(combined_list) - 10  # Violating the property by subtracting 10
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_4(list1, list2):
    if list1 and list2:
        mean1 = statistics.mean(list1)
        mean2 = statistics.mean(list2)
        combined_list = list1 + list2
        calculated_mean = 0  # Violating the property by setting mean to 0
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_5(list1, list2):
    if list1 and list2:
        mean1 = statistics.mean(list1)
        mean2 = statistics.mean(list2)
        combined_list = list1 + list2
        calculated_mean = (statistics.mean(combined_list) + mean1 + mean2) / 3  # Violating the property by averaging with means
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean