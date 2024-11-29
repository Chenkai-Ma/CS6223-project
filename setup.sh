#!/bin/bash

# this file has to be run from the root directory of the project
# register setting profile, and load sound_valid.
python conftest.py

# prefix python files with "test" to conform to the naming convention
# find gpt-4-final -type f -name "*.py" | while read file; do
#     dir=$(dirname "$file")
#     base=$(basename "$file")

#     # Check if the file already starts with "test"
#     if [[ $base != test* ]]; then
#         mv "$file" "$dir/test_$base"
#     fi
# done





