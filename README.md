# CS6223 project: Explore the Impact of API Source Code on LLM-Aided Property-Based Testing

In this project, we investigate the role of API source code in LLM-aided PBT generation, with three prompting approaches: using API source code alone("code_only"), API documentation alone("doc_only"), and a combination of both("doc_and_code").

## File Structure

- `prompt.py`: The prompts used to generate properties, PBTs and property mutants.
- `dataset`: The dataset used in the experiment, including 30 API methods, their docs, and codes.
- `code_only`, `doc_only`, `doc_and_code`: All the generated properties, PBTs and property mutants for each API method. Each folder correponds to each method. For example, `code_only` contains all the generated data with `code_only` prompt method.
- `script_llm`: The script to prompt LLM to generate data. We use `code_only` as an example. Users can replace the file path in the script to generate data with other prompt methods.
- `sound_valid.sh`: 
- `property_coverage.sh`: 


## Contributions of Group Members

| Name | Code                                                            | Paper                                       |
| ---- | --------------------------------------------------------------- | ------------------------------------------- |
| Chenkai Ma  | Evaluation/post-processing                                      | Analysis of the method and paper writing   |
| Xu Zhao   | LLM prompting (in both methods and computing property coverage) | Analysis of the method and paper writing |


This project is based on [Vikram, Vasudev, et al. "Can large language models write good property-based tests?](https://arxiv.org/pdf/2307.04346)