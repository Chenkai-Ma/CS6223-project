# Meeting Notes

## Reminders

### Experiments

- Experiment planning：

|  | Our method: code + doc | Baseline: doc only (from original paper) | Baseline: code only |
| ----------- | ----------- | ----------- | ----------- |
| RQ1: Sound and Valid | *TBD | done | 14 Nov |
| RQ2: Property Coverage | *TBD | 14 Nov | TBD (21 Nov?) |

- Procedure for RQ1: zx generates PBTs, then mck filter sound and valid test functions.

- Procedure for RQ2 (details below): mck select pairs of (sound and valid test function, property) according to last cell of [process_data.ipynb](our_proptest_data/process_data.ipynb); then zx generates mutated test functions; then mck computes property coverage.

### Property Coverage Workflow

For each API method: 

- [@mck] For each property, find one corresponding test function (entire PBTs are unnecessary) that are sound and valid. If multiple such test functions exist, choose one randomly.
- [@zx] For each pair of (test function, property), prompt LLM to generate 5 mutated test functions ("property mutant"). Essentially, a property mutant is the original test function + few lines of codes that manipulate the output from API method (while keep other things intact).
- [@mck] Test these property mutants, only aim for assertion errors (this means filtering invalid ones with run-time errors)
- [@mck] Compute property mutation score and property coverage.

### Other

- The code (artifact) of this project will also be graded.
- Project due: 2 Dec.

## Progress

### Sound and valid

- 已完成对于doc方法生成的30个API的test function的sound和valid的测试，结果在[google doc](https://docs.google.com/spreadsheets/d/1ho1ij9dSY98MuzCt7yKXHBuz76prcS5Z1I_kI3RQznE/edit?gid=2025599766#gid=2025599766)。**结论：比原论文(在它的40个API上)的结果更好**。
- Jsonl: 生成了所有API对应的jsonl文件。对于部分API，有的property没有sound&valid的test function，那么在生成jsonl的时候就property的数目、pbt的数目就会相应减少。另外，我把`statistics.variance`的jsonl删了，因为我们不用这个API。（该API其他的文件也可以考虑删了）

## Feedback 

### RQ1: Sound and Valid

- For "code + doc": TBD (if we have time)

### RQ2: Property coverage

- 形式（格式以及命名）都没有问题，之后沿用就好了。
- 内容似乎不对。mutant_*.py的每个test function还是正常的PBT（即检查API的输出是否满足给定的property）。这些test function主要对输入数据进行了变换，这其实相当于fuzzing，而hypothesis已经在构造example的时候已经自动做了这一步了。对于一个mutated test function，我们期望的是**沿用原来对应的test function（保持所有内容不变）**，除了**对API的输出做一次变换以违反对应的property，以期望原来的assertion会失败**。请参考以下的例子，它比较了原论文和我们的方法的异同：

API： `html.escape`

它的第一个property：
```
1. The output should not contain any '&', '<' or '>' characters unless they are part of an HTML-safe sequence. This holds regardless of the input string 's' or the truth value of the 'quote' argument.
```

对于该property的一个（原本的）test function:

```
@given(st.text())
def test_no_html_unsafe_characters(s):
    result = html.escape(s)
    assert not any(c in result for c in '&<>')
```

对于该API和该property的一个property mutant：
```
The first version will always add a non-escaped "&" character at the end of the string
def buggy_1(s, quote=True):
    modified_string = html.escape(s, quote) + '&'
    return modified_string
```

可以看到，本质上该property mutant就是**首先调用了这个API**，然后**对其输出做了一次变换以违反对应的property**。

原论文的方法是在构造出了该property mutant之后，通过在**test function中把对API的调用替换成对property mutant的调用**，从而构造出一个mutated test function：

```
@given(st.text())
def test_no_html_unsafe_characters_mutant(s):
    result = buggy_1(s)
    assert not any(c in result for c in '&<>')
```

注意该mutated test function和原本的test function除了在调用API的地方有区别，**其他地方（包括assertion）都完全一样**。

原论文的方法有两步：生成property mutant，然后构造mutated test functions。我们的方法将这两步合并到一步，即我们希望通过原本的test function和对应的property，跳过property mutant，直接生成如下的mutated test function：

```
@given(st.text())
def test_no_html_unsafe_characters_mutant(s):
    result = html.escape(s, quote) + '&'
    assert not any(c in result for c in '&<>')
```

请注意，该mutated test function和原论文生成的mutated test function是等价的，二者和原本的test function的唯一区别就是对API调用的结果进行了一次变换以违反property。

### Writing

- I suggest finishing writing in 28 Nov. So we have time to check, revise (if any), and organize codes, etc.