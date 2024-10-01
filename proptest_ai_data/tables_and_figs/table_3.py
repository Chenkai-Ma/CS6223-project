import pandas as pd
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)
    args = parser.parse_args()

    df = pd.read_csv(os.path.join(args.results_dir, "property-labels.csv"))
    # Filter out empty assertion values
    df = df[df['Is Assertion #1 sound?'].notnull() |
            df['Is Assertion #2 sound?'].notnull() |
            df['Is Assertion #3 sound?'].notnull() |
            df['Is Assertion #4 sound?'].notnull() |
            df['Is Assertion #5 sound?'].notnull()]
    df['Total Assertions'] = df[['Is Assertion #1 sound?', 'Is Assertion #2 sound?', 'Is Assertion #3 sound?',
                                  'Is Assertion #4 sound?', 'Is Assertion #5 sound?']].notnull().sum(axis=1)
    df['Total Yes'] = df[['Is Assertion #1 sound?', 'Is Assertion #2 sound?', 'Is Assertion #3 sound?',
                          'Is Assertion #4 sound?', 'Is Assertion #5 sound?']].eq('Yes').sum(axis=1)
    grouped = df.groupby(['Model'])[['Total Assertions', 'Total Yes']].agg('sum').reset_index()

    total_row = pd.DataFrame([{'Model': 'Total', 'tech': 'Total',
                              'Total Assertions': df['Total Assertions'].sum(),
                              'Total Yes': df['Total Yes'].sum()}])

    result = pd.concat([grouped, total_row], ignore_index=True)

    with open(os.path.join(args.output_dir, "table_3.csv"), "w") as f:
        f.write("Model,Sound,Unsound\n")


        for index, row in result.iterrows():
            approach = 'Single Stage' if row['tech'] == 'pbt' else 'Two Stage'
            f.write(f"{row['Model']},{approach},{row['Total Yes']},{row['Total Assertions'] - row['Total Yes']}\n")
