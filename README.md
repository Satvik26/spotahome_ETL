# Spotahome Data Pipeline using Airflow

This is a spotahome ETL data pipeline which aims to gather data about the different types of renting properties available in Milan in the spotahome website.

Spotahome Website:

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/spotahome%20website.png)

## Architecture

1. The data is gathered from the website using webscraping and then stored in Amazon S3 in CSV format.
2. Libraries used are as follows : bs4, requests, s3fs, pandas, airflow.
3. The orchestration of the project is done using Airflow.
4. The Python and airflow code are hosted in the EC2 instance

## Technology Used

-> Programming language : Python

-> AWS
  1. EC2
  2. S3
  3. IAM
 
Connection established with the EC2 instance using ssh

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/Screenshot%202023-03-17%20at%2019.23.29.png)

The libraries required in the project such airflow, virtual environment, python are also installed in the EC2 instance.

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/Screenshot%202023-03-17%20at%2019.23.10.png)

The commands used for installing all the libraries are as follows:
```diff
sudo apt-get update

sudo apt install python3-pip

sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate

sudo pip install apache-airflow

sudo pip install pandas

sudo pip install s3fs

sudo pip install bs4

sudo pip install requests

airflow    -> For checking if the airflow is installed or not

airflow standalone  -> For start running the airflow server
```

The Data is gathered from the website and then stored in Amazon S3 in CSV format. The orchestration of the project is performed using Airflow.

The below images are of the successful running of the dag and upload of the csv file in the S3 Bucket

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/Screenshot%202023-03-17%20at%2019.48.42.png)

The Test1.csv File can be seen in the below S3 bucket image:

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/Screenshot%202023-03-17%20at%2019.50.50.png)

The Csv file:

![alt text](https://github.com/Satvik26/spotahome_ETL/blob/main/Images/Test1.png)


