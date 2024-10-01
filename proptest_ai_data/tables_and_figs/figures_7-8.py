import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import argparse
import scipy
import seaborn as sns
import os

def generate_raw_cov_plot(cov_df, results_dir, fig_name):
  fig, ax = plt.subplots()
  sns.violinplot(cov_df['Count'], cut=10)

  # Rotate x-axis labels for better visibility
  plt.xticks([])
  plt.yticks(fontsize=15)

  # Set labels and title
  ax.set_xlabel('Dependency', fontsize=20)
  ax.set_ylabel('Lines Covered in Dependency', fontsize=20)
  ax.set_title('Line Coverage of Dependency by \n One Consumer Test Suite', fontsize=20)
  ax.set_ylim(0, 12000)


  # Display the plot
  plt.tight_layout()
  plt.savefig(os.path.join(results_dir, fig_name), bbox_inches='tight')


def generate_cov_plot(cov_df, results_dir, fig_name, accum=False):
    sns.set(style="darkgrid")
    plt.figure(figsize=(7,5))
    color = (0.4766525695245418, 0.7651057285659362, 0.51439702678457)
    if accum:
        sns.barplot(cov_df, x='k', y='Improvement', estimator=scipy.stats.gmean, color=color)
        plt.title("Consumer Test Suite Coverage", fontsize=18)
        plt.xticks([0, 3, 8, 13, 18, 23, 28, 33], fontsize=15)
    else:
        sns.set(rc={'figure.figsize':(7,5)})
        sns.barplot(cov_df, x='k', y='Improvement', color=color, width=0.5)
        plt.title("Consumer Test Suite Coverage\n of commons-io@2.4", fontsize=20)
    plt.yticks(fontsize=15)
    plt.ylabel("Coverage Improvement\nof Dependency", fontsize=18)
    plt.xlabel("Number of Consumer Test Suites", fontsize=18)
    fmt = '%.0f%%'

    yticks = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(yticks)
    plt.savefig(os.path.join(results_dir, fig_name), bbox_inches='tight')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", required=True, type=str)
    parser.add_argument("--results_dir", required=True, type=str)

    args = parser.parse_args()

    raw_cov = pd.read_csv(os.path.join(args.data_dir, "raw_coverage.csv"))
    result_df = raw_cov.groupby(['Consumer', 'Consumer_Version', 'Dependency', 'Dependency_Version']).size().reset_index(name='Count')

    generate_raw_cov_plot(result_df, args.results_dir, "figure_7a.pdf")

    cov_df = pd.read_csv(os.path.join(args.data_dir, 'coverage.csv'))
    generate_cov_plot(cov_df[(cov_df['Dependency'] == 'commons-io:commons-io') &
                     (cov_df['Dependency_Version'] == '2.4')], args.results_dir, "figure_7b.pdf", accum=False)
    generate_cov_plot(cov_df, args.results_dir, "figure_8.pdf", accum=True)
