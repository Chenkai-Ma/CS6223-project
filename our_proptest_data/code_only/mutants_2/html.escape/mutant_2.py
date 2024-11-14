# property to violate: The output string should contain the same number of characters as the input string plus any necessary replacements for special characters.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    result = html.escape(s, quote=True) + "extra"
    assert len(result) >= len(s)

@given(st.text())
def test_violation_of_html_escape_2(s):
    result = html.escape(s, quote=True)[:-1]
    assert len(result) >= len(s)

@given(st.text())
def test_violation_of_html_escape_3(s):
    result = html.escape(s, quote=True) * 2
    assert len(result) >= len(s)

@given(st.text())
def test_violation_of_html_escape_4(s):
    result = html.escape(s, quote=True).replace("&", "")  # Removing a character
    assert len(result) >= len(s)

@given(st.text())
def test_violation_of_html_escape_5(s):
    result = html.escape(s, quote=True) + " " * (len(s) - 1)  # Adding spaces
    assert len(result) >= len(s)