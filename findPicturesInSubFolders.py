import glob
import argparse

parser = argparse.ArgumentParser(description='Prints all image paths from subfolders in the path specified')
parser.add_argument('-p', '--path', help="Path to scan for", dest="path", metavar="path", required=True)
args = vars(parser.parse_args())


path = args["path"]
images = []

image_list = glob.glob(path + "\\*\\*")

print(image_list)
