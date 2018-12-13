import argparse
import os
import sys


def debug(str):
    print("[DEBUG]", str)


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory",
                    type=str,
                    action="store",
                    dest="input",
                    required=True,
                    help="Input directory, make sur your markdowns files are inside")
parser.add_argument("-o", "--output-directory",
                    type=str,
                    action="store",
                    default="./output",
                    dest="output",
                    help="Output directory, where will be created HTML files\n default value = ./output")
parser.add_argument("-t", "--template-directory",
                    type=str,
                    action="store",
                    dest="template",
                    help="Source directory, HTML/CSS files used to generate output")
arg = parser.parse_args()

# Argument validation

if not os.path.exists(arg.input):
    print(arg.input, "input directory doesn't exist")
    sys.exit()

if arg.template:
    if not os.path.exists(arg.template):
        print(arg.template, "template directory doesn't exist")
        sys.exit()
    else:
        print(arg.template, "template selected")
else:
    print("No template selected")

if not os.path.exists(arg.output):
    print("Creating", arg.output, "output directory")
    os.makedirs(arg.output)
else:
    print(arg.output, "output directory already exist")

list_input_file = os.listdir(arg.input)
# debug(list_input_file)
markfiles = []

for file in list_input_file:
    # debug(file)
    extension = file[-3:]
    if extension == ".md":
        markfiles.append(arg.input + "/" + file)
        debug(markfiles)

if len(markfiles) <= 0:
    print("There is no markfiles in the input directory")
    sys.exit()

for md_file in markfiles:
    with open(md_file) as file_to_read:
        for line in file_to_read:
            if line[:3] == "###":
                print(line)
            elif line[:2] == "##":
                print(line)
            elif line[:1] == "#":
                print(line)
