# CS6223 project: Explore the Impact of API Source Code on LLM-Aided Property-Based Testing

## Contributions of Group Members

| Name | Code                                                            | Paper                                       |
| ---- | --------------------------------------------------------------- | ------------------------------------------- |
| Chenkai Ma  | Evaluation/post-processing                                      | Analysis of the method and paper writing   |
| Xu Zhao   | LLM prompting (in both methods and computing property coverage) | Analysis of the method and paper writing |

## File Structure

- `prompt.py`: The prompts used to generate properties, PBTs and property mutants.
- `dataset`: The dataset used in the experiment, including 30 API methods, their docs, and codes.
- `code_only`, `doc_only`, `doc_and_code`: All the generated properties, PBTs and property mutants for each API method. Each folder correponds to each method. For example, `code_only` contains all the generated data with `code_only` prompt method.
- `script_llm`: The script to prompt LLM to generate data. We use `code_only` as an example. Users can replace the file path in the script to generate data with other prompt methods.

This project is based on [Vikram, Vasudev, et al. "Can large language models write good property-based tests?](https://arxiv.org/pdf/2307.04346)


----
### Evaluation: Property Coverage

- Actual prompt to extract properties p1 for a API method f: reuse prompts in [`prompts.py`](proptest_ai_data/prompts.py) for two stage prompting.
- The code to generate five property mutants for each property pi is in [`prompts.py`](proptest_ai_data/prompts.py): `(Maybe)SYSTEM_PROMPT + MUTANTS_PROMPT (filled with api docs and one property)`

## Ideas for the project

### Property Coverage

- Property coverage: Instead of generating property mutants from original API, then substitude original PTB to get mutated PTB, we may **directly prompt LLM to generate mutated test functions from original test functions (along with their properties).** This helps to solve some intricacies of constructing mutated PTB (see your notes), simplifies the workflow, and could also be **one contribution**. Mutated test functions should be filtered for soundness, and aim for assertion errors.

- For each API method: 

- [@mck] For each property, find one corresponding test function (entire PBTs are unnecessary) that are sound and valid. If multiple such test functions exist, choose one randomly.
- [@zx] For each pair of (test function, property), prompt LLM to generate 5 mutated test functions ("property mutant"). Essentially, a property mutant is the original test function + few lines of codes that manipulate the output from API method to violate the corresponding property, while keeping other things, especially the invocation of API and assertion, intact.
- [@mck] Test these property mutants, only aim for assertion errors (this means filtering invalid ones with run-time errors)
- [@mck] Compute property mutation score and property coverage.

### Experiment Setup

- API to test [(Google doc)](https://docs.google.com/spreadsheets/d/1ho1ij9dSY98MuzCt7yKXHBuz76prcS5Z1I_kI3RQznE/edit?gid=0#gid=0): 30 in total (16 original + 14 new). The source code for each API should be at least moderately self-contained, i.e., have some basic logic, and should be rather simple/short. Docs are stored in folder "api_docs" as .txt files and named according to the url of the API, e.g. "[datetime.date.isocalendar](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar)" (this naming is a little different from the original paper), while the content are directly copied from the urls. Codes are stored in folder "api_codes" as .py files and named similarly, and the content are just the one function for the API (no other stuff like imports). Specifically, for each code, I removed the docstring because it is similar to the docs, and we want to separate codes from docs; I also slightly adjusted some identation; 

## Experiment Result

- [google doc](https://docs.google.com/spreadsheets/d/1ho1ij9dSY98MuzCt7yKXHBuz76prcS5Z1I_kI3RQznE/edit?gid=2025599766#gid=2025599766)
