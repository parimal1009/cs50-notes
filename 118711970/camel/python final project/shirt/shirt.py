import sys
import os
from PIL import Image, ImageOps

def resize_crop_overlay_shirt(input_path, output_path):
    # Check if the input file exists
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    # Open the input image
    input_image = Image.open(input_path)

    # Open the shirt image
    shirt_image = Image.open('shirt.png')

    # Resize and crop the input image to match the dimensions of the shirt image
    resized_input = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt image on the resized input image
    resized_input.paste(shirt_image, (0, 0), shirt_image)

    # Save the result as the output image
    resized_input.save(output_path)

    # Exit with exit code 0 upon successful execution
    sys.exit(0)

if __name__ == "__main__":
    # Get input and output paths from command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Perform resizing, cropping, and overlaying of the shirt
    resize_crop_overlay_shirt(input_path, output_path)
