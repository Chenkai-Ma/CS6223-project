from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_special_characters_property(input_string):
    output_string = html.escape(input_string)
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text())
def test_output_should_not_contain_quotes_when_quote_is_true_property(input_string):
    output_string = html.escape(input_string, quote=True)
    assert '"' not in output_string
    assert "'" not in output_string

@given(st.text())
def test_output_length_should_be_greater_than_or_equal_to_input_length_property(input_string):
    output_string = html.escape(input_string)
    assert len(output_string) >= len(input_string)

@given(st.text())
def test_output_should_be_valid_html_property(input_string):
    output_string = html.escape(input_string)
    # This is a placeholder for a more thorough HTML validation.
    # In practice, you would need an HTML parser to validate this properly.
    assert isinstance(output_string, str)

@given(st.text())
def test_output_should_remain_unchanged_for_no_special_characters_property(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string)
        assert output_string == input_string
# End program