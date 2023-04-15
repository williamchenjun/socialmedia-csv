# Data for Q3.
# Pre-processed by Jun William Chen.

import pandas as pd

df = pd.read_csv("WhatsgoodlyData-6.csv")

data = df[
        (df["Segment Type"] == "Custom") 
       & (df["Segment Description"].str
          .contains("What's your major?|I'm in?|are you pursuing?|What's your GPA?|Graduation Year|student loan debt|or private school|your parents make"))
       ]

unis = df[(df["Segment Type"] == "University") & (~df["Segment Description"].str.endswith(("High School", "HS")))]

data = data.append(unis, ignore_index = True)
data = data.append(df[df["Segment Description"].str.endswith(("High School", "HS"))], ignore_index = True)

data.loc[data["Segment Description"].str.endswith(("High School", "HS")), "Segment Type"] = ["High School"]*len(data.loc[data["Segment Description"].str.endswith(("High School", "HS")), "Segment Description"])

data[data["Segment Description"].str.contains("GPA")] = data[data["Segment Description"].str.contains("GPA")].astype(str).apply(lambda x: x.str.encode("ascii", "ignore").str.decode("ascii"))
data[data["Segment Description"].str.contains("your parents make")] = data[data["Segment Description"].str.contains("your parents make")].astype(str).apply(lambda x: x.str.encode("ascii", "ignore").str.decode("ascii"))

# Removing unnecessary string

cat_names = ("School Type", "Working Class", "Major", "Student Loan Debt", "Career Pursue", "GPA", "Graduation Year")

# School type reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.endswith(("Private", "Public", "No school")), "Segment Type"] = ["School Type"]*len(data.loc[data["Segment Description"].str.endswith(("Private", "Public", "No school")), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("Private"), "Segment Description"] = ["Private"]*len(data.loc[data["Segment Description"].str.endswith("Private"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Public"), "Segment Description"] = ["Public"]*len(data.loc[data["Segment Description"].str.endswith("Public"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("No school"), "Segment Description"] = ["No school"]*len(data.loc[data["Segment Description"].str.endswith("No school"), "Segment Description"])

# Working class reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.endswith(("(> $240K)", "(~$160K", "(~$90K)", "(< ~$50K) ")), "Segment Type"] = ["Working Class"]*len(data.loc[data["Segment Description"].str.endswith(("(> $240K)", "(~$160K", "(~$90K)", "(< ~$50K) ")), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("(> $240K)"), "Segment Description"] = ["Upper class"]*len(data.loc[data["Segment Description"].str.endswith("(> $240K)"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("(~$160K"), "Segment Description"] = ["Upper-middle class"]*len(data.loc[data["Segment Description"].str.endswith("(~$160K"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("(~$90K)"), "Segment Description"] = ["Middle / lower-middle class"]*len(data.loc[data["Segment Description"].str.endswith("(~$90K)"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("(< ~$50K) "), "Segment Description"] = ["Poor"]*len(data.loc[data["Segment Description"].str.endswith("(< ~$50K) "), "Segment Description"])

# Major reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("What's your major?"), "Segment Type"] = ["Major"]*len(data.loc[data["Segment Description"].str.startswith("What's your major?"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("ME/EE/other engineer"), "Segment Description"] = ["ME/EE/other engineer"]*len(data.loc[data["Segment Description"].str.endswith("ME/EE/other engineer"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Business/Econ/Finance"), "Segment Description"] = ["Business/Econ/Finance"]*len(data.loc[data["Segment Description"].str.endswith("Business/Econ/Finance"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Pre-med"), "Segment Description"] = ["Pre-med"]*len(data.loc[data["Segment Description"].str.endswith("Pre-med"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Comm / marketing"), "Segment Description"] = ["Comm / marketing"]*len(data.loc[data["Segment Description"].str.endswith("Comm / marketing"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Languages"), "Segment Description"] = ["Languages"]*len(data.loc[data["Segment Description"].str.endswith("Languages"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Visual/performing arts"), "Segment Description"] = ["Visual/performing arts"]*len(data.loc[data["Segment Description"].str.endswith("Visual/performing arts"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("History"), "Segment Description"] = ["History"]*len(data.loc[data["Segment Description"].str.endswith("History"), "Segment Description"])
data.loc[data["Segment Description"] == "What's your major? Other", "Segment Description"] = ["Other (Major)"]*len(data.loc[data["Segment Description"] == "What's your major? Other", "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Comp sci"), "Segment Description"] = ["Comp sci"]*len(data.loc[data["Segment Description"].str.endswith("Comp sci"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Political science / philosophy"), "Segment Description"] = ["Political science / philosophy"]*len(data.loc[data["Segment Description"].str.endswith("Political science / philosophy"), "Segment Description"])

# Student Loan Debt reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("student loan debt?"), "Segment Type"] = ["Student Loan Debt"]*len(data.loc[data["Segment Description"].str.startswith("student loan debt?"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("student loan debt? No"), "Segment Description"] = ["No"]*len(data.loc[data["Segment Description"].str.endswith("student loan debt? No"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("student loan debt? Yes"), "Segment Description"] = ["Yes"]*len(data.loc[data["Segment Description"].str.endswith("student loan debt? Yes"), "Segment Description"])

# Career Pursue reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("are you pursuing?"), "Segment Type"] = ["Career Pursue"]*len(data.loc[data["Segment Description"].str.startswith("are you pursuing?"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("are you pursuing? Undecided"), "Segment Description"] = ["Undecided"]*len(data.loc[data["Segment Description"].str.endswith("are you pursuing? Undecided"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("are you pursuing? Humanities"), "Segment Description"] = ["Humanities"]*len(data.loc[data["Segment Description"].str.endswith("are you pursuing? Humanities"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("are you pursuing? Technical / engineering"), "Segment Description"] = ["Technical / engineering"]*len(data.loc[data["Segment Description"].str.endswith("are you pursuing? Technical / engineering"), "Segment Description"])

# GPA reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("What's your GPA?"), "Segment Type"] = ["GPA"]*len(data.loc[data["Segment Description"].str.startswith("What's your GPA?"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("What's your GPA? 1.0 to 2.0"), "Segment Description"] = ["1.0 to 2.0"]*len(data.loc[data["Segment Description"].str.endswith("What's your GPA? 1.0 to 2.0"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("What's your GPA? 2.0 to 3.0"), "Segment Description"] = ["2.0 to 3.0"]*len(data.loc[data["Segment Description"].str.endswith("What's your GPA? 2.0 to 3.0"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("What's your GPA? 3.0 to 4.0"), "Segment Description"] = ["3.0 to 4.0"]*len(data.loc[data["Segment Description"].str.endswith("What's your GPA? 3.0 to 4.0"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("What's your GPA? Below 1.0 "), "Segment Description"] = ["Below 1.0"]*len(data.loc[data["Segment Description"].str.endswith("What's your GPA? Below 1.0 "), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("What's your GPA? Above 4.0 "), "Segment Description"] = ["Above 4.0"]*len(data.loc[data["Segment Description"].str.endswith("What's your GPA? Above 4.0 "), "Segment Description"])

# Education Level reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("I'm in?"), "Segment Type"] = ["Education Level"]*len(data.loc[data["Segment Description"].str.startswith("I'm in?"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("I'm in? Post-grad"), "Segment Description"] = ["Post-grad"]*len(data.loc[data["Segment Description"].str.endswith("I'm in? Post-grad"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("I'm in? Other"), "Segment Description"] = ["Other (Education Level)"]*len(data.loc[data["Segment Description"].str.endswith("I'm in? Other"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("I'm in? Grad School"), "Segment Description"] = ["Grad School"]*len(data.loc[data["Segment Description"].str.endswith("I'm in? Grad School"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("I'm in? College"), "Segment Description"] = ["College"]*len(data.loc[data["Segment Description"].str.endswith("I'm in? College"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("I'm in? High School"), "Segment Description"] = ["High School"]*len(data.loc[data["Segment Description"].str.endswith("I'm in? High School"), "Segment Description"])

# Education Level reformat.
# Change segment type name.
data.loc[data["Segment Description"].str.startswith("Graduation Year"), "Segment Type"] = ["Graduation Year"]*len(data.loc[data["Segment Description"].str.startswith("Graduation Year"), "Segment Description"])

data.loc[data["Segment Description"].str.endswith("Graduation Year 2017"), "Segment Description"] = ["2017"]*len(data.loc[data["Segment Description"].str.endswith("Graduation Year 2017"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Graduation Year 2018"), "Segment Description"] = ["2018"]*len(data.loc[data["Segment Description"].str.endswith("Graduation Year 2018"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Graduation Year 2019"), "Segment Description"] = ["2019"]*len(data.loc[data["Segment Description"].str.endswith("Graduation Year 2019"), "Segment Description"])
data.loc[data["Segment Description"].str.endswith("Graduation Year 2020"), "Segment Description"] = ["2020"]*len(data.loc[data["Segment Description"].str.endswith("Graduation Year 2020"), "Segment Description"])

data["Count"] = data["Count"].astype(int)

data.to_csv("Q3_Data.csv", index = False)