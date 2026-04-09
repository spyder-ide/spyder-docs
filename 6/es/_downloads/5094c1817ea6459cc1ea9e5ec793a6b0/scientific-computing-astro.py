#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scientific Computing and Visualization with Spyder

Astrological signs and cognitive ability

Created on Thu May 20 10:17:27 2021

@author: Spyder Team
"""

# %% Import the libraries
import scipy.stats as stats
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


# %% Load raw data (csv) and save it in parquet format:
data = pd.read_csv("parsed_data_public.csv", low_memory=False)
data.to_parquet("parsed_data_public.parquet")


# %% Load raw data (parquet)
data = pd.read_parquet("parsed_data_public.parquet")


# %% Let's explore age
print(data.d_age.describe())


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


# %%
g = sns.FacetGrid(data, row="d_astrology_seriosity", col="gender")
g.map(sns.histplot, "d_age")
plt.show()


# %% Demographic variables list
demograph = [v for v in list(data.columns) if v.startswith("d_")]


# %% Cognitive ability questions
# Select the questions for the cognitive ability test (14 questions).
# Add the correct answers in a new column.

test_items = pd.read_csv("test_items.csv")

ca_test = data.copy()  # Make a copy of the original dataframe

right_answers = []
for i, j in test_items.iterrows():
    right_answers.append(j.iloc[j["option_correct"] + 2])
test_items["right_answer"] = right_answers


for i, j in test_items.iterrows():
    q = "q" + str(j["ID"])
    a = str(j["right_answer"])
    try:
        ca_test.dropna(subset=[q], inplace=True)
        ca_test["resp_" + q] = ca_test.apply(lambda row: row[q] == a, axis=1)
    except:
        print(f"{q} not found.")
        pass


# The identification of some answers failed due to formal discrepancies.
# Let's fix it (use debugger?):
ca_test.q18154 = pd.Series(ca_test.q18154, dtype="int")
ca_test.q18154 = pd.Series(ca_test.q18154, dtype="string")
ca_test.resp_q18154 = ca_test.apply(lambda row: row["q18154"] == "26", axis=1)

ca_test.q255 = pd.Series(ca_test.q255, dtype="int")
ca_test.q255 = pd.Series(ca_test.q255, dtype="string")
ca_test.resp_q255 = ca_test.apply(lambda row: row["q255"] == "89547", axis=1)


# %% Sum correct answers
cognitive_score = ca_test[list(ca_test.filter(regex="^resp"))].sum(axis=1)
ca_test["cognitive_score"] = cognitive_score


# %%
print(f"The new lenght of data is {len(ca_test)} rows.")


# %%
print(ca_test.cognitive_score.describe())


# %%
sns.histplot(ca_test.cognitive_score, kde=True, bins=6)


# %%
palette = sns.color_palette("husl")
sns.palplot(palette)


# %% Astrological sign (boxplot)
sns.catplot(x=ca_test.d_astrology_sign, y=ca_test.cognitive_score,
            kind="box", height=5, aspect=2, data=ca_test).set_axis_labels("Zodiac sign", "cognitive score")
sns.set_palette(palette)


# %% Astrological sign (barplot)
fig_dims = (12, 8)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x=ca_test.d_astrology_sign,
            y=ca_test.cognitive_score, ax=ax, data=ca_test)
sns.set_palette(palette)
plt.xlabel("Zodiac sign")
plt.ylabel("cognitive score")


# %% See the figures:
astrology_belief = ca_test.groupby("d_astrology_sign")[
    "cognitive_score"].describe()


# %% ANOVA for astrology sign
astro_cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

astro_pivot = ca_test.pivot(
    columns="d_astrology_sign", values="cognitive_score")
astro_pivot.drop(astro_pivot.columns[0], axis=1, inplace=True)
astro_col_names = list(astro_pivot.columns)
astro_pivot.columns = astro_cols
astro_pivot.dropna(how="all", inplace=True)

# Working, but it needs to be checked:
astro_samples = [astro_pivot[col].dropna() for col in astro_pivot]
astro_fvalue, astro_pvalue = stats.f_oneway(*astro_samples)


num_groups = len(astro_pivot.columns)
num_observations = len(astro_pivot)
dfn = num_groups - 1
dfd = num_observations - num_groups

f_critical = stats.f.ppf(q=0.05, dfn=dfn, dfd=dfd)


# %%
astro_melt = pd.melt(astro_pivot.reset_index(), id_vars=[
                     "index"], value_vars=astro_cols)
astro_melt.columns = ["index", "religiosity", "value"]
sns.boxplot(x="religiosity", y="value", data=astro_melt)
sns.set_palette(palette)
