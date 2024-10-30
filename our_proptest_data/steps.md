Use `prompt.py`, instead of `origin_prompt.py`

Two stage prompting for generating PBTs:

Stage 1: `generate_pbt.py`

1. Extract at least 5 properties --> sample 1 time, temp = 0.5 (`generate_pbt.py --mode properties --temperature 0.5 --num_samples 1`)

   1. output file: our_proptest_data/properties
2. Generate tests based on the properties. --> number of samples 5, temp=0.7 (`generate_pbt.py --mode pbt --temperature 0.7 --num_samples 5`)

   1. output file: our_proptest_data/proptest/{function_name}/pbt_{i}.py
   2. each pbt_{i}.py corresponds to a sample.  There are 5 test functions in each test_{i}.py, each function corresponds to a property.

Stage 2: `generate_mutants.py`

Generate mutants --> for each sound and valid test function, generate 5 test functions that violate the property, temp = 0.5 (`generate_mutants.py --num_samples 1 --temperature 0.5`)

output file: our_proptest_data/mutants/{funtion_name}/mutant_{i}.py

each mutant_{i}.py corresponds to a sound and valid test function. It contains 5 new test functions that violate the property.
