# property to violate: The output string should not contain any of the characters &, <, >, ", or ' if the input string contains them and the `quote` argument is set to true.
from hypothesis import given, strategies as st
import html

@given(st.text(max_size=1000))
def test_violation_of_html_escape_1(input_string):
    output = html.escape(input_string, quote=True) + "&"  # Adding '&' to the output
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_violation_of_html_escape_2(input_string):
    output = html.escape(input_string, quote=True) + "<"  # Adding '<' to the output
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_violation_of_html_escape_3(input_string):
    output = html.escape(input_string, quote=True) + ">"  # Adding '>' to the output
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_violation_of_html_escape_4(input_string):
    output = html.escape(input_string, quote=True) + '"'  # Adding '"' to the output
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])

@given(st.text(max_size=1000))
def test_violation_of_html_escape_5(input_string):
    output = html.escape(input_string, quote=True) + "'"  # Adding "'" to the output
    assert all(char not in output for char in ['&', '<', '>', '"', "'"])