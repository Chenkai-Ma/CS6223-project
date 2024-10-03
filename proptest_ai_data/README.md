# Proptest AI: Anonymized Dataset

## Getting-started

The synthesized property-based tests are located in `proptest/`. 
The extracted properties and mutants are located in `properties` and `mutants` respectively. API Documentation is located in `api_docs`.
The prompt templates are located in `prompts.py`.

All soundness, validity, and property coverage data are located in `results/`
Scripts used to generate the tables and figures can be found in the `tables_and_figs/` directory. The tables and figures are located in the `figures/` directory.

* You will need **Python 3** on your system. 

First, please install requirements using the following command:
```
pip install -r requirements.txt
```

## Generating tables and figures

To generate figures, run the corresponding script using the following command:
```
python <script.py> --results_dir <results_dir> --output_dir <figures_dir>
```

For example,
```
python tables_and_figs/figure_5.py --results_dir results/ --output_dir figures/

```




