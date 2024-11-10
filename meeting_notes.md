# Meeting Notes

## Reminders

### Experiments

- Experiment planning：

|  | Our method: code + doc | Baseline: doc only (from original paper) | Baseline: code only |
| ----------- | ----------- | ----------- | ----------- |
| RQ1: Sound and Valid | if time permits | done | done |
| RQ2: Property Coverage | if time permits | done | TBD (21 Nov?) |

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

- [google doc](https://docs.google.com/spreadsheets/d/1ho1ij9dSY98MuzCt7yKXHBuz76prcS5Z1I_kI3RQznE/edit?gid=2025599766#gid=2025599766)
- Doc only 的property coverage已完成：和原论文相比, property coverage高很多（说明我们的方法确实有作用？）。
- Code only的sound & valid已完成。表现不如doc only，结果和原论文接近。
- Code only的test function的jsonl文件都生成了，保存在`/our_proptest_data/sound_valid`。可以进行后续的mutant的生成了。（感觉结果不一定比doc only差）。

## Feedback 

- 实验结果：code only的整体表现可能不如doc only。那么至少有两种思路：第一个是不做code+doc的实验，而是在report里面强调探究code only的效果（同时也可以说一下其他改进的效果，例如property mutant）；第二个是做code+doc方法的实验，然后期待其效果大于doc only。