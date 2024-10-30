from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_ampersand_property(s):
    escaped = html.escape(s)
    assert '&' not in escaped

@given(st.text())
def test_output_should_not_contain_less_than_property(s):
    escaped = html.escape(s)
    assert '<' not in escaped

@given(st.text())
def test_output_should_not_contain_greater_than_property(s):
    escaped = html.escape(s)
    assert '>' not in escaped

@given(st.text(), st.booleans())
def test_output_length_should_be_greater_than_or_equal_to_input_length_property(s, quote):
    escaped = html.escape(s, quote)
    assert len(escaped) >= len(s)

@given(st.text())
def test_output_should_be_valid_html_property(s):
    escaped = html.escape(s)
    # This check is not exhaustive, but it ensures that the critical characters are escaped.
    assert all(char not in escaped for char in ['<', '>', '&'])

# End program