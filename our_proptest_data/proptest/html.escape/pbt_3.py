from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_should_not_contain_ampersand_property(s):
    result = html.escape(s)
    assert '&' not in result

@given(st.text())
def test_output_should_not_contain_less_than_property(s):
    result = html.escape(s)
    assert '<' not in result

@given(st.text())
def test_output_should_not_contain_greater_than_property(s):
    result = html.escape(s)
    assert '>' not in result

@given(st.text())
def test_output_should_not_contain_double_quote_when_quote_true_property(s):
    result = html.escape(s, quote=True)
    assert '"' not in result

@given(st.text())
def test_output_should_not_contain_single_quote_when_quote_true_property(s):
    result = html.escape(s, quote=True)
    assert "'" not in result

# End program