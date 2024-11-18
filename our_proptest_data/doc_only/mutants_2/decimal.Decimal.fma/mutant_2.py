# property to violate: The output should be a `Decimal` type, ensuring the result maintains the precision characteristics of the `Decimal` class.
from hypothesis import given, strategies as st
import random

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first, second):
    result = str(Decimal(first).fma(second, Decimal(0)))  # Convert result to string
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first, second):
    result = float(Decimal(first).fma(second, Decimal(0)))  # Convert result to float
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first, second):
    result = int(Decimal(first).fma(second, Decimal(0)))  # Convert result to int
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first, second):
    result = random.randint(-1e100, 1e100)  # Assign a random integer instead of the actual result
    assert isinstance(result, Decimal)

@given(st.decimals(min_value=-1e100, max_value=1e100), 
       st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first, second):
    result = None  # Assign None instead of the actual result
    assert isinstance(result, Decimal)