import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"


# Extract data from CSV
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe


# Extract data from JSON
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


# Extract data from XML
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name": name, "height": height, "weight": weight}])],
                              ignore_index=True)
    return dataframe


# Extract all data from CSV, JSON, and XML files
def extract():
    extracted_data = pd.DataFrame(
        columns=['name', 'height', 'weight'])  # Create an empty DataFrame to hold extracted data

    # Process all CSV files
    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, extract_from_csv(csvfile)], ignore_index=True)

        # Process all JSON files
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, extract_from_json(jsonfile)], ignore_index=True)

        # Process all XML files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, extract_from_xml(xmlfile)], ignore_index=True)

    return extracted_data


# Transform the data (convert inches to meters and pounds to kilograms)
def transform(data):
    '''Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters '''
    data['height'] = round(data['height'] * 0.0254, 2)

    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data['weight'] * 0.45359237, 2)

    return data


# Log the progress of the ETL job
def log_progress(message):
    timestamp_format = '%Y-%b-%d %H:%M:%S' 
    now = datetime.now()  # Get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')

# Define the load function to save the transformed data into a CSV file
def load_data(target_file, data):
    data.to_csv(target_file, index=False)


# ETL Process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data = extract()

# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")