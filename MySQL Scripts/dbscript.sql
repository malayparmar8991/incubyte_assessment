--Here dbname will be the name of our database and country_name will be the distinct name of country for which we are creating table
--This will create a table with the name of country_name
CREATE TABLE `dbname`.`country_name` (
  `Customer Name` VARCHAR(255) NOT NULL,
  `Customer ID` VARCHAR(18) NOT NULL,
  `Customer Open Date` DATE NOT NULL,
  `Last Consulted Date` DATE NULL,
  `Vaccination Type` CHAR(5) NULL,
  `Doctor Consulted` CHAR(255) NULL,
  `State` CHAR(5) NULL,
  `Post Code` INT(5) NULL,
  `Date of Birth` DATE NULL,
  `Active Customer` CHAR(1) NULL,
  PRIMARY KEY (`Customer Name`));

--This will insert all the customers with Country as country_name in the country_name table
INSERT INTO `dbname`.`country_name`
(`Customer Name`,
  `Customer ID`,
  `Customer Open Date`,
  `Last Consulted Date`,
  `Vaccination Type`,
  `Doctor Consulted`,
  `State`,
  `Post Code`,
  `Date of Birth`,
  `Active Customer`)
  SELECT `Customer Name`,
  `Customer ID`,
  `Customer Open Date`,
  `Last Consulted Date`,
  `Vaccination Type`,
  `Doctor Consulted`,
  `State`,
  `Post Code`,
  `Date of Birth`,
  `Active Customer` FROM `dbname`.`customer` where Country='country_name';
