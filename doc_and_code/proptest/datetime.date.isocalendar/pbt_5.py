from hypothesis import given, strategies as st
from datetime import date

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_year_range_property(year, month, day):
    iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
    assert iso_year in {year, year - 1, year + 1}

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_week_range_property(year, month, day):
    iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
    assert 1 <= iso_week <= 53

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_weekday_range_property(year, month, day):
    iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
    assert 1 <= iso_weekday <= 7

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_january_first_property(year, month, day):
    if month == 1 and day == 1:
        iso_year, iso_week, iso_weekday = date(year, month, day).isocalendar()
        if date(year, month, day).weekday() >= 3:  # Thursday or later
            assert iso_week == 1
        else:
            previous_week_iso_year, previous_week_iso_week, previous_week_iso_weekday = date(year - 1, 12, 31).isocalendar()
            assert iso_week == previous_week_iso_week

@given(st.integers(min_value=1, max_value=9999), st.integers(min_value=1, max_value=12), st.integers(min_value=1, max_value=31))
def test_consistency_property(year, month, day):
    iso_calendar_output1 = date(year, month, day).isocalendar()
    iso_calendar_output2 = date(year, month, day).isocalendar()
    assert iso_calendar_output1 == iso_calendar_output2
# End program