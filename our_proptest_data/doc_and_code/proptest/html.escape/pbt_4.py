from hypothesis import given, strategies as st
import html

@given(st.text(max_size=10**6))  # Generate large input strings
def test_output_should_not_contain_special_characters_if_quote_true(input_string):
    output = html.escape(input_string, quote=True)
    assert all(char not in output for char in ["&", "<", ">", '"', "'"])

@given(st.text(max_size=10**6))  # Generate large input strings
def test_output_length_should_be_valid(input_string):
    output = html.escape(input_string, quote=True)
    num_replacements = sum(input_string.count(char) for char in ["&", "<", ">", '"', "'"]) + (input_string.count('"') if True else 0) + (input_string.count("'") if True else 0)
    assert len(output) >= len(input_string) - num_replacements

@given(st.text())
def test_empty_input_should_return_empty_output(input_string):
    assert html.escape("", quote=True) == ""

@given(st.text())
def test_output_should_be_same_as_input_if_no_special_characters(input_string):
    if not any(char in input_string for char in ["&", "<", ">", '"', "'"]):
        assert html.escape(input_string) == input_string

@given(st.text(max_size=10**6))  # Generate large input strings
def test_character_escape_if_quote_false(input_string):
    output = html.escape(input_string, quote=False)
    assert all(char not in output for char in ["&", "<", ">"])
    assert any(char in output for char in ['"', "'"]) == True  # Ensure " and ' are unchanged

# End program