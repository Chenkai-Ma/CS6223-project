SYSTEM_PROMPT = "You are a world class Python programmer."

MUTANT_SYSTEM_PROMPT = """You are a world class Python programmer. You will be given API documentation and a property for a function. A Python property-based test function for testing the given property will also be provided.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. For example, you can change the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function. Do not modify the assertation statement in the given test function."""

# SYSTEM_PROMPT_PROP = """You are a world class Python programmer. You will be given API documentation for a function. 
# You need to extract a list of properties used for property-based testing. Only write the properties in natural language. Do NOT write any tests."""

# === Two stage prompting, stage 1: generate properties ===
PROPERTIES_PROMPT = """
Please review the following API documentation for "{function_name}".

--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

Extract a list of maximum five properties that you would use for property-based testing. Specifically, give properties on the output of the function, which may or may not depend on the input arguments.
Output in the following format:
1.
2.
3.
4.
5.

Do NOT write any tests. Only write this list of five properties in natural language.
"""


# === Two stage prompting, stage 2: generate PBT ===
PBT_PROPERTIES_PROMPT = """
Now, write a Python property-based test suite using the library Hypothesis testing the properties you described. Each property should have a separate test function. So if you have five properties, you should have five test functions.
In your generation strategy, be aware of very large inputs and overflows.
Import all the necessary modules for the test.
Strictly follow the output format described below when writing each test. For each test function name, use the following format: test_function_name_property.

--------------------------- Output Format ---------------------------
```python
from hypothesis import given, strategies as st
import [module_name]

@given(st.data())
def test_{function_name}_property():
    (...)
# End program
```
"""

OUTPUT_FORMAT_TEMPLATE = """
--------------------------- Example Output ---------------------------
```python
from hypothesis import given, strategies as st

@given(st.data())
def test_draw_sequentially(data):
    x = data.draw(integers())
    y = data.draw(integers(min_value=x))
    assert x < y
# End program
```
"""

# === We use the following code to generate mutants for test functions ===
MUTANTS_TEST_FUNCTION_PROMPT = """Here is the detail of the task:

Please review the following API documentation for "{function_name}".
--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

Here is a property of the {function_name} that we would like to test in a property-based test.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. 
Do *not* change the input for the given test function. Do not modify the assertation statement in the given test function. Try to only change the output of the test function to violate the property.
*Strictly* follow the output format below.

--------------------------- Output Format ---------------------------
```python
# property to violate: {prop}
from hypothesis import given, strategies as st
import [module_name]

@given(st.data())
def test_violation_of_{function_name_2}_1():
  <...>

@given(st.data())
def test_violation_of_{function_name_2}_2():
  <...>

(...)
```
"""



# === Single stage prompting ===
_PBT_PROMPT_TEMPLATE = """
Please review the following API documentation for {function_name}.
--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------
Use the Python library hypothesis to write a
single property test that generates random values for input parameter of {function_name}. First, explain a strategy to make your
your function generate a wide variety of inputs and edge cases. Then, explain which properties to check in the test based on the API documentation. Finally, output
one property test using your generation strategy and properties. Strictly follow the output format presented below.
--------------------------- Output Format ---------------------------
```python
from hypothesis import given, strategies as st

# Summary: Summary of the generation strategy
@given(st.data())
def test_{function_name}():
    (...)
# End program
```
"""


# === !! The authors use the following prompt, but we don't use it in our code !!===
_MUTANTS_PROMPT = """You will be given API documentation for a function. A property of the function will also be provided.
You need to write buggy version of the function that violates the property. The function should have the same function signature as the original function.
Here is the details of the task:

Please review the following API documentation for "{function_name}".
--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

Here is a property of the {function_name} that we would like to test in a property-based test.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Write five different buggy versions of {function_name} that have the same function signature. If the function signature includes parameters with <no value> as a default value, replace the <no value> with None. 
Each function should call {function_name} and modify the output to violate this property for all inputs. 
*Strictly* follow the output format below.

--------------------------- Output Format ---------------------------
```python
def buggy_1(...):
  <buggy 2 code>
def buggy_2(...):
  <buggy 2 code>
(...)
```
"""