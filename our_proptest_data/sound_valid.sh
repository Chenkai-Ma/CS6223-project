# Evaluate soundness and validity separately for each API.
# this file has to be run from the root directory of the project

log_dir="logs/sound_valid_log"
api_dir="proptest"

mkdir -p $log_dir

APIs=($(ls $api_dir))
skip_list=("cryptography.fernet.Fernet.encrypt"
"decimal.Decimal.quantize"
"numpy.add"
"pandas.cut"
"pandas.merge")

for API in "${APIs[@]}"
do
    if [[ " ${skip_list[@]} " =~ " ${API} " ]]; then
        echo "Skipping $API"
        continue
    fi

    echo "Evaluating $API"
    pytest $api_dir/$API/pbt_*.py \
        --continue-on-collection-errors \
        --hypothesis-profile=debug \
        --tb=line \
        > $log_dir/$API.log
done