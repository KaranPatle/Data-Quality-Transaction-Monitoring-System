-- Total Transactions & Revenue
SELECT COUNT(*) AS total_transactions,
       SUM(Amount) AS total_revenue
FROM transactions;

-- Missing Values
SELECT COUNT(*) 
FROM transactions
WHERE Amount IS NULL;

-- Duplicate Records
SELECT Transaction_ID, COUNT(*)
FROM transactions
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;

-- Revenue by City
SELECT City, SUM(Amount) AS revenue
FROM transactions
GROUP BY City
ORDER BY revenue DESC;


-- Negetive Transactions
SELECT *
FROM transactions
WHERE Amount<0;


--Top Products Category 
SELECT Product_Category, SUM(Amount) as revenue
FROM transactions
GROUP BY Product_Category
ORDER BY revenue DESC;


--Daily Trend
SELECT Transaction_Date, SUM(Amount) AS daily_revenue
FROM transactions
GROUP BY Transaction_Date
ORDER BY Transaction_Date;