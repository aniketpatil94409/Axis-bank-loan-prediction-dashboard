#  Axis Bank Loan Default Prediction Project

This project analyzes Axis Bank's loan customer data to explore trends in loan defaults using SQL, Power BI, and Python (with pandas, matplotlib, seaborn).
## Project Overview

The goal of this project is to explore and analyze Axis Bank's loan customer data to identify trends, patterns, and potential risk factors related to loan default. 

Using **SQL**, **Power BI**, and **Python**, we examine various factors like income, EMI, credit score, education, and property area to understand their impact on loan repayment behavior.

This project demonstrates:
- SQL for structured data querying  
- Power BI for interactive visual dashboards  
- Python for detailed data exploration and visualization  

---
## Dataset Information
The dataset contains structured loan information including:

- `customer_id`: Unique identifier for customers  
- `customer_name`: Name of the customer  
- `income`: Monthly income  
- `loan_amount`: Loan amount requested  
- `emi`: Monthly installment  
- `credit_score`: Customer's credit score  
- `education`: Education level  
- `property_area`: Urban, Rural, Semiurban  
- `loan_status`: `Fully Paid` or `Defaulted`  

---
## SQL Insights
1. **Total Loan Records**  
   - Used `COUNT(*)` to get total number of entries.

2. **Average Loan Amount by Loan Status**  
   - Compared loan amounts for `Defaulted` vs `Fully Paid`.

3. **Top 10 Customers with Highest EMI**  
   - Sorted and limited top EMI values.

4. **Customer Count by Loan Status**  
   - Counted how many customers defaulted or paid.

5. **Urban Area Defaulters**  
   - Filtered for customers from `Urban` areas who defaulted.

6. **Average Income by Education**  
   - Grouped by education to find income patterns.

7. **Loan Count by Property Area**  
   - Distribution of loans across `Urban`, `Rural`, `Semiurban`.

8. **Same Credit Score Pairs**  
   - Paired customers with same credit scores using self-join.

---

## Power BI Dashboard
Created interactive visualizations to show:
---

### Page 1: Loan Status Overview
- **Bar Chart:** Fully Paid vs Defaulted loan count
- **KPI Cards:** Total loans, Total defaults, Default rate (%)
- **Pie Chart:** Visual proportion of loan status

**Insight:** Quickly understand overall loan performance and identify default trends.

---

### Page 2: EMI & High-Risk Customers
- **Table:** Top 10 customers with highest EMI
- **(Optional) Scatter Plot:** EMI vs Income
- **Slicers:** Filter by loan status, area, education

**Insight:** Spot high EMI customers, assess repayment stress, and flag potential risk.

---

### Page 3: Demographics & Loan Patterns
- **Bar Chart:** Loan count by property area
- **Bar Chart:** Avg income by education
- **Slicers:** Credit score, education, area, loan status

**Insight:** Analyze regional default patterns and understand income trends

## Python EDA:
- Cleaned and explored dataset using pandas
- Visualized relationships and group statistics
- Identified outliers and patterns in income, EMI, education, and area

---

## How to Use This Project
Requirements:

Python 3.12+

VS Code or Jupyter Notebook

MySQL or compatible RDBMS

Power BI Desktop (free)


## Conclusion
-Building predictive models to flag potential defaulters

-Automating dashboard refresh with live data

-Enhancing visuals with interactivity and advanced metrics

