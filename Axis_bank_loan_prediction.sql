CREATE DATABASE loan_default_project;
USE loan_default_project;

select * from loan_data limit 10;

#1.Count total number of loan records
create view total_loan_records as
SELECT COUNT(*) AS total_loans
FROM loan_data;

select * from total_loan_records;


#2.Average loan amount by loan status
create view avg_loan_status as
SELECT loan_status, AVG(loan_amount) AS avg_loan_amount
FROM loan_data
GROUP BY loan_status;

select * from avg_loan_status;


#3. Get top 10 customers with highest EMI
create view top_10_cust_emi as
SELECT customer_id, customer_name, emi
FROM loan_data
ORDER BY emi DESC
LIMIT 10;

select * from top_10_cust_emi;


#4.Count how many customers defaulted vs fully paid
create view count_customers as
SELECT loan_status, COUNT(*) AS total_customers
FROM loan_data
GROUP BY loan_status;

select * from count_customers;


#5.List customers from Urban areas who defaulted
create view defaulted_cust_frm_urban as
SELECT customer_id, customer_name, property_area, loan_status
FROM loan_data
WHERE property_area = 'Urban' AND loan_status = 'Defaulted';

select * from defaulted_cust_frm_urban;


#6.Average income of customers by education level
create view avg_income_cust as
SELECT education, AVG(income) AS average_income
FROM loan_data
GROUP BY education;

select * from avg_income_cust;


#7.Count loans by property area
create view loans_by_property_area as
SELECT property_area, COUNT(*) AS total_loans
FROM loan_data
GROUP BY property_area
ORDER BY total_loans DESC;

select * from loans_by_property_area;


#8. Find pairs of customers who have the same credit score
create view cust_with_same_credit_score as
SELECT A.customer_id AS customer_1, 
B.customer_id AS customer_2, 
A.credit_score
FROM loan_data A
JOIN loan_data B ON A.credit_score = B.credit_score 
AND A.customer_id < B.customer_id
ORDER BY A.credit_score;

select * from cust_with_same_credit_score;




