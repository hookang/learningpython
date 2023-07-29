from PIL import Image
import os

# Function to perform the required operations on each image file
def process_image(file_path, output_folder):
    try:
        # Open the image
        image = Image.open(file_path)

        # Convert the image to RGB mode (removes the alpha channel)
        image = image.convert("RGB")

        # Rotate the image 90° clockwise
        image = image.rotate(-90)

        # Resize the image from 192x192 to 128x128
        image = image.resize((128, 128))

        # Save the image to the output folder in .jpeg format
        output_file = os.path.join(output_folder, os.path.basename(file_path) + ".jpeg")
        image.save(output_file, format="JPEG")
        print(f"Processed: {output_file}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    # Specify the folder with the images to be processed
    input_folder = "/home/student-01-76cf86aa87ad/images"

    # Specify the output folder where processed images will be saved
    output_folder = "/opt/icons"

    # Create the output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each file in the folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            process_image(file_path, output_folder)

if __name__ == "__main__":
    main()
