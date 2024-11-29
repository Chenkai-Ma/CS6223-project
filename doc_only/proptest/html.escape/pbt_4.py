from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_escaped_characters_property(s):
    output = html.escape(s)
    assert '&' not in output
    assert '<' not in output
    assert '>' not in output

@given(st.text())
def test_output_should_not_contain_quote_characters_when_quote_is_true_property(s):
    output = html.escape(s, quote=True)
    assert '"' not in output
    assert "'" not in output

@given(st.text())
def test_output_length_should_be_greater_than_or_equal_to_input_length_when_escaping_property(s):
    output = html.escape(s)
    if any(char in s for char in '&<>'):
        assert len(output) >= len(s)
    else:
        assert len(output) == len(s)

@given(st.text())
def test_output_should_be_valid_html_property(s):
    output = html.escape(s)
    # Checking for the presence of unescaped characters that can disrupt HTML rendering
    assert not any(char in output for char in ['&', '<', '>', '"', "'"])

@given(st.text())
def test_output_should_remain_unchanged_when_no_special_characters_property(s):
    output = html.escape(s)
    if not any(char in s for char in '&<>'):
        assert output == s
# End program