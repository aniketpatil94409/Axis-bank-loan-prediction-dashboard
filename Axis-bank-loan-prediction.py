# Axis Bank Loan Prediction Project 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load Dataset
df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\Project Analysis\\Axis_bank_loan_prediction\\Axis_bank_loan_prediction.csv")

# Preview Data
print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------
# 1. Total Number of Loan Records
print("\nTotal loan records:", len(df))

# ------------------------------
# 2. Average Loan Amount by Loan Status
avg_loan_by_status = df.groupby("loan_status")["loan_amount"].mean()
print("\nAverage Loan Amount by Loan Status:")
print(avg_loan_by_status)

# ------------------------------
# 3. Top 10 Customers with Highest EMI
top_10_emi = df[["customer_id", "customer_name", "emi"]].sort_values(by="emi", ascending=False).head(10)
print("\nTop 10 Customers with Highest EMI:")
print(top_10_emi)

# ------------------------------
# 4. Count Customers by Loan Status
loan_status_count = df["loan_status"].value_counts()
print("\nCustomer Count by Loan Status:")
print(loan_status_count)

# Bar plot: Count of loan status
sns.countplot(data=df, x="loan_status", palette="Set2")
plt.title("Loan Status Distribution")
plt.show()

# ------------------------------
# 5. Defaulted Customers from Urban Area
urban_defaults = df[(df["property_area"] == "Urban") & (df["loan_status"] == "Defaulted")]
print("\nDefaulted Customers from Urban Area:")
print(urban_defaults[["customer_id", "customer_name", "property_area", "loan_status"]])

# ------------------------------
# 6. Average Income by Education
avg_income_edu = df.groupby("education")["income"].mean()
print("\nAverage Income by Education Level:")
print(avg_income_edu)

# Bar plot: Average income by education
avg_income_edu.plot(kind='bar', color='skyblue')
plt.title("Average Income by Education")
plt.ylabel("Income")
plt.xlabel("Education Level")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# 7. Count Loans by Property Area
loans_by_area = df["property_area"].value_counts()
print("\nLoan Count by Property Area:")
print(loans_by_area)

# Pie chart: Loan count by property area
loans_by_area.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title("Loan Distribution by Property Area")
plt.ylabel("")
plt.show()

# ------------------------------
# 8. Pairs of Customers with Same Credit Score
credit_score_pairs = df.merge(df, on='credit_score')
credit_score_pairs = credit_score_pairs[credit_score_pairs['customer_id_x'] < credit_score_pairs['customer_id_y']]
print("\nPairs of Customers with Same Credit Score:")
print(credit_score_pairs[["customer_id_x", "customer_id_y", "credit_score"]])
