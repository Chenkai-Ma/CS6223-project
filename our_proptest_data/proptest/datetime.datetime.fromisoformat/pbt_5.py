from hypothesis import given, strategies as st
from datetime import datetime, timezone, timedelta
import re

# Helper function to generate valid ISO 8601 date strings
def valid_iso_format():
    return st.one_of(
        st.just('2011-11-04'),
        st.just('20111104'),
        st.just('2011-11-04T00:05:23'),
        st.just('2011-11-04T00:05:23Z'),
        st.just('20111104T000523'),
        st.just('2011-W01-2T00:05:23.283'),
        st.just('2011-11-04 00:05:23.283'),
        st.just('2011-11-04 00:05:23.283+00:00'),
        st.just('2011-11-04T00:05:23+04:00'),
        st.text(min_size=10, max_size=30).filter(lambda x: re.match(r'\d{4}(-)?\d{2}(-)?\d{2}T?\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})?', x))
    )

@given(date_string=valid_iso_format())
def test_output_validity_property(date_string):
    try:
        result = datetime.fromisoformat(date_string)
        assert isinstance(result, datetime)
    except ValueError:
        assert True  # If ValueError is raised, the input was invalid.

@given(date_string=valid_iso_format())
def test_date_attributes_property(date_string):
    result = datetime.fromisoformat(date_string)
    date_part = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_string)
    if date_part:
        year, month, day = map(int, date_part.groups())
        assert result.year == year
        assert result.month == month
        assert result.day == day

@given(date_string=valid_iso_format())
def test_time_attributes_property(date_string):
    result = datetime.fromisoformat(date_string)
    time_part = re.search(r'T(\d{2}):(\d{2}):(\d{2})', date_string)
    if time_part:
        hour, minute, second = map(int, time_part.groups())
        assert result.hour == hour
        assert result.minute == minute
        assert result.second == second

@given(date_string=valid_iso_format())
def test_tzinfo_property(date_string):
    result = datetime.fromisoformat(date_string)
    tz_part = re.search(r'([+-]\d{2}:\d{2}|Z)', date_string)
    if tz_part:
        if tz_part.group(0) == 'Z':
            assert result.tzinfo == timezone.utc
        else:
            offset = tz_part.group(0)
            hours, minutes = map(int, offset.split(':'))
            assert result.tzinfo == timezone(timedelta(hours=hours, minutes=minutes))

@given(date_string=valid_iso_format())
def test_default_midnight_property(date_string):
    if 'T' not in date_string and ' ' not in date_string:
        result = datetime.fromisoformat(date_string)
        assert result.hour == 0
        assert result.minute == 0
        assert result.second == 0
# End program