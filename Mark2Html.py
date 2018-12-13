import argparse
import os
import sys

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

if not os.path.exists(arg.template):
    print(arg.template, "template directory doesnt exist")
    sys.exit()

if not os.path.exists(arg.output):
    print("Creating", arg.output, "output directory")
    os.makedirs(arg.output)
else:
    print(arg.output, "output directory already exist")
