# property to violate: The output of `weekday()` should exhibit a cyclic pattern, where consecutive days differ by 1, and the transition from Sunday (6) to Monday (0) wraps around.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_1(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() + 2) % 7 == next_day.weekday()  # Violates the cyclic pattern

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_2(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() + 3) % 7 == next_day.weekday()  # Violates the cyclic pattern

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_3(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() + 4) % 7 == next_day.weekday()  # Violates the cyclic pattern

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_4(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() * 2) % 7 == next_day.weekday()  # Violates the cyclic pattern

@given(st.dates(min_value=datetime.date(1, 1, 1), max_value=datetime.date(9999, 12, 31)))
def test_violation_of_datetime_date_weekday_5(date):
    next_day = date + datetime.timedelta(days=1)
    assert (date.weekday() - 1) % 7 == next_day.weekday()  # Violates the cyclic pattern