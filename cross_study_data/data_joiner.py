import pandas as pd

video_study_data = pd.read_csv("video_study_data/data4jasp.csv")
text_study_data = pd.read_csv("text_study_data/data4jasp.csv")

text_study_data = text_study_data[text_study_data["Dialogue"] == 1][[
    "Age",
    "Gender",
    "English",
    "Model",
    "Personality condition",
    "Condition",
    "Extraversion",
    "Fluency"
    ]]
text_study_data.insert(0, column="Study", value="Text")
video_study_data = video_study_data[[
    "Age",
    "Gender",
    "English",
    "Model",
    "Personality condition",
    "Condition",
    "Extraversion",
    "Fluency"
    ]]
video_study_data.insert(0, column="Study", value="Video")

all = pd.concat([text_study_data, video_study_data], ignore_index=True)

for index, row in all.iterrows():
    all.loc[index, ('Condition')] = f"{row['Model']} {row['Personality condition']} {row['Study']}"

all.to_csv("./cross_study_data/data4jasp.csv", index=False)
