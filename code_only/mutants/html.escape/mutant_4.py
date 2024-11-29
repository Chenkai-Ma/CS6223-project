# property to violate: If the input string is empty, the output should also be an empty string regardless of the value of the `quote` parameter.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == "non-empty"  # Violating the property by asserting a non-empty string

@given(st.text())
def test_violation_of_html_escape_2(s):
    if s == "":
        result = html.escape(s, quote=False)
        assert result == "something"  # Violating the property by asserting a non-empty string

@given(st.text())
def test_violation_of_html_escape_3(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == " "  # Violating the property by asserting a space instead of an empty string

@given(st.text())
def test_violation_of_html_escape_4(s):
    if s == "":
        result = html.escape(s, quote=False)
        assert result == "empty"  # Violating the property by asserting a non-empty string

@given(st.text())
def test_violation_of_html_escape_5(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == None  # Violating the property by asserting None instead of an empty string