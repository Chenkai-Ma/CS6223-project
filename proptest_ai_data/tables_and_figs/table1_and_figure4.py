import os
import argparse
import pandas as pd
from dateutil.parser import parse
import seaborn as sns
import matplotlib.pyplot as plt

def generate_table_1(deps_df, pin_df, results_dir):
    tab_rows = []
    print("Generating table 1...")
    generate_table_row(deps_df, pin_df, tab_rows, direct=True)
    generate_table_row(deps_df, pin_df, tab_rows, direct=False)

    pd.DataFrame(tab_rows, columns=['Consumers', 'Consumers with >= 1 pin', 'Dependencies', 'Potential Upgrades']).to_csv(os.path.join(results_dir, 'table1.csv'))

def generate_figure_4(pin_df, results_dir):
    print("Generating Figure 4...")
    plot_hists(pin_df, results_dir)

def generate_table_row(dependencies_df, upgrade_df, rows, direct=True):
    if direct:
        dependencies_df = dependencies_df[dependencies_df["Depth"] == 1]
        upgrade_df = upgrade_df[upgrade_df["Depth"] == 1]
    else:
        dependencies_df = dependencies_df[dependencies_df["Depth"] > 1]
        upgrade_df = upgrade_df[upgrade_df["Depth"] > 1]


    num_deps = len(dependencies_df)
    num_consumers = len(dependencies_df[dependencies_df.apply(lambda row: row["VersionPublishDate"] is not None and row["DependencyVersionPublishDate"] is not None, axis=1)].groupby('Name').count())
    num_pinned_consumers = len(upgrade_df.groupby('Consumer').count())
    num_upgrades = len(upgrade_df.groupby(["Dependency", "Dependency Version", "Highest Upgrade"]))
    rows.append([num_consumers, num_pinned_consumers, num_deps, num_upgrades])


def plot_hists(upgrade_df, results_dir, color="blue", save=True):
    upgrade_df["Highest Upgrade Date"] = upgrade_df["Highest Upgrade Date"].apply(lambda row: parse(row))
    upgrade_df["Dependency Date"] = upgrade_df["Dependency Date"].apply(lambda row: parse(row))
    upgrade_df["Difference in Version Dates"] = upgrade_df["Highest Upgrade Date"] - upgrade_df["Dependency Date"]
    upgrade_df["Version Difference in Days"] = upgrade_df["Difference in Version Dates"].apply(lambda x: x.total_seconds() / 86400)

    upgrade_df_unique = upgrade_df.drop_duplicates(subset=["Dependency", "Dependency Version", "Highest Upgrade"])
    plt.figure()
    plt.ylabel("Number of Pins")
    plt.xlabel("Days behind Upgrade Version")
    plt.title("Age of Directly Pinned Versions\n(publish time)")
    sns.histplot(data=upgrade_df_unique[upgrade_df_unique["Depth"] == 1], x="Version Difference in Days", log_scale=(False, False), kde=True, color="blue")

    plt.savefig(os.path.join(results_dir, "fig4_direct_publish_time.pdf"), bbox_inches='tight')

    plt.figure()
    plt.title("Age of Directly Pinned Versions\n(number of versions)")
    plt.ylabel("Number of Pins")
    plt.xlabel("Versions behind Upgrade Version")
    sns.histplot(data=upgrade_df_unique[upgrade_df_unique["Depth"] == 1], x="Number of Upgrades", log_scale=(True, False), kde=True, color="blue")
    plt.savefig(os.path.join(results_dir, "fig4_direct_versions.pdf"), bbox_inches='tight')


    upgrade_df_unique = upgrade_df.drop_duplicates(subset=["Dependency", "Dependency Version", "Highest Upgrade"])
    plt.figure()
    plt.ylabel("Number of Pins")
    plt.xlabel("Days behind Upgrade Version")
    plt.title("Age of Indirectly Pinned Versions\n(publish time)")
    sns.histplot(data=upgrade_df_unique[upgrade_df_unique["Depth"] > 1], x="Version Difference in Days", log_scale=(False, False), kde=True, color="green")
    plt.savefig(os.path.join(results_dir, "fig4_indirect_publish_time.pdf"), bbox_inches='tight')

    plt.figure()
    plt.title("Age of Indirect Pins (versions)")
    plt.ylabel("Number of Pins")
    plt.title("Age of Indirectly Pinned Versions\n(number of versions)")
    plt.xlabel("Versions behind Upgrade Version")
    sns.histplot(data=upgrade_df_unique[upgrade_df_unique["Depth"] > 1], x="Number of Upgrades", log_scale=(True, False), kde=True, color="green")
    plt.savefig(os.path.join(results_dir, "fig4_indirect_versions.pdf"), bbox_inches='tight')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", required=True, type=str)
    parser.add_argument("--results_dir", required=True, type=str)

    args = parser.parse_args()

    deps_file = os.path.join(args.data_dir, "dataset_dependencies.csv")
    pins_file = os.path.join(args.data_dir, "dataset_pins.csv")

    print("Loading data...")
    deps_df = pd.read_csv(deps_file)
    pins_df = pd.read_csv(pins_file)

    generate_table_1(deps_df, pins_df, args.results_dir)
    generate_figure_4(pins_df, args.results_dir)
