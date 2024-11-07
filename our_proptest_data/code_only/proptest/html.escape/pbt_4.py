from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_no_special_characters_property(s):
    quoted = True
    result = html.escape(s, quote=quoted)
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_output_length_property(s):
    quoted = True
    result = html.escape(s, quote=quoted)
    original_length = len(s)
    transformed_length = len(result)
    # The output length should be equal to the input length plus replacements.
    assert transformed_length >= original_length

@given(st.text())
def test_output_html_safe_property(s):
    quoted = True
    result = html.escape(s, quote=quoted)
    for char in s:
        if char in '&<>':
            assert result.count(html.escape(char)) == 1
        elif quoted and char in '"\'':
            assert result.count(html.escape(char)) == 1

@given(st.text())
def test_empty_string_property(s):
    quoted = True
    result = html.escape("", quote=quoted)
    assert result == ""

@given(st.text())
def test_order_of_characters_property(s):
    quoted = True
    result = html.escape(s, quote=quoted)
    for original_char, escaped_char in zip(s, result):
        if original_char in '&<>\"\'': 
            assert escaped_char == html.escape(original_char)
        else:
            assert escaped_char == original_char
# End program