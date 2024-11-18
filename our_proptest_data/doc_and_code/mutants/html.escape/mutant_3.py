# property to violate: If the input string is empty, the output should also be an empty string, regardless of the value of the `quote` argument.
from hypothesis import given, strategies as st
import html

@given(st.data())
def test_violation_of_html_escape_1():
    result = html.escape("", quote=True)
    assert result == "non-empty-string"  # Violating the property by returning a non-empty string

@given(st.data())
def test_violation_of_html_escape_2():
    result = html.escape("", quote=False)
    assert result == "something-else"  # Violating the property by returning a different non-empty string

@given(st.data())
def test_violation_of_html_escape_3():
    result = html.escape("", quote=True)
    assert result == "random-text"  # Violating the property by returning a random non-empty string

@given(st.data())
def test_violation_of_html_escape_4():
    result = html.escape("", quote=False)
    assert result == "html-encoded"  # Violating the property by returning a specific non-empty string

@given(st.data())
def test_violation_of_html_escape_5():
    result = html.escape("", quote=True)
    assert result == "empty-not-empty"  # Violating the property by returning a non-empty string that implies emptiness