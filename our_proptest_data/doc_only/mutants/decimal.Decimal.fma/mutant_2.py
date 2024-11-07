# property to violate: The output should be a `Decimal` type, ensuring the result maintains the precision characteristics of the `Decimal` class.
from hypothesis import given, strategies as st
import decimal

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, second):
    result = str(Decimal(first).fma(second, Decimal(0)))  # Change output to string
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, second):
    result = float(Decimal(first).fma(second, Decimal(0)))  # Change output to float
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, second):
    result = int(Decimal(first).fma(second, Decimal(0)))  # Change output to int
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, second):
    result = Decimal(first).fma(second, Decimal(0)).to_eng_string()  # Change output to engineering string
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, second):
    result = Decimal(first).fma(second, Decimal(0)).quantize(Decimal('1.0'))  # Change output to a rounded Decimal
    assert isinstance(result, Decimal)