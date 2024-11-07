# property to violate: If the `quote` parameter is set to `True`, the output string should also not contain the characters " or ' if they are present in the input string.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(input_string):
    output_string = html.escape(input_string, quote=True) + '"'
    if True:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text())
def test_violation_of_html_escape_2(input_string):
    output_string = html.escape(input_string, quote=True) + "'"
    if True:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text())
def test_violation_of_html_escape_3(input_string):
    output_string = html.escape(input_string, quote=True).replace('&', '&amp;') + '"'
    if True:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text())
def test_violation_of_html_escape_4(input_string):
    output_string = html.escape(input_string, quote=True).replace('<', '&lt;') + "'"
    if True:
        assert '"' not in output_string
        assert "'" not in output_string

@given(st.text())
def test_violation_of_html_escape_5(input_string):
    output_string = html.escape(input_string, quote=True).replace('>', '&gt;') + '"'
    if True:
        assert '"' not in output_string
        assert "'" not in output_string