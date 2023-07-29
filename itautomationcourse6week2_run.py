#!/usr/bin/env python3

import os
import requests

def read_feedback_files(directory):
    feedback_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                feedback_data = file.read()
                feedback_list.append(feedback_data)
    return feedback_list

def main():
    # Replace 'corpweb-external-IP' with the actual external IP address of the company's website
    url = 'http://34.69.27.237/feedback/'
    feedback_directory = '/data/feedback'

    # Get a list of feedback data from text files in the directory
    feedback_list = read_feedback_files(feedback_directory)

    for feedback in feedback_list:
        # Create a dictionary with 'title', 'name', 'date', and 'feedback' keys
        feedback_dict = {
            'title': 'Feedback',
            'name': 'Anonymous',
            'date': '2023-07-28',
            'feedback': feedback
        }

        # Send the dictionary as a POST request to the company's website
        response = requests.post(url, json=feedback_dict)

        # Check if the request was successful (status code 201)
        if response.status_code == 201:
            print("Feedback sent successfully!")
        else:
            print(f"Error sending feedback: Status code {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    main()
