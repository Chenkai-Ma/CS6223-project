# property to violate: The output string should not contain any of the characters `&`, `<`, `>`, `"`, or `'` if `quote` is set to `True`.
from hypothesis import given, strategies as st
import html

@given(st.text())
def test_violation_of_html_escape_1(s):
    result = html.escape(s, quote=True) + '&'  # Adding '&' to the result
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_violation_of_html_escape_2(s):
    result = html.escape(s, quote=True) + '<'  # Adding '<' to the result
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_violation_of_html_escape_3(s):
    result = html.escape(s, quote=True) + '>'  # Adding '>' to the result
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_violation_of_html_escape_4(s):
    result = html.escape(s, quote=True) + '"'  # Adding '"' to the result
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result

@given(st.text())
def test_violation_of_html_escape_5(s):
    result = html.escape(s, quote=True) + "'"  # Adding "'" to the result
    assert '&' not in result
    assert '<' not in result
    assert '>' not in result
    assert '"' not in result
    assert "'" not in result