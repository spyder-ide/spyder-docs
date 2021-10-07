#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scientific Computing and Visualization with Spyder

Created on Thu May 20 10:17:27 2021

@author: Spyder Team
"""

# %% Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns


# %% Load raw data (parquet)
data = pd.read_parquet("parsed_data_public.parquet")


# %% Let's explore age
print(data.d_age.describe())

age = data.d_age.tolist()


# %% Save some variables and display them in the Variable Explorer
max_age = data.d_age.min()
min_age = data.d_age.max()


# %% Plot age with pandas
data.d_age.plot.hist(bins=25, alpha=0.5)


# %% Plot age with seaborn (and search for help from IPython Console)
sns.histplot(data.d_age, kde=True, bins=25)
plt.show()


# %% Plot age and mean
sns.histplot(data.d_age, kde=True, bins=25)
plt.xlabel('Age')
plt.axvline(data.d_age.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(data.d_age.mean()*1.1, max_ylim*0.9,
         'Mean: {:.2f}'.format(data.d_age.mean()))
plt.show()


# %% Demographic variables list
demograph = [v for v in list(data.columns) if v.startswith("d_")]


# %% Cognitive ability questions
# Select the questions for the cognitive ability test (14 questions).
# Add the correct answers in a new column.

test_items = pd.read_csv("test_items.csv")

ca_test = data.copy()  # Make a copy of the original dataframe

right_answers = []
for ID, ROW in test_items.iterrows():
    right_answers.append(ROW.iloc[ROW["option_correct"] + 2])
test_items["right_answer"] = right_answers


for ID, ROW in test_items.iterrows():
    QUESTION = "q" + str(ROW["ID"])
    ANSWER = str(ROW["right_answer"])
    try:
        ca_test.dropna(subset=[QUESTION], inplace=True)
        ca_test["resp_" + QUESTION] = ca_test.apply(lambda row: row[QUESTION] == ANSWER, axis=1)
    except KeyError:
        print(f"{QUESTION} not found.")


# The identification of some answers failed due to formal discrepancies.
ca_test.q18154 = pd.Series(ca_test.q18154, dtype="int")
ca_test.q18154 = pd.Series(ca_test.q18154, dtype="string")
ca_test.resp_q18154 = ca_test.apply(lambda row: row["q18154"] == "26", axis=1)

ca_test.q255 = pd.Series(ca_test.q255, dtype="int")
ca_test.q255 = pd.Series(ca_test.q255, dtype="string")
ca_test.resp_q255 = ca_test.apply(lambda row: row["q255"] == "89547", axis=1)


# %% Sum correct answers
cognitive_score = ca_test[list(ca_test.filter(regex="^resp"))].sum(axis=1)
ca_test["cognitive_score"] = cognitive_score


# %% Print the new lenght of data
print(f"The new lenght of data is {len(ca_test)} rows.")


# %% Show summary of data
print(ca_test.cognitive_score.describe())


# %%
sns.histplot(ca_test.cognitive_score, kde=True, bins=6)


# %%
palette = sns.color_palette("husl")
sns.palplot(palette)


# %% q997 = Are you a cat person or a dog person? (boxplot)
sns.catplot(x=ca_test.q997, y=ca_test.cognitive_score,
            kind="box", height=5, aspect=2,
            data=ca_test).set_axis_labels(
                "q997 = Are you a cat person or a dog person?", "cognitive score")
sns.set_palette(palette)


# %% q997 = Are you a cat person or a dog person? (barplot)
fig_dims = (12, 8)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x=ca_test.q997, y=ca_test.cognitive_score, ax=ax, data=ca_test)
sns.set_palette(palette)
plt.xlabel("q997 = Are you a cat person or a dog person?")
plt.ylabel("cognitive score")


# %% See the figures:
dog_or_cat = ca_test.groupby("q997")["cognitive_score"].describe()


# %% ANOVA for dog or cat preferences
dog_or_cat_pivot = ca_test.pivot(columns="q997", values="cognitive_score")
dog_or_cat_pivot.drop(dog_or_cat_pivot.columns[0], axis=1, inplace=True)

dog_or_cat_col_names = list(dog_or_cat_pivot.columns)
dog_or_cat_pivot.columns = ["A", "B", "C", "D"]
dog_or_cat_pivot.dropna(how="all", inplace=True)

dog_or_cat_samples = [dog_or_cat_pivot[col].dropna() for col in dog_or_cat_pivot]
f_value, p_value = stats.f_oneway(*dog_or_cat_samples)


num_groups = len(dog_or_cat_pivot.columns)
num_observations = len(dog_or_cat_pivot)
dfn = num_groups - 1
dfd = num_observations - num_groups

f_critical = stats.f.ppf(q=0.95, dfn=dfn, dfd=dfd)
