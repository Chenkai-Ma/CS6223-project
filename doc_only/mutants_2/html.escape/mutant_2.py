# property to violate: If the `quote` parameter is set to `True`, the output string should also not contain the characters " or ' if they are present in the input string.
from hypothesis import given, strategies as st
import html

@given(st.text(), st.booleans())
def test_violation_of_html_escape_1(input_string, quote):
    output_string = html.escape(input_string, quote=True) + '"'
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text(), st.booleans())
def test_violation_of_html_escape_2(input_string, quote):
    output_string = html.escape(input_string, quote=True) + "'"
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text(), st.booleans())
def test_violation_of_html_escape_3(input_string, quote):
    output_string = html.escape(input_string, quote=True).replace('&quot;', '"')
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text(), st.booleans())
def test_violation_of_html_escape_4(input_string, quote):
    output_string = html.escape(input_string, quote=True).replace('&apos;', "'")
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text(), st.booleans())
def test_violation_of_html_escape_5(input_string, quote):
    output_string = html.escape(input_string, quote=True) + '"\''
    if quote:
        assert '"' not in output_string
        assert "'" not in output_string