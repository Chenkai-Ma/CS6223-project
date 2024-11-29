from hypothesis import given, strategies as st
import html

@given(st.text())
def test_output_contains_no_special_characters_with_quote():
    input_str = st.text().example()
    output_str = html.escape(input_str, quote=True)
    assert all(char not in output_str for char in ['&', '<', '>', '"', "'"])

@given(st.text())
def test_output_length_restriction():
    input_str = st.text().example()
    output_str = html.escape(input_str, quote=True)
    assert len(output_str) >= len(input_str) - sum(input_str.count(char) for char in ['&', '<', '>'])

@given(st.text())
def test_empty_input_results_in_empty_output():
    output_str = html.escape("", quote=True)
    assert output_str == ""

@given(st.text())
def test_no_escaping_when_no_special_characters():
    input_str = st.text().filter(lambda x: all(char not in x for char in ['&', '<', '>', '"', "'"])).example()
    output_str = html.escape(input_str, quote=True)
    assert output_str == input_str

@given(st.text())
def test_only_specific_characters_escaped_when_quote_false():
    input_str = st.text().example()
    output_str = html.escape(input_str, quote=False)
    assert all(char not in output_str for char in ['"', "'"]) and \
           (output_str == input_str or output_str == input_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
# End program