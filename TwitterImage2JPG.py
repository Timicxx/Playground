import glob
import os
import argparse

parser = argparse.ArgumentParser(description='Converts images with twitter format to jpeg format')
parser.add_argument('-p', '--path', help="Path to scan for", dest="path", metavar="path", required=True)
args = vars(parser.parse_args())

os.chdir(args["path"])
extensions = ["*.jpg_large", "*.png_large", "*.jpg_orig"]
file_list = list()

for extension in extensions:
    file_list = file_list + glob.glob(extension)

for file in file_list:
    for extension in extensions:
        new_extension = extension.replace('*', '')
        if file.endswith(new_extension):
            new_name = file.replace(new_extension, '') + ".jpg"
            os.rename(file, new_name)

print("Done!")
