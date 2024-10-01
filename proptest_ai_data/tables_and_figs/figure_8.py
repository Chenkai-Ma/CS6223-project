import os
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

import seaborn as sns

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)

    args = parser.parse_args()

    valid_sound_df = pd.read_csv(os.path.join(args.results_dir, 'validity_soundness.csv'))
    valid_sound_df['Library'] = valid_sound_df['api'].apply(lambda x: x.split('.')[0])
    filtered_df = valid_sound_df[(valid_sound_df['validity'] == 1000) & (valid_sound_df['soundness'] == 1000) & (valid_sound_df['model'] == 'gpt-4-final')]

    # Calculate the percentage of rows that meet the condition for each Library value
    library_percentage = filtered_df.groupby(['Library', 'tech']).size() / valid_sound_df[valid_sound_df['model'] == 'gpt-4-final'].groupby(['Library', 'tech']).size() * 100

    # Convert the percentage data to a DataFrame
    percentage_df = library_percentage.reset_index()
    percentage_df.columns = ['Library', 'tech', 'Percentage']

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    bar_plot = sns.barplot(x='Library', y='Percentage', data=percentage_df, hue='tech')

    # Customize the plot
    bar_plot.set_xlabel('Library', fontsize=16)
    bar_plot.set_ylabel('Percentage Valid and Sound \n Test Functions', fontsize=16)
    bar_plot.set_title("Valid and Sound Test Functions\n by Library (GPT-4)", fontsize=20)
    plt.xticks(rotation=45, ha="right", fontsize=14)
    bar_plot.yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.yticks(fontsize=14)
    labels = ['Single Stage', 'Two Stage']
    h, l = bar_plot.get_legend_handles_labels()
    bar_plot.legend(h, labels, title="Approach")

    plt.savefig(os.path.join(args.output_dir, 'figure8.pdf'), bbox_inches='tight')

