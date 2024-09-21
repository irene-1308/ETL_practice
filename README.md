# Introduction

This repo is a documentation of my studies of Python during IBM Data Engineering Professional Certificate course. There are 4 folders in this repo - one with a course project (Project folder) and three with preparation exercises. 

### Project


### ETL

This project implements an ETL (Extract, Transform, Load) process using Python to handle CSV, JSON, and XML data formats.

Through this task, I learned how to:
- Use the pandas library for data manipulation and extraction.
- Implement functions to extract data from various file formats.
- Transform data by converting height from inches to meters and weight from pounds to kilograms.
- Utilise logging to track the progress of each ETL phase effectively.

### Web Scraping and APIs

I learned to extract data from web pages using Python through web scraping. The main objectives included utilising the `requests` and `BeautifulSoup` libraries to retrieve and analyse HTML code.

By the end of this exercise, I learnt how to:
- Scrape relevant information (e.g. average rank or film title) from a specified webpage.
- Organise the extracted data into a structured format and save it in a CSV file.
- Store the same data in a SQLite database.

This experience enhanced my understanding of web scraping techniques and improved my ability to handle HTML data structures for information extraction.

### Database Creation and Data Loading 

I learned how to create a database using Python and the SQLite3 library, which is embedded in Python. 

I used Pandas to read the CSV file and load the data into the SQLite database. The essential steps involved:
- Defining table attributes and creating the table.
- Loading data using `to_sql()`, ensuring that existing tables were replaced if necessary.
- Executing SQL queries to view all data, specific columns, and count entries.

## Installation

Clone the repository:
bash
‘’’ git clone <repository_url>

Navigate to the folder:
bash
‘’’ cd *folder name*

Before running any of the folders,, ensure you have the pandas library installed. Execute the following command in your terminal:
bash
‘’’ python3.12 -m pip install pandas
