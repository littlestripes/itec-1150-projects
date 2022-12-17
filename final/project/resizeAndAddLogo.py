#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os  # listdir()
import re  # search(), compile()
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# to be used by is_image() to determine whether or not the filename
# passed in is an image file
image_filename_regex = re.compile(
        r"^[a-zA-Z0-9]+\.(bmp)|(gif)|(jpg)|(png)$", flags=re.I
)

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)


def is_image(filename) -> bool:
    """
    Returns True if the filename meets the criteria to be an image.
    """
    if image_filename_regex.search(filename) is not None:
        return True

    return False


# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not is_image(filename) or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size

    # check if dimensions of image are big enough to accommodate the logo
    if width < (logoWidth * 2) or height < (logoHeight * 2):
        continue

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
