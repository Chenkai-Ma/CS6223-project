import os
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

import seaborn as sns

import matplotlib.ticker as mtick
import matplotlib as mpl

def rename_columns(df):
    df['tech'] = df['tech'].replace({'pbt': 'Single Stage', 'pbt_and_props': 'Two Stage'})
    df['model'] = df['model'].replace({'claude-3-opus-20240229': 'Claude-3-Opus',
                                   'gemini-1.5-pro-latest-final': 'Gemini-1.5-Pro',
                                   'gpt-4-final': 'GPT-4'})

def plot_metric(results, save_file):

    # Filter

    results = results[results['validity'] > 0]
    results = results.groupby(['tech', 'api', 'model'])[['validity', 'soundness']].mean().reset_index()
    rename_columns(results)
    results[f"{metric}_perc"] = results[metric] / 1000 * 100

    results = results.rename(columns={'tech': 'Approach'})

    plt.figure(figsize=(6, 4))
    ax = sns.violinplot(data=results, x="model", y=f"{metric}_perc", hue="Approach", split=True, inner="quart", cut=0)
    hatches = ['','x', '', 'x', '', 'x']
    ihatch = iter(hatches)
    _ = [i.set_hatch(next(ihatch)) for i in ax.get_children() if isinstance(i, mpl.collections.PolyCollection)]

    handles, labels = ax.get_legend_handles_labels()
    handles[1].set_hatch('x')


    # Adding legend
    ax.legend(handles, labels, loc='best')

    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
#     plt.ylim((0, 100))
    plt.xlabel("Model", fontsize=15)
    plt.legend(loc='lower left')
    plt.ylabel(f"Average {metric.capitalize()}\n(1,000 executions)", fontsize=15)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)
    plt.savefig(save_file, bbox_inches='tight')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_dir", required=True, type=str)
    parser.add_argument("--output_dir", required=True, type=str)

    args = parser.parse_args()

    valid_sound_df = pd.read_csv(os.path.join(args.results_dir, 'validity_soundness.csv'))
