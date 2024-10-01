import pandas as pd
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)
    args = parser.parse_args()

    new_df = pd.read_csv(os.path.join(args.results_dir, "validity_soundness.csv"))

    with open(os.path.join(args.output_dir, "table_2.csv"), 'w') as f:
        f.write("model,approach,total,valid,both\n")
        for m in set(new_df['model'].values):
            for tech in ['pbt', 'pbt_and_props']:
                total = len(new_df[(new_df['tech'] == tech) & (new_df['model'] == m)])
                valid = len(new_df[(new_df['tech'] == tech) & (new_df['model'] == m) & (new_df['validity'] == 1000)])
                both = len(new_df[(new_df['tech'] == tech) & (new_df['model'] == m) & (new_df['soundness'] == 1000) & (new_df['validity'] == 1000)])
                approach = "single" if tech == 'pbt' else 'two'
                f.write(f"{m},{approach},{total},{valid},{both}\n")


