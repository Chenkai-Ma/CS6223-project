# Meeting Notes - [2024/10/10]

## Progress

- Evaluating soundness and validity: basically done. Identifying sound and valid PTBs is done manually.
- Evaluating property coverage: a prototype is tested, but there are several issues pending.
- An updated requirementx.txt

## Suggestions

- Follow the file structure and naming conventions of the origianl project.
- Writing: each person writes about the part he implements. As for the rest, do together.
- Property coverage: Instead of generating property mutants from original API, then substitude original PTB to get mutated PTB, we may **directly prompt LLM to generate mutated test functions from original test functions (along with their properties).** This helps to solve some intricacies of constructing mutated PTB (see your notes), simplifies the workflow, and could also be **one contribution**. Mutated test functions should be filtered for soundness, and aim for assertion errors.
- Use the same properties to generate original PTBs (e.g., in double-stage prompting) and property mutants to prevent mismatches.