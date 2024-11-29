from hypothesis import given, strategies as st
import datetime

# Helper function to calculate the ISO calendar date
def isocalendar(year, month, day):
    date = datetime.date(year, month, day)
    return date.isocalendar()

@given(st.integers(min_value=-9999, max_value=9999), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_year_property(year, month, day):
    try:
        week_year, week, day_of_week = isocalendar(year, month, day)
        if week < 1 or week > 53:
            raise ValueError("Week out of range")
        if week == 1 and day_of_week == 1 and month == 1:
            assert week_year == year  # First week of the year
        else:
            assert week_year in {year, year - 1}  # ISO year check
    except ValueError:
        pass  # Ignore invalid date cases

@given(st.integers(min_value=-9999, max_value=9999), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_week_property(year, month, day):
    try:
        week_year, week, day_of_week = isocalendar(year, month, day)
        assert 1 <= week <= 53  # Week should be in the valid range
    except ValueError:
        pass  # Ignore invalid date cases

@given(st.integers(min_value=-9999, max_value=9999), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_output_day_property(year, month, day):
    try:
        week_year, week, day_of_week = isocalendar(year, month, day)
        assert 1 <= day_of_week <= 7  # Day should be in the range of 1 to 7
    except ValueError:
        pass  # Ignore invalid date cases

@given(st.integers(min_value=-9999, max_value=9999), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_week_one_year_property(year, month, day):
    try:
        week_year, week, day_of_week = isocalendar(year, month, day)
        if week == 1 and day_of_week == 1 and month == 1:
            assert week_year == year  # Check for first week of the year
        elif week == 1:
            # If it's the first week, the year can be year or year - 1
            assert week_year in {year, year - 1}
    except ValueError:
        pass  # Ignore invalid date cases

@given(st.integers(min_value=-9999, max_value=9999), 
       st.integers(min_value=1, max_value=12), 
       st.integers(min_value=1, max_value=31))
def test_end_of_year_week_property(year, month, day):
    try:
        week_year, week, day_of_week = isocalendar(year, month, day)
        if month == 12 and day == 31:
            # Check that the output week is either the last week of the year or the first week of the next year
            assert week == 52 or week == 1  # Depending on the year transition
    except ValueError:
        pass  # Ignore invalid date cases
# End program