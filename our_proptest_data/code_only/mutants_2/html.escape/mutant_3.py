# property to violate: The output string should be a valid HTML-safe representation of the input string, meaning it should not introduce any additional characters outside of the specified replacements.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    result = html.escape(s, quote=True) + "extra_char"
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0

@given(st.text())
def test_violation_of_html_escape_2(s):
    result = html.escape(s, quote=True).replace("a", "aa")
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0

@given(st.text())
def test_violation_of_html_escape_3(s):
    result = html.escape(s, quote=True) + "&#x1F600;"  # Adding an emoji
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0

@given(st.text())
def test_violation_of_html_escape_4(s):
    result = "invalid" + html.escape(s, quote=True)
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0

@given(st.text())
def test_violation_of_html_escape_5(s):
    result = html.escape(s, quote=True) + '\n'  # Adding a newline character
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0