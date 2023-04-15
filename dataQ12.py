# Data for Q1 and Q2.
# Pre-processed by Jun William Chen.

import pandas as pd
import numpy as np

df = pd.read_csv("WhatsgoodlyData-6.csv")

df.loc[df["Segment Type"] == "University", "Segment Type"] = np.where(
    df[df["Segment Type"] == "University"]["Segment Description"].str.endswith(("High School", "HS")), 
    "High School", "University"
    )

df["Count"] = df["Count"].astype(int)

# Height
df.loc[df["Segment Description"].str.contains("Tall|Medium|Short", regex = True), "Segment Type"] = ["Height"]*len(df[df["Segment Description"].str.contains("Tall|Medium|Short", regex = True)])
df.loc[df["Segment Description"].str.contains("Tall"), "Segment Description"] = ["Tall"]*len(df[df["Segment Description"].str.contains("Tall")])
df.loc[df["Segment Description"].str.contains("Medium"), "Segment Description"] = ["Medium"]*len(df[df["Segment Description"].str.contains("Medium")])
df.loc[df["Segment Description"].str.contains("Short"), "Segment Description"] = ["Short"]*len(df[df["Segment Description"].str.contains("Short")])

# Class
df.loc[df["Segment Description"].str.contains("Upper class|Upper-middle class|Middle / lower-middle class|Poor", regex = True), "Segment Type"] = ["Working Class"]*len(df[df["Segment Description"].str.contains("Upper class|Upper-middle class|Middle / lower-middle class|Poor", regex = True)])
df.loc[df["Segment Description"].str.contains("Upper class"), "Segment Description"] = ["Upper class"]*len(df[df["Segment Description"].str.contains("Upper class")])
df.loc[df["Segment Description"].str.contains("Upper-middle class"), "Segment Description"] = ["Upper-middle class"]*len(df[df["Segment Description"].str.contains("Upper-middle class")])
df.loc[df["Segment Description"].str.contains("Middle / lower-middle class"), "Segment Description"] = ["Middle / lower-middle class"]*len(df[df["Segment Description"].str.contains("Middle / lower-middle class")])
df.loc[df["Segment Description"].str.contains("Poor"), "Segment Description"] = ["Poor"]*len(df[df["Segment Description"].str.contains("Poor")])

# School type
df.loc[df["Segment Description"].str.endswith(("Private", "Public", "No school")), "Segment Type"] = ["School Type"]*len(df[df["Segment Description"].str.endswith(("Private", "Public", "No school"))])
df.loc[df["Segment Description"].str.endswith("Private"), "Segment Description"] = ["Private"]*len(df[df["Segment Description"].str.endswith("Private")])
df.loc[df["Segment Description"].str.endswith("Public"), "Segment Description"] = ["Public"]*len(df[df["Segment Description"].str.endswith("Public")])
df.loc[df["Segment Description"].str.endswith("No school"), "Segment Description"] = ["No school"]*len(df[df["Segment Description"].str.endswith("No school")])

# Ethnicity
df.loc[df["Segment Description"].str.endswith(("Asian", "Other", "White", "Black", "Hispanic", "Native American")), "Segment Type"] = ["Ethnicity"]*len(df[df["Segment Description"].str.endswith(("Asian", "Other", "White", "Black", "Hispanic", "Native American"))])
df.loc[df["Segment Description"].str.endswith("Asian"), "Segment Description"] = ["Asian"]*len(df[df["Segment Description"].str.endswith("Asian")])
df.loc[df["Segment Description"].str.endswith("Other"), "Segment Description"] = ["Other"]*len(df[df["Segment Description"].str.endswith("Other")])
df.loc[df["Segment Description"].str.endswith("Native American"), "Segment Description"] = ["Native American"]*len(df[df["Segment Description"].str.endswith("Native American")])
df.loc[df["Segment Description"].str.endswith("Black"), "Segment Description"] = ["Black"]*len(df[df["Segment Description"].str.endswith("Black")])
df.loc[df["Segment Description"].str.endswith("Hispanic"), "Segment Description"] = ["Hispanic"]*len(df[df["Segment Description"].str.endswith("Hispanic")])
df.loc[df["Segment Description"].str.endswith("White"), "Segment Description"] = ["White"]*len(df[df["Segment Description"].str.endswith("White")])

# Job
df.loc[df["Segment Description"].str.endswith(("Nope, and not looking for one", "Yes, full-time", "No, but I'm searching for one", "Yes, part-time")), "Segment Type"] = ["Employment"]*len(df[df["Segment Description"].str.endswith(("Nope, and not looking for one", "Yes, full-time", "No, but I'm searching for one", "Yes, part-time"))])
df.loc[df["Segment Description"].str.endswith("Nope, and not looking for one"), "Segment Description"] = ["Nope, and not looking for one"]*len(df[df["Segment Description"].str.endswith("Nope, and not looking for one")])
df.loc[df["Segment Description"].str.endswith("Yes, full-time"), "Segment Description"] = ["Yes, full-time"]*len(df[df["Segment Description"].str.endswith("Yes, full-time")])
df.loc[df["Segment Description"].str.endswith("No, but I'm searching for one"), "Segment Description"] = ["No, but I'm searching for one"]*len(df[df["Segment Description"].str.endswith("No, but I'm searching for one")])
df.loc[df["Segment Description"].str.endswith("Yes, part-time"), "Segment Description"] = ["Yes, part-time"]*len(df[df["Segment Description"].str.endswith("Yes, part-time")])

# Data that we are not interested in.
elim = ("games a lot?", "What's your major?", "you vote for?", "Are you?", "Are you a?", "you a feminist?", "Are you single?", "student loan debt?", "you a virgin?", "Sexual orientation?", "in Greek life?", "your zodiac sign?", "grow up speaking?", "are you pursuing?", "do per month?", "What's your leaning?", "I'm in?", "What's your GPA?", "Mac or PC?", "clubs / organizations?", "Graduation Year")

# Get all rows that do not match with what we don't want.
df = df[df["Segment Description"].str.startswith(elim) == False]

df.to_csv("Q12_Data.csv", index = False)
