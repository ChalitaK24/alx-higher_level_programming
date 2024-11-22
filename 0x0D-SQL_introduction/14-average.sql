-- computes the score average of all records
-- in the table second_table of the database hbtn_0c_0 in MySQL server
USE hbtn_0c_0;
SELECT COUNT(*) AS record_count, AVG(score) AS average from second_table;
