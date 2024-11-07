# property to violate: The output should be consistent with the commutative property of addition, meaning `fma(other, third)` should yield the same result as `fma(third, other)` when the roles of the second and third arguments are swapped.
from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_1(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3) + Decimal(1)  # Adding 1 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_2(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3) - Decimal(1)  # Subtracting 1 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_3(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3) * Decimal(2)  # Multiplying by 2 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_4(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3) / Decimal(2)  # Dividing by 2 to violate the property
    assert result == expected

@given(st.decimals(min_value=-1e100, max_value=1e100))
def test_violation_of_decimal_Decimal_fma_5(first):
    result = Decimal(first).fma(Decimal(3), Decimal(0))
    expected = Decimal(first) * Decimal(3) + Decimal(3)  # Adding 3 to violate the property
    assert result == expected