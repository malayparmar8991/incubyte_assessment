import mysql.connector

#initializing mysql connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*********",
  database="dbname"
)

#defining cursor to execute commands
mycursor = mydb.cursor()

#fetching all distinct country names
mycursor.execute("SELECT DISTINCT(Country) FROM `dbname`.`customer`;")

myresult = mycursor.fetchall()

#iteratively creating tables for all distinct countries and adding data from the customer table
for x in myresult:
  mycursor.execute('''CREATE TABLE `dbname`.`{}` (
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
  PRIMARY KEY (`Customer Name`));'''.format(x[0]))

  mycursor.execute('''INSERT INTO `dbname`.`{}` (
  `Customer Name`,
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
  `Active Customer`
  FROM `dbname`.customer where Country="{}";'''.format(x[0], x[0]))


#committing the changes
mydb.commit()
