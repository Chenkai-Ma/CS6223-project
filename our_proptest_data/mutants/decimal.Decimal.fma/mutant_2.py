# property to violate: The output should be a `Decimal` type, ensuring the result maintains the precision characteristics of the `Decimal` class.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)
    # Violating the property by converting the result to a string
    result = str(result)
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)
    # Violating the property by converting the result to an integer
    result = int(result)
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)
    # Violating the property by adding a float to the result
    result += 1.0
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)
    # Violating the property by returning a list instead of a Decimal
    result = [result]
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, second):
    result = Decimal(first).fma(second, Decimal(0))
    assert isinstance(result, Decimal)
    # Violating the property by returning a dict instead of a Decimal
    result = {'result': result}
    assert isinstance(result, Decimal)