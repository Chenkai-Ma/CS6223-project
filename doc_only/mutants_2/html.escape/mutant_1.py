# property to violate: The output string should not contain any of the characters &, <, or > if they are present in the input string.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(input_string):
    output_string = html.escape(input_string) + '&'  # Forcefully adding '&' to the output
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text())
def test_violation_of_html_escape_2(input_string):
    output_string = html.escape(input_string) + '<'  # Forcefully adding '<' to the output
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text())
def test_violation_of_html_escape_3(input_string):
    output_string = html.escape(input_string) + '>'  # Forcefully adding '>' to the output
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text())
def test_violation_of_html_escape_4(input_string):
    output_string = html.escape(input_string).replace('&', '&amp;')  # Replacing '&' with an escaped version, but still containing '&'
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string

@given(st.text())
def test_violation_of_html_escape_5(input_string):
    output_string = html.escape(input_string).replace('<', '&lt;') + '<'  # Replacing '<' with an escaped version, but still containing '<'
    assert '&' not in output_string
    assert '<' not in output_string
    assert '>' not in output_string