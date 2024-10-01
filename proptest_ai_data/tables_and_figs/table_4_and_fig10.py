import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)
    args = parser.parse_args()

    mut_df = pd.read_csv(os.path.join(args.results_dir, "property-mutant-score.csv"))
    mut_df['library'] = mut_df['api'].apply(lambda x: x.split('.')[0])
    mut_df['propcoverage'] = mut_df['killed'] * 100
    with open(os.path.join(args.output_dir, "table_4.csv"), "w") as f:
        f.write("Model,Approach,Property Mutation Score, Total Mutants\n")
        for m in set(mut_df['model'].values):
            for tech in ['pbt', 'pbt_and_props']:
                approach = 'Single Stage' if tech == 'pbt' else 'Two Stage'
                total = len(mut_df[(mut_df['tech'] == tech) & (mut_df['model'] == m)])
                percent = len(mut_df[(mut_df['tech'] == tech) & (mut_df['model'] == m) & (mut_df['killed'] == 1)]) / total
                f.write(f"{m},{approach},{percent},{total}\n")

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    bar_plot = sns.barplot(x='library', y='propcoverage', data=mut_df)

    # Customize the plot
    bar_plot.set_xlabel('Library', fontsize=16)
    bar_plot.set_ylabel('Percent of Killed Mutants', fontsize=16)
    bar_plot.set_title("Property Mutation Score of Samples", fontsize=20)
    plt.xticks(rotation=45, ha="right", fontsize=14)
    bar_plot.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.yticks(fontsize=14)
    # labels = ['Single Stage', 'Two Stage']
    # h, l = bar_plot.get_legend_handles_labels()
    # bar_plot.legend(h, labels, title="Approach")

    plt.savefig("property-coverage-library.pdf", bbox_inches='tight')



