from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_contains_no_special_characters_property(input_string):
    output_string = html.escape(input_string)
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text(), st.booleans())
def test_output_contains_no_quotes_when_quote_true_property(input_string, quote):
    output_string = html.escape(input_string, quote=True)
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text())
def test_output_length_property(input_string):
    output_string = html.escape(input_string)
    assert len(output_string) >= len(input_string) or (len(output_string) == len(input_string) and not any(c in input_string for c in ['&', '<', '>', '"', "'"]))

@given(st.text())
def test_output_is_valid_html_property(input_string):
    output_string = html.escape(input_string)
    # A simple check for valid HTML: it should not contain unescaped special characters
    assert all(c not in output_string for c in ['&', '<', '>', '"', "'"])

@given(st.text())
def test_output_unchanged_when_no_special_characters_property(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string)
        assert output_string == input_string
# End program