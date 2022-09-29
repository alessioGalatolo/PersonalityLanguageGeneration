import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("text_study_data/data4jasp.csv")

sns.set_theme()
sns.set_style("whitegrid")
sns.set_palette("colorblind")
sns.set_context("talk")

# plot extraversion, different graph by dialogue, ext/int in x, model in y
sns.catplot(
    data=data,
    x="Personality condition",
    y="Extraversion",
    hue="Model",
    order=["Ext", "Int"],
    hue_order=["Expert", "GPT-3", "STRAP"],
    col="Dialogue",
    errorbar="ci",
    kind="point",
    dodge=True,
    sharex=True,
    sharey=True
).savefig("text_study_data/plots/text_study_extraversion")

dummy_row = data.iloc[0].to_dict()
dummy_row["Fluency"] = 0.0
row1 = dummy_row.copy()
row1["Model"] = "GPT-3"
row2 = dummy_row.copy()
row2["Model"] = "Expert"
row3 = dummy_row.copy()
row3["Model"] = "STRAP"


fig, ax = plt.subplots()
ax.set_ylim(0, 6)
ax.set_yticks(range(0, 7))
sns.set_context("notebook")

# violin fluency across all dialgoues by model
sns.violinplot(
    data=pd.concat([
        data,  # add dummy data for more beautiful violin plot
        pd.DataFrame([row1, row2, row3])
    ]),
    x="Model",
    y="Fluency",
    order=["Expert", "GPT-3", "STRAP"],
    cut=0,
    inner="box",
    ax=ax
)

plt.savefig("text_study_data/plots/text_study_fluency")
