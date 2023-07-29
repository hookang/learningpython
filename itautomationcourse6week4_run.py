#!/usr/bin/env python3

import os
import requests

def process_text_files(directory):
    data_list = []
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                # Read the contents of the text file
                lines = file.readlines()
                # Extract information from the text file
                name = lines[0].strip()
                weight = int(lines[1].strip().split()[0])  # Convert weight to an integer
                description = lines[2].strip()
                image_name = os.path.splitext(filename)[0] + '.jpeg'

                # Create a dictionary for each fruit
                fruit_data = {
                    "name": name,
                    "weight": weight,
                    "description": description,
                    "image_name": image_name
                }
                data_list.append(fruit_data)

    return data_list

def upload_data(url, data_list):
    # Upload the data to the specified URL using the POST method
    for data in data_list:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print(f"Uploaded: {data['name']}")

def main():
    # Specify the URL for data upload
    upload_url = "http://34.125.11.84/fruits/"

    # Specify the path to the descriptions directory
    descriptions_directory = os.path.expanduser("~/supplier-data/descriptions")

    # Process the text files and create a list of dictionaries
    data_list = process_text_files(descriptions_directory)

    # Upload the data to the specified URL
    upload_data(upload_url, data_list)

if __name__ == "__main__":
    main()
