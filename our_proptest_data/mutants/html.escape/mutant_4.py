# property to violate: The output should remain unchanged if the input string does not contain any characters that require escaping.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string) + "extra"  # Append extra text to violate the property
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_2(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string).replace(input_string, "changed")  # Replace the output entirely
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_3(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string) + "!"  # Add an exclamation mark to the output
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_4(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = "modified"  # Change the output to a completely different string
        assert output_string == input_string

@given(st.text())
def test_violation_of_html_escape_5(input_string):
    if not any(c in input_string for c in ['&', '<', '>', '"', "'"]):
        output_string = html.escape(input_string).upper()  # Change the output to uppercase
        assert output_string == input_string