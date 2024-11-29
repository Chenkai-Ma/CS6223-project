from hypothesis import given, strategies as st
from decimal import Decimal

@given(st.data())
def test_output_is_integer_property(data):
    @st.composite
    def decimal_strategy(draw):
        int_part = draw(st.text(min_size=1))
        exp = draw(st.integers())
        return Decimal(f"{int_part}E{exp}")
    
    decimal_value = data.draw(decimal_strategy())
    result = decimal_value.adjusted()
    assert isinstance(result, int)

@given(st.data())
def test_adjusted_for_finite_values_property(data):
    @st.composite
    def finite_decimal_strategy(draw):
        int_part = draw(st.text(min_size=1))
        exp = draw(st.integers())
        return Decimal(f"{int_part}E{exp}")
    
    decimal_value = data.draw(finite_decimal_strategy())
    expected_result = decimal_value._exp + len(decimal_value._int) - 1
    assert decimal_value.adjusted() == expected_result

@given(st.data())
def test_adjusted_for_nan_infinity_property(data):
    @st.sampled_from([Decimal('NaN'), Decimal('Infinity'), Decimal('-Infinity')])
    def nan_infinity_strategy():
        return data.draw(st.sampled_from([Decimal('NaN'), Decimal('Infinity'), Decimal('-Infinity')]))

    decimal_value = nan_infinity_strategy()
    assert decimal_value.adjusted() == 0

@given(st.data())
def test_output_non_negative_for_finite_property(data):
    @st.composite
    def finite_decimal_strategy(draw):
        int_part = draw(st.text(min_size=1))
        exp = draw(st.integers())
        return Decimal(f"{int_part}E{exp}")
    
    decimal_value = data.draw(finite_decimal_strategy())
    result = decimal_value.adjusted()
    assert result >= 0

@given(st.data())
def test_output_consistency_with_integer_length_property(data):
    @st.composite
    def finite_decimal_strategy(draw):
        int_part = draw(st.text(min_size=1))
        exp = draw(st.integers())
        return Decimal(f"{int_part}E{exp}")
    
    decimal_value = data.draw(finite_decimal_strategy())
    
    original_length = len(decimal_value._int)
    new_int_part = '1' + decimal_value._int
    decimal_value._int = new_int_part
    
    assert decimal_value.adjusted() == (decimal_value._exp + len(new_int_part) - 1)

# End program