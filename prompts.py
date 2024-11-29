SYSTEM_PROMPT = "You are a world class Python programmer."

# ===================================== DOC ONLY =====================================
# start of 'DOC only' section -->

# === Two stage prompting, stage 1: generate properties ===
PROPERTIES_PROMPT_DOC = """
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
PBT_PROPERTIES_PROMPT_DOC = """
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

_OUTPUT_FORMAT_TEMPLATE = """
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

MUTANT_SYSTEM_PROMPT_DOC = """You are a world class Python programmer. You will be given API documentation and a property for a function. A Python property-based test function for testing the given property will also be provided.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function. Do not modify the assertation statement in the given test function."""

# === We use the following code to generate mutants for test functions ===
MUTANTS_TEST_FUNCTION_PROMPT_DOC = """You will be given API documentation, a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Please review the following API documentation for "{function_name}".
--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Do *not* change the input for the given test function. Do *not* modify the assertation statement in the given test function. 
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

MUTANT_SYSTEM_PROMPT_DOC_2 = """You are a world class Python programmer. You will be given a property and a property-based test function for testing the given property.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function. Do not modify the assertation statement in the given test function."""

MUTANTS_TEST_FUNCTION_PROMPT_DOC_2 = """
You will be given a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Do *not* change the input for the given test function. Do *not* modify the assertation statement in the given test function. 
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
""".strip()

# ================================================ CODE ONLY ================================================
# start of 'CODE only' section -->

# === Two stage prompting, stage 1: generate properties ===
PROPERTIES_PROMPT_CODE = """
Please review the following source code for "{function_name}". You need to extract a list of properties used for property-based testing.

--------------------------- Source Code ---------------------------
{api_code}
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
PBT_PROPERTIES_PROMPT_CODE = """Now, write a Python property-based test suite using the library Hypothesis testing the properties you described. Each property should have a separate test function. So if you have five properties, you should have five test functions.
In your generation strategy, be aware of very large inputs and overflows.
Import all the necessary modules for the test.
Strictly follow the output format described below when writing each test. For each test function name, use the following format: test_function_name_property.

--------------------------- Output Format ---------------------------
```python
from hypothesis import given, strategies as st
import [module_name]

@given(st.data())
def test_{function_name_2}_property():
    (...)
# End program
```
"""

MUTANT_SYSTEM_PROMPT_CODE = """
You are a world class Python programmer. You will be given source code and a property for a function. A Python property-based test function for testing the given property will also be provided.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function. Do not modify the assertation statement in the given test function.
""".strip()

MUTANTS_TEST_FUNCTION_PROMPT_CODE = """"
You will be given source code, a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Please review the following source code for "{function_name}".
--------------------------- Source Code ---------------------------
{api_code}
-------------------------------------------------------------------------

Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Keep the parameters of the given test function, if any, unchanged. Do *not* modify the assertation statement in the given test function. Strictly follow the output format below.

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
""".strip()

MUTANT_SYSTEM_PROMPT_CODE_2 = """
You are a world class Python programmer. You will be give a property and a property-based test function for testing the given property.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function if any. Do not modify the assertation statement in the given test function.
""".strip()

MUTANTS_TEST_FUNCTION_PROMPT_CODE_2 = """"
You will be given a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Keep the parameters of the given test function, if any, unchanged. Do *not* modify the assertation statement in the given test function. Strictly follow the output format below.

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
""".strip()

# ================================================ DOC AND CODE ================================================
# start of 'DOC AND CODE' section -->

# === Two stage prompting, stage 1: generate properties ===
PROPERTIES_PROMPT_DOC_CODE = """
Please review the following API documentation and source code for "{function_name}". You need to extract a list of properties used for property-based testing.

--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

--------------------------- Source Code ---------------------------
{api_code}
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
PBT_PROPERTIES_PROMPT_DOC_CODE = """Now, write a Python property-based test suite using the library Hypothesis testing the properties you described. Each property should have a separate test function. So if you have five properties, you should have five test functions.
In your generation strategy, be aware of very large inputs and overflows.
Import all the necessary modules for the test.
Strictly follow the output format described below when writing each test. For each test function name, use the following format: test_function_name_property.

--------------------------- Output Format ---------------------------
```python
from hypothesis import given, strategies as st
import [module_name]

@given(st.data())
def test_{function_name_2}_property():
    (...)
# End program
```
"""

MUTANT_SYSTEM_PROMPT_DOC_CODE = """
You are a world class Python programmer. You will be given API documentation, source code and a property for a function. A Python property-based test function for testing the given property will also be provided.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function. Do not modify the assertation statement in the given test function.
""".strip()

MUTANTS_TEST_FUNCTION_PROMPT_DOC_CODE = """"
You will be given API documentation, source code, a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Please review the following API documentation and source code for "{function_name}".
--------------------------- API Documentation ---------------------------
{api_documentation}
-------------------------------------------------------------------------

--------------------------- Source Code ---------------------------
{api_code}
-------------------------------------------------------------------------

Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Keep the parameters of the given test function, if any, unchanged. Do *not* modify the assertation statement in the given test function. Strictly follow the output format below.

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
""".strip()

# === The same as DOC_ONLY and CODE_ONLY ===
MUTANT_SYSTEM_PROMPT_DOC_CODE_2 = """
You are a world class Python programmer. You will be give a property and a property-based test function for testing the given property.
You need to write five different test functions that violate the given property. Each new test function should be based on the given test function, i.e. slightly modify the given test function to violate the property. Only modify the original output of the test function to violate the property for all inputs.
Do not change the parameters of the given test function, if any. Do not change the input for the given test function if any. Do not modify the assertation statement in the given test function.
""".strip()

MUTANTS_TEST_FUNCTION_PROMPT_DOC_CODE_2 = """"
You will be given a property, and a property-based test function for a function. You need to write five different test functions that violate the given property.
Here is a property of the {function_name} that you need to violate for the test function.
--------------------------- Property ---------------------------
{prop}
-------------------------------------------------------------------------

Here is the property-based test function for the above property.
--------------------------- Property-based Test Function ---------------------------
{pbt}
-------------------------------------------------------------------------

Here are the details of the task:
Write five different test functions that violate the given property. Each function should sligtly modify the given test function to violate the property for all inputs. Try to only change the output of the test function to violate the property.
Keep the parameters of the given test function, if any, unchanged. Do *not* modify the assertation statement in the given test function. Strictly follow the output format below.

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
""".strip()
