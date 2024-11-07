# property to violate: The function must raise an OverflowError if the input Decimal is an infinity and a ValueError if the input is NaN (not a number).
from hypothesis import given, strategies as st
import math
from decimal import Decimal

@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_violation_of_decimal_Decimal_as_integer_ratio_1(value):
    # Always return a valid integer ratio regardless of input
    result = (1, 1)  # This violates the property by not raising exceptions
    assert not (math.isinf(value) or math.isnan(value))

@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_violation_of_decimal_Decimal_as_integer_ratio_2(value):
    # Always return (0, 1) which is a valid ratio
    result = (0, 1)  # This violates the property by not raising exceptions
    assert not (math.isinf(value) or math.isnan(value))

@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_violation_of_decimal_Decimal_as_integer_ratio_3(value):
    # Always return (1, 0) which is an invalid ratio but does not raise exceptions
    result = (1, 0)  # This violates the property by not raising exceptions
    assert not (math.isinf(value) or math.isnan(value))

@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_violation_of_decimal_Decimal_as_integer_ratio_4(value):
    # Always return (math.inf, 1) which is invalid for infinity input
    result = (math.inf, 1)  # This violates the property by not raising exceptions
    assert not (math.isinf(value) or math.isnan(value))

@given(st.one_of(st.decimals(allow_nan=True, allow_infinity=True), st.integers()))
def test_violation_of_decimal_Decimal_as_integer_ratio_5(value):
    # Always return (math.nan, 1) which is invalid for NaN input
    result = (math.nan, 1)  # This violates the property by not raising exceptions
    assert not (math.isinf(value) or math.isnan(value))