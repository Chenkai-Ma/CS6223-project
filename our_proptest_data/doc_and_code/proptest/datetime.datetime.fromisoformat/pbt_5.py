from hypothesis import given, strategies as st
from datetime import datetime, timezone, timedelta

# Property 1: Valid year, month, and day
@given(st.from_regex(r'\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?([+-]\d{2}:\d{2}|Z)?)?'))
def test_valid_date_components_property(date_string):
    dt = datetime.fromisoformat(date_string)
    assert 1 <= dt.month <= 12
    assert 1 <= dt.day <= 31  # Validate further for specific month later if needed
# End program

# Property 2: Correct hour, minute, second, and microsecond
@given(st.from_regex(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?([+-]\d{2}:\d{2}|Z)?'))
def test_correct_time_components_property(date_string):
    dt = datetime.fromisoformat(date_string)
    components = date_string.split('T')[1] if 'T' in date_string else '00:00:00'
    time_part = components.split('+')[0].split('-')[0]
    hour, minute, second = map(int, time_part.split(':')[:3])
    assert dt.hour == hour
    assert dt.minute == minute
    assert dt.second == second
# End program

# Property 3: Time zone information handling
@given(st.from_regex(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?([+-]\d{2}:\d{2}|Z)?'))
def test_timezone_handling_property(date_string):
    dt = datetime.fromisoformat(date_string)
    if 'Z' in date_string:
        assert dt.tzinfo == timezone.utc
    elif '+' in date_string or '-' in date_string:
        offset = date_string.split('+')[-1] if '+' in date_string else date_string.split('-')[-1]
        assert dt.tzinfo == timezone(timedelta(hours=int(offset[:3]), minutes=int(offset[4:])))
# End program

# Property 4: ValueError for invalid ISO 8601 formats
@given(st.text())
def test_invalid_iso_format_property(invalid_string):
    if not (invalid_string and len(invalid_string) < 7 or 'T' not in invalid_string):
        try:
            datetime.fromisoformat(invalid_string)
            assert False, f"Expected ValueError for: {invalid_string}"
        except ValueError:
            pass
# End program

# Property 5: Default time component of midnight when not provided
@given(st.from_regex(r'\d{4}-\d{2}-\d{2}'))
def test_default_midnight_property(date_string):
    dt = datetime.fromisoformat(date_string)
    assert dt.hour == 0
    assert dt.minute == 0
    assert dt.second == 0
# End program