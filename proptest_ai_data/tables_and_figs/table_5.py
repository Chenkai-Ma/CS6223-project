import pandas as pd
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)
    args = parser.parse_args()

    prop_cov_df = pd.read_csv(os.path.join(args.results_dir, "property-coverage.csv"))
    with open(os.path.join(args.output_dir, "table_5.csv"), "w") as f:
        f.write("Model,Approach,Property Coverage\n")
        for m in ['gpt-4-final', 'claude-3-opus-20240229', 'gemini-1.5-pro-latest-final']:
            for tech in ['pbt', 'pbt_and_props']:
                prop_cov = len(prop_cov_df[(prop_cov_df['propcoverage'] > 0) & (prop_cov_df['model'] == m) & (prop_cov_df['tech'] == tech)]) / 200
                approach = 'Single Stage' if tech == 'pbt' else 'Two Stage'
                f.write(f"{m},{approach},{prop_cov}\n")
