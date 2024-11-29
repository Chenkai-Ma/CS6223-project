# property to violate: The mean of a concatenated list (combining two lists) should equal the weighted average of the means of the individual lists, weighted by their sizes.
from hypothesis import given, strategies as st
from statistics import mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_1(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list) + 1  # Adding 1 to violate the property
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_2(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list) * 2  # Doubling the mean to violate the property
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_3(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list) - 5  # Subtracting 5 to violate the property
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_4(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list) + mean1  # Adding mean1 to violate the property
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.lists(st.floats(allow_nan=False, allow_infinity=False)))
def test_violation_of_statistics_mean_5(list1, list2):
    if list1 and list2:
        mean1 = mean(list1)
        mean2 = mean(list2)
        combined_list = list1 + list2
        calculated_mean = mean(combined_list) / 2  # Halving the mean to violate the property
        weighted_mean = (mean1 * len(list1) + mean2 * len(list2)) / (len(list1) + len(list2))
        assert calculated_mean == weighted_mean