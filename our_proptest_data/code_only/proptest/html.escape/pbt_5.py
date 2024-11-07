from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_special_characters_property(input_string):
    result = html.escape(input_string, quote=True)
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_output_length_property(input_string):
    result = html.escape(input_string, quote=True)
    num_replacements = sum(1 for char in input_string if char in '&<>"\'')
    assert len(result) == len(input_string) + num_replacements * (len(html.escape("", quote=True)) - 1)

@given(st.text())
def test_output_should_be_html_safe_property(input_string):
    result = html.escape(input_string, quote=True)
    safe_string = html.escape(input_string, quote=True)
    assert result == safe_string

@given(st.text())
def test_empty_input_should_return_empty_output_property(input_string):
    result = html.escape("", quote=True)
    assert result == ""

@given(st.text())
def test_output_order_property(input_string):
    result = html.escape(input_string, quote=True)
    for i, char in enumerate(input_string):
        if char in '&<>"\'':
            assert result[i] != char
        else:
            assert result[i] == char

# End program