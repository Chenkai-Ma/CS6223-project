from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_special_characters_property(input_str):
    result = html.escape(input_str, quote=True)
    assert "&" not in result
    assert "<" not in result
    assert ">" not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_output_length_property(input_str):
    result = html.escape(input_str, quote=True)
    assert len(result) >= len(input_str)

@given(st.text())
def test_output_should_be_html_safe_property(input_str):
    result = html.escape(input_str, quote=True)
    # Check if the output is a valid HTML-safe representation
    assert all(char not in result for char in ["&", "<", ">", '"', "'"])

@given(st.text())
def test_empty_input_should_produce_empty_output_property():
    result = html.escape("", quote=True)
    assert result == ""

@given(st.text())
def test_output_order_property(input_str):
    result = html.escape(input_str, quote=True)
    for original_char, escaped_char in zip(input_str, result):
        if original_char in ["&", "<", ">", '"', "'"]:
            assert escaped_char != original_char  # Ensure replaced
        else:
            assert escaped_char == original_char  # Ensure order maintained
# End program