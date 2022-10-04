import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("cross_study_data/data4jasp.csv")

sns.set_theme()
sns.set_style("whitegrid")
sns.set_palette("colorblind")
sns.set_context("talk")


# plot extraversion, ext/int in x, model in y
sns.catplot(
    data=data,
    x="Study",
    y="Extraversion",
    hue="Model",
    errorbar="ci",
    hue_order=["Expert", "GPT-3", "STRAP"],
    kind="point",
    dodge=True,
    sharex=True,
    sharey=True,
    legend=""
).savefig("cross_study_data/plots/cross_study_extraversion")

# plot fluency, ext/int in x, model in y
sns.catplot(
    data=data,
    x="Study",
    y="Fluency",
    hue="Model",
    errorbar="ci",
    kind="point",
    hue_order=["Expert", "GPT-3", "STRAP"],
    dodge=True,
    sharex=True,
    sharey=True,
    legend_out=False
).savefig("cross_study_data/plots/cross_study_fluency")
