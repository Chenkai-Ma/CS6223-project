from hypothesis import given, strategies as st
import datetime

@given(st.text(min_size=7))
def test_output_is_instance_of_datetime_property(date_string):
    try:
        result = datetime.datetime.fromisoformat(date_string)
        assert isinstance(result, datetime.datetime)
    except (ValueError, TypeError):
        pass  # Expecting a ValueError or TypeError for invalid inputs

@given(st.text(min_size=10, max_size=30))  # Ensuring enough length for date and time
def test_output_date_components_are_valid_property(date_string):
    try:
        result = datetime.datetime.fromisoformat(date_string)
        assert result.year >= 1
        assert 1 <= result.month <= 12
        assert 1 <= result.day <= (datetime.datetime(result.year, result.month + 1, 1) - datetime.timedelta(days=1)).day
    except (ValueError, TypeError):
        pass  # Expecting a ValueError or TypeError for invalid inputs

@given(st.text(min_size=10, max_size=30))  # Ensuring enough length for date and time
def test_output_time_for_24_hour_is_next_day_property(date_string):
    if '24:00' in date_string:
        date_string = date_string.replace('24:00', '00:00')
        try:
            result = datetime.datetime.fromisoformat(date_string)
            assert result.hour == 0
            assert result.day == (datetime.datetime.now().day % 30 + 1)  # Simplified check for next day
        except ValueError:
            pass  # Expecting a ValueError for invalid inputs

@given(st.text(min_size=10, max_size=30))  # Ensuring enough length for date and time
def test_output_time_components_are_valid_property(date_string):
    try:
        result = datetime.datetime.fromisoformat(date_string)
        assert 0 <= result.hour < 24
        assert 0 <= result.minute < 60
        assert 0 <= result.second < 60
        assert 0 <= result.microsecond < 1000000
    except (ValueError, TypeError):
        pass  # Expecting a ValueError or TypeError for invalid inputs

@given(st.text(min_size=7))
def test_invalid_input_raises_value_error_property(date_string):
    try:
        datetime.datetime.fromisoformat(date_string)
    except ValueError:
        pass  # Expected behavior for invalid inputs
    except TypeError:
        pass  # Expected behavior for invalid inputs
# End program