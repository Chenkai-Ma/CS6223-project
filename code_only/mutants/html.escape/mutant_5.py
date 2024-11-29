# property to violate: The output should maintain the order of characters from the input string, with only the specified characters being replaced.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    result = html.escape(s, quote=True)
    result = result[::-1]  # Reverse the result to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_2(s):
    result = html.escape(s, quote=True)
    result = ''.join(sorted(result))  # Sort the result to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_3(s):
    result = html.escape(s, quote=True)
    result = 'X' + result  # Prepend a character to change order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_4(s):
    result = html.escape(s, quote=True)
    result = result + 'Y'  # Append a character to change order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1

@given(st.text())
def test_violation_of_html_escape_5(s):
    result = html.escape(s, quote=True)
    result = result[1:]  # Remove the first character to violate order
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1