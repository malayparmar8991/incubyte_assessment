This SQL Script is a common script which should be executed for each and every distinct country present in the customer table.
All distinct country names can be extracted from the customer table using the following command:-
"SELECT DISTINCT(Country) FROM `dbname`.`customer`;"

This is in general tedious because we need to edit the country name before executing the scripts for all the distinct countries of the customers.
An effective solution would be to use MySQL connector with Python to execute the SQL commands iteratively. Please check "Python Script to Create Tables" for this solution.
