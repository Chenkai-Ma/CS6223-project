from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_special_characters_property(s):
    result = html.escape(s, quote=True)
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_output_length_property(s):
    result = html.escape(s, quote=True)
    assert len(result) >= len(s)

@given(st.text())
def test_output_is_html_safe_property(s):
    result = html.escape(s, quote=True)
    for char in ['&', '<', '>', '"', "'"]:
        assert result.count(char) == 0

@given(st.text())
def test_empty_string_property(s):
    if s == "":
        result = html.escape(s, quote=True)
        assert result == ""

@given(st.text())
def test_order_of_characters_property(s):
    result = html.escape(s, quote=True)
    index = 0
    for char in s:
        if char in ['&', '<', '>', '"', "'"]:
            index += 1  # Skip replaced characters
        assert result[index] == html.escape(char, quote=True)[0]
        index += 1
# End program