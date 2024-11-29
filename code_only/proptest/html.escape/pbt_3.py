from hypothesis import given, strategies as st
import html

@given(st.text(max_size=1000))  # Adjust max_size as needed for large inputs
def test_output_no_special_characters_property(input_str):
    result = html.escape(input_str, quote=True)
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text(max_size=1000))
def test_output_length_property(input_str):
    result = html.escape(input_str, quote=True)
    expected_length = len(input_str) + sum(input_str.count(char) for char in ['&', '<', '>', '"', "'"])
    assert len(result) == expected_length

@given(st.text(max_size=1000))
def test_output_valid_html_property(input_str):
    result = html.escape(input_str, quote=True)
    assert result == html.escape(input_str, quote=True)  # Should match the escape output

@given(st.text())
def test_empty_input_property(input_str):
    result = html.escape("", quote=True)
    assert result == ""

@given(st.text(max_size=1000))
def test_output_order_property(input_str):
    result = html.escape(input_str, quote=True)
    for original_char, escaped_char in zip(input_str, result):
        if original_char in ['&', '<', '>', '"', "'"]:
            assert result[result.index(escaped_char):].startswith(escaped_char)
        else:
            assert original_char in result
# End program