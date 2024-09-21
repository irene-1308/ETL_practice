import requests  # For making HTTP requests to get the web page content
import sqlite3  
import pandas as pd  
from bs4 import BeautifulSoup  # For parsing HTML and extracting data


url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'  # Database file where data will be saved
table_name = 'Top_50'  
csv_path = './webscraping/top_50_films.csv'  # Path where the CSV file will be saved

# Create an empty DataFrame with columns for Average Rank, Film, and Year
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

# Make a request to the URL and retrieve the HTML content of the page
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')
tables = data.find_all('tbody')
rows = tables[0].find_all('tr') # Extract all table rows ('tr' tag) from the first table body

# Loop through each row in the table, extract the top 50 films' data
for row in rows:
    if count < 50: 
        col = row.find_all('td')  
        if len(col) != 0:  
            data_dict = {
                "Average Rank": col[0].contents[0],  
                "Film": col[1].contents[0],  
                "Year": col[2].contents[0] 
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break  

print(df)

df.to_csv(csv_path)
conn = sqlite3.connect(db_name) # Create a connection to the SQLite database

# Write the DataFrame to a table in the SQLite database (if the table already exists, it will be replaced)
df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()
