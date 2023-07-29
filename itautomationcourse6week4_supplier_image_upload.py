#!/usr/bin/env python3

from PIL import Image
import os

def is_image_file(filename):
    """Check if the file is an image based on the extension."""
    valid_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.tiff']
    return any(filename.lower().endswith(ext) for ext in valid_extensions)

def process_images(directory):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and is_image_file(filename):
            # Open the image
            image = Image.open(file_path)

            # Convert RGBA to RGB format
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Resize the image to 600x400 pixels
            image = image.resize((600, 400))

            # Save the image with JPEG format
            output_file = os.path.splitext(file_path)[0] + '.jpeg'
            image.save(output_file, format='JPEG')
            print(f"Processed: {output_file}")

def main():
    # Specify the path to the images directory
    images_directory = os.path.expanduser("~/supplier-data/images")

    # Process the images in the specified directory
    process_images(images_directory)

if __name__ == "__main__":
    main()

student-01-79c6ce800f3c@linux-instance:~$ cat supplier_image_upload.py
#!/usr/bin/env python3

import requests
import os

def upload_images(url, image_directory):
    # Iterate through each file in the image directory
    for filename in os.listdir(image_directory):
        file_path = os.path.join(image_directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as opened:
                files = {'file': opened}
                response = requests.post(url, files=files)
                response.raise_for_status()
                print(f"Uploaded: {filename}")

def main():
    # Specify the URL for image upload
    upload_url = "http://localhost/upload/"

    # Specify the path to the images directory
    image_directory = os.path.expanduser("~/supplier-data/images")

    # Upload the images to the specified URL
    upload_images(upload_url, image_directory)

if __name__ == "__main__":
    main()
