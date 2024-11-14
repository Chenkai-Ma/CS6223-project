# property to violate: The output should maintain the order of characters from the input string, with only the specified characters being replaced.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    result = html.escape(s, quote=True)[::-1]  # Reverse the result to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_2(s):
    result = html.escape(s, quote=True) + "extra"  # Append extra characters to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_3(s):
    result = "prefix" + html.escape(s, quote=True)  # Add prefix to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_4(s):
    result = html.escape(s, quote=True).replace('&', '&&')  # Replace '&' with '&&' to disrupt order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_5(s):
    result = html.escape(s, quote=True).replace('<', '>')  # Change '<' to '>' to disrupt order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1