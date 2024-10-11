# Evaluate soundness and validity separately for each API.
# 如果要使用这个脚本，需要将其放在cs6223/proptest_ai_data/proptests目录下

log_dir="sound_valid_logs"

mkdir -p $log_dir

APIs=($(ls gpt-4-final))

for API in "${APIs[@]}"
do
    mkdir -p $log_dir/$API
    for prompting_method in "single_stage" "two_stage"
    do
        echo "Evaluating $API: $prompting_method"
        pytest gpt-4-final/$API/$prompting_method/pbt_*.py \
            --continue-on-collection-errors \
            --hypothesis-profile=debug \
            --tb=line \
            > $log_dir/$API/$prompting_method.log
    done
done