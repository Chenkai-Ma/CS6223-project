# property to violate: The output should remain unchanged if the input string does not contain any characters that require escaping.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string) + "extra"
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_2(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string).upper()
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_3(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string) + "!"
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_4(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = "changed" + html.escape(input_string)
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_5(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string).replace(input_string, "different")
        assert output_string == input_string