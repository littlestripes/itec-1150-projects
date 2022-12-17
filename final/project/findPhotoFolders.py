"""
Program Name: findPhotoFolders.py
Author: Val Kamali
Email: val.kamali@go.minnstate.edu
Description:
    Locates folders that contain photos on the hard drive and prints their
    absolute paths to standard output.
Dates: 2022-12-16 - File created.
"""

import os              # walk(), name
import pathlib         # Path
import re              # compile(), search()
import datetime        # datetime
from PIL import Image  # open(), size

PHOTO_HEIGHT, PHOTO_WIDTH = 500, 500


def is_image(filename) -> bool:
    """
    Returns True if the filename meets the criteria to be an image.

    :param filename: string, the filename to be examined
    """
    image_filename_regex = re.compile(
            r"^[a-zA-Z0-9]+\.(bmp)|(jpg)|(png)$", flags=re.I
    )

    if image_filename_regex.search(filename) is not None:
        return True

    return False


def write_to_errlog(filename: str):
    """
    Writes to the error log. Error log is named with this format:
        `errlog-{date}.txt`
    """
    dt = datetime.date.today()
    with open(f"error_log-{dt}.txt", "a") as errlog:
        errlog.writelines(f"Bad image: {filename}\n")


def main():
    # first, the root directory depends on if this is running on a POSIX
    # system (mac, linux, solaris, other advanced operating systems) or NT
    if os.name == "posix":
        root = pathlib.Path("/")
    else:
        root = pathlib.Path("C:\\")

    # start walkin'
    for foldername, subfolders, filenames in os.walk(root):
        # initialize counters
        num_photos = 0
        num_nonphotos = 0

        for filename in filenames:
            if not is_image(filename):
                num_nonphotos += 1
                continue


            current_file = pathlib.Path(foldername) / pathlib.Path(filename)

            try:
                with Image.open(current_file) as img:
                    width, height = img.size
                    if width > PHOTO_WIDTH and height > PHOTO_HEIGHT:
                        # this is a photo
                        num_photos += 1
                    else:
                        # too small to be a photo
                        num_nonphotos += 1
            except:  # catching PIL.UnidentifiedImageError, see note at bottom
                # add it to an error report
                write_to_errlog(current_file)

        # if more than half of files were photos, print abs path of folder
        try:
            if num_photos / num_nonphotos > 1:
                print(f"Photo pholder phound at {foldername}!")
        except ZeroDivisionError:  # sometimes a folder has nothing for us
            continue

    print("That's all, folks!")
    return


if __name__ == "__main__":
    print("Welcome to the Photo Pholder Phinder 2022! (patent pending)\n")
    main()


# Footnote: Thee reason why I used a bare except to catch that error is because
# Automate The Boring Stuff explicitly tells you not to import PIL, but to
# import Image `from` PIL, because that's just how it's done. I took Al
# Sweigart's advice and just used a bare except to catch that error. I didn't
# see any other errors being thrown by that particular block of code, so it
# seemed like the best solution to the problem, albeit bad practice.
