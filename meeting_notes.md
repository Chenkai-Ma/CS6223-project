# Meeting Notes

## Reminders

### Experiments

- Experiment result: [google doc](https://docs.google.com/spreadsheets/d/1ho1ij9dSY98MuzCt7yKXHBuz76prcS5Z1I_kI3RQznE/edit?gid=2025599766#gid=2025599766)

- Experiment planning：

|  | Our method: code + doc | Baseline: doc only (from original paper) | Baseline: code only |
| ----------- | ----------- | ----------- | ----------- |
| RQ1: Sound and Valid | Done | done | done |
| RQ2: Property Coverage | Done | done | done |

- Procedure for RQ1: zx generates PBTs, then mck filter sound and valid test functions.

- Procedure for RQ2 (details below): mck select pairs of (sound and valid test function, property) according to last cell of [process_data.ipynb](our_proptest_data/process_data.ipynb) （Jsonl：对于部分API，有的property没有sound&valid的test function，那么在生成jsonl的时候就property的数目、pbt的数目就会相应减少）; then zx generates mutated test functions; then mck computes property coverage.

### Property Coverage Workflow

For each API method: 

- [@mck] For each property, find one corresponding test function (entire PBTs are unnecessary) that are sound and valid. If multiple such test functions exist, choose one randomly.
- [@zx] For each pair of (test function, property), prompt LLM to generate 5 mutated test functions ("property mutant"). Essentially, a property mutant is the original test function + few lines of codes that manipulate the output from API method to violate the corresponding property, while keeping other things, especially the invocation of API and assertion, intact.
- [@mck] Test these property mutants, only aim for assertion errors (this means filtering invalid ones with run-time errors)
- [@mck] Compute property mutation score and property coverage.

### Other

- Writing: (Try to) finish in 28 Nov. So we have time to check, revise (if any), and organize codes, etc.
- The code (artifact) of this project will also be graded.
- Project due: 2 Dec.

## Progress

- Code + doc: sound and valid evaluation complete: worst among three. Property coverage: mutant is normal; mutant 2 performs pretty well.

- Mutant 2: mixed performance.

## Feedback 

