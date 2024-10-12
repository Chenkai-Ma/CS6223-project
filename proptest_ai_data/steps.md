Use `prompt.py`, instead of `origin_prompt.py`

Two stage prompting for generating PBTs:

Stage 1: `generate_pbt.py`

1. Extract at least 5 properties --> sample 1 time, temp = 0?
2. Generate tests based on the properties. --> sample 5 times, temp=0.7

Stage 2: `generate_mutants.py`

Generate mutants --> for each property, generate 5 buggy version one time, temp = 0?
