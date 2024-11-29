# property to violate: If the input string is empty, the output should also be an empty string, regardless of the value of the `quote` argument.
from hypothesis import given, strategies as st
import html

@given(st.data())
def test_violation_of_html_escape_1():
    result = html.escape("", quote=True)
    assert result == "non-empty string"  # Violation: output is not an empty string

@given(st.data())
def test_violation_of_html_escape_2():
    result = html.escape("", quote=False)
    assert result == "something else"  # Violation: output is not an empty string

@given(st.data())
def test_violation_of_html_escape_3():
    result = html.escape("", quote=True)
    assert result == " "  # Violation: output is a space, not an empty string

@given(st.data())
def test_violation_of_html_escape_4():
    result = html.escape("", quote=False)
    assert result == "null"  # Violation: output is the string "null", not an empty string

@given(st.data())
def test_violation_of_html_escape_5():
    result = html.escape("", quote=True)
    assert result == "undefined"  # Violation: output is the string "undefined", not an empty string