CREATE DATABASE IF not EXISTS CREDIT;
use CREDIT;
CREATE TABLE credit_card (
	ID varchar(100)  Not null primary key,
    LIMIT_BAL varchar(100) Not null,
    SEX varchar(100) Not null,
    EDUCATION varchar(100) Not null,
    MARRIAGE varchar(100) Not null,
    AGE varchar(100) Not null,
    PAY_0 varchar(100) Not null,
    PAY_2 varchar(100) Not null,
    PAY_3 varchar(100) Not null,
    PAY_4 varchar(100) Not null,
    PAY_5 varchar(100) Not null,
    PAY_6 varchar(100) Not null,
    BILL_AMT1 varchar(100) Not null,
    BILL_AMT2 varchar(100) Not null,
    BILL_AMT3 varchar(100) Not null,
    BILL_AMT4 varchar(100) Not null,
    BILL_AMT5 varchar(100) Not null,
    BILL_AMT6 varchar(100) Not null,
    PAY_AMT1 varchar(100) Not null,
    PAY_AMT2 varchar(100) Not null,
    PAY_AMT3 varchar(100) Not null,
    PAY_AMT4 varchar(100) Not null,
    PAY_AMT5 varchar(100) Not null,
    PAY_AMT6 varchar(100) Not null,
    default_payment varchar(100) Not null);
 

LOAD DATA LOCAL INFILE 'C:/Users/yaomu/Desktop/DA/Proejct/Credit_Card.csv' 
INTO TABLE credit_card
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
    
SELECT * FROM credit_card
ORDER BY ID ASC;
