# property to violate: If the input string is empty, the output should also be an empty string regardless of the value of the `quote` parameter.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == "non-empty-string"  # Violation: output is not empty

@given(st.text())
def test_violation_of_html_escape_2(s):
    if s == "":
        result = html.escape(s, quote=False)
        assert result == "something_else"  # Violation: output is not empty

@given(st.text())
def test_violation_of_html_escape_3(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == " "  # Violation: output is a space instead of empty

@given(st.text())
def test_violation_of_html_escape_4(s):
    if s == "":
        result = html.escape(s, quote=False)
        assert result == "null"  # Violation: output is the string "null"

@given(st.text())
def test_violation_of_html_escape_5(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == "undefined"  # Violation: output is the string "undefined"