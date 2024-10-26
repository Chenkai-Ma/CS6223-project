# Meeting Notes - [2024/10/24]

## Reminders

- Full-scale experiment: it takes two rounds. In the first round, zx generates PBTs and mck filter sound and valid PBTs; in the second round, zx generates mutated test functions from test functions in sound and valid PBTs and mck computes property coverage.
- RQ3 ("docs + codes" vs. "codes only"): details TBD.
- The code (artifact) of this project will also be graded.

### Property Coverage Workflow

For each API method: 

- [@mck] For each property, find one corresponding test function (entire PBTs are unnecessary) that are sound and valid. If multiple such test functions exist, choose one randomly.
- [@zx] For each pair of (test function, property), prompt LLM to generate 5 mutated test functions ("property mutant"). Essentially, a property mutant is the original test function + few lines of codes that manipulate the output from API method (while keep other things intact).
- [@mck] Test these property mutants, only aim for assertion errors (this means filtering invalid ones with run-time errors)
- [@zx] Compute property mutation score and property coverage.


## Progress

- Migrated codes (sound&valid) to our github repo.
- Tested sound and valid and mutants, results in [`logs`](our_proptest_data/logs)

## Feedback 

### Property coverage

- 形式上，基本ok（生成结果就是test functions，即property mutant）。不过命名上还可以更清晰：建议每一个property对应一个.py文件，该文件内包含该property的5个property mutant（即5个test function）。这个.py文件的名字（或者其包含的property mutant的函数名）应指出这个property是什么。
- 实现上，个人感觉还可以更简洁：沿用原始的test function（包括assertion），只不过添加一段代码对API方法返回的结果做一次变换（以违反对应的property）。例如，statistics_variance的[pbt_1.py](our_proptest_data/proptest/statistics_variance/pbt_1.py)有如下的test function: 

```
@given(st.lists(st.floats(), min_size=2))
def test_output_non_negative_property(data):
    result = statistics.variance(data)
    assert result >= 0  # Variance cannot be negative
```

它的一个property mutant就是

```
@given(st.lists(st.floats(), min_size=2))
def test_output_non_negative_property(data):
    result = statistics.variance(data)
    result = -1 * result
    assert result >= 0  # Variance cannot be negative
```

该property mutant和原本的test function唯一的区别在于多了一行代码`result = -1 * result`用于变换API方法的输出.类似的，如果原本的assertion是`assert result == 0`，那么property mutant可以添加如下代码`result = result + 1`.

- 后续建议: 对于下表的`statistics_variance`的两个[property](our_proptest_data/properties/statistics_variance.txt)和对应的test function，请分别提供5个property mutant。上方的reminder描述了计算property coverage的流程。

| Property | Test Function |
| ----------- | ----------- |
| property 1: non-negative | `test_variance_non_negative_property()` from [cs6223/our_proptest_data/proptest/statistics_variance/pbt_2.py](our_proptest_data/proptest/statistics_variance/pbt_2.py)  |
| property 2: identical values | `test_variance_identical_values_property()` from [cs6223/our_proptest_data/proptest/statistics_variance/pbt_2.py](our_proptest_data/proptest/statistics_variance/pbt_2.py)  |