# Evaluate property coverage for each API.
# this file has to be run from the our_proptest_data directory

approach="doc_and_code"
metric="property_coverage"

log_dir="${approach}/logs/${metric}_2_log"
api_dir="${approach}/mutants_2"

mkdir -p $log_dir

APIs=($(ls $api_dir))
skip_list=("cryptography.fernet.Fernet.encrypt"
"decimal.Decimal.quantize"
"numpy.add"
"pandas.cut"
"pandas.merge"
"_old_statistics_variance"
"statistics_variance")

for API in "${APIs[@]}"
do
    if [[ " ${skip_list[@]} " =~ " ${API} " ]]; then
        echo "Skipping $API"
        continue
    fi

    echo "Evaluating $API"
    pytest $api_dir/$API/mutant_*.py \
        --continue-on-collection-errors \
        --hypothesis-profile=debug \
        --tb=line \
        > $log_dir/$API.log
done