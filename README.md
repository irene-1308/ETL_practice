# 🐍 Python Study Projects Overview 🐍

This repository showcases my Python projects during the IBM Data Engineering Professional Certificate course. It contains four folders: one main project (the GDP folder) and three preparation exercises.

## 🌍 GDP Project

This is my primary study project, where I applied all the skills gained from the other tasks.

### Project Brief
An international firm aiming to expand its business globally has hired me as a Junior Data Engineer. My task is to create an automated script that extracts the list of all countries ranked by their GDPs in billion USD (rounded to two decimal places), based on data released by the International Monetary Fund (IMF).

The script needs to:
- Output the data as a JSON file, `Countries_by_GDP.json`.
- Store the data in a SQLite database, `World_Economies.db`, in a table named `Countries_by_GDP` with attributes `Country` and `GDP_USD_billion`.

To demonstrate the script's functionality, I query the database to show entries with economies greater than 100 billion USD. The entire execution process is logged in a file called `etl_project_log.txt`.

## ✅ ETL Project

This project implements an ETL (Extract, Transform, Load) pipeline using Python to handle CSV, JSON, and XML data formats.

Through this task, I gained experience in:
- Using the Pandas library for data extraction and manipulation.
- Extracting data from multiple formats.
- Transforming data by converting height (inches to meters) and weight (pounds to kilograms).
- Using logging to track progress through each stage of the ETL process.

## ✅ Web Scraping and APIs

I developed skills in extracting data from web pages using Python’s web scraping techniques, focusing on the `requests` and `BeautifulSoup` libraries for retrieving and parsing HTML.

By the end of this task, I learned how to:
- Scrape relevant information (e.g., film titles and ranks) from a webpage.
- Structure the scraped data and save it as a CSV file.
- Store the data in a SQLite database for easy querying.

This project significantly enhanced my ability to work with HTML structures and extract useful information.

## ✅ Database Creation and Data Loading

In this task, I learned to create and manage databases using Python's SQLite3 library. 

I used Pandas to read CSV files and load the data into an SQLite database, learning how to:
- Define table attributes and create tables.
- Load data into the database using `to_sql()`, with options to replace existing tables.
- Execute SQL queries to display data, specific columns, and entry counts.

## 👷🏻‍♂️ Installation

Clone the repository:

```bash
git clone <repository_url>
```

Navigate to the project folder:

```bash
cd <folder_name>
```

Before running the projects, ensure that you have the Pandas library installed. You can install it by running the following command:

```bash
python3.12 -m pip install pandas
```
