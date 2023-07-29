#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_data(directory):
    data = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                description = lines[2].strip()
                data.append(f"name: {name}<br/>weight: {weight}<br/><br/>{description}<br/><br/>")
    return "".join(data)

def main():
    # Specify the directory with the description files
    descriptions_directory = os.path.expanduser("~/supplier-data/descriptions")

    # Process the data and create the paragraph for the report
    paragraph = process_data(descriptions_directory)

    # Generate the report and save it as 'processed.pdf' in the /tmp/ directory
    report_file = "/tmp/processed.pdf"
    title = f"Processed Update on {datetime.date.today()}"
    reports.generate_report(report_file, title, paragraph)

    # Send the email with the PDF report as an attachment
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    sender = "automation@example.com"
    recipient = "student-01-79c6ce800f3c@example.com"  # Replace 'username' with the actual recipient's email address
    emails.send_email(sender, recipient, subject, body, attachment_path=report_file)

if __name__ == "__main__":
    main()
