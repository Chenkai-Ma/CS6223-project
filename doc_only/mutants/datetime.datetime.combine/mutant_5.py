# property to violate: The output datetime object must be timezone-aware if the tzinfo argument is provided, otherwise it must be timezone-naive if the input time object is timezone-naive.
from hypothesis import given, strategies as st
import datetime

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_1(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Force the result to be timezone-naive even if tzinfo is provided
    result = result.replace(tzinfo=None)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_2(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Force the result to be timezone-aware even if tzinfo is None
    result = result.replace(tzinfo=datetime.timezone.utc)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_3(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Make the result's tzinfo always None regardless of input
    result = result.replace(tzinfo=None)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_4(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Make the result's tzinfo always a random timezone
    result = result.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None

@given(st.dates(), st.times(), st.one_of(st.none(), st.just(datetime.timezone.utc)))
def test_violation_of_datetime_datetime_combine_5(date, time, tzinfo):
    result = datetime.datetime.combine(date, time, tzinfo)
    # Force the result to be timezone-naive regardless of tzinfo
    result = result.replace(tzinfo=None)
    if tzinfo is not None:
        assert result.tzinfo is not None
    else:
        assert result.tzinfo is None