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
