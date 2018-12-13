import argparse
import os
import sys


def debug(str):
    print("[DEBUG]", str)


def md_sort(list_input_file):
    markfiles = []
    for file in list_input_file:
        extension = file[-3:]
        if extension == ".md":
            markfiles.append(arg.input + "/" + file)

    if len(markfiles) <= 0:
        print("There is no markfiles in the input directory")
        sys.exit()
    else:
        return markfiles


def convert2html(line):
    html_line = ""
    if line[:1] == "#":
        html_line = title_html(line)
    elif line[:1] == "*":
        html_line = ("<li>" + line[1:].rstrip() + " </li>")
    else:
        html_line = line
    return html_line


def title_html(line):
    if line[:4] == "####":
        html_line = ("<h4>" + line[4:].rstrip() + " </h4>")
    elif line[:3] == "###":
        html_line = ("<h3>" + line[3:].rstrip() + " </h3>")
    elif line[:2] == "##":
        html_line = ("<h2>" + line[2:].rstrip() + " </h2>")
    elif line[:1] == "#":
        html_line = ("<h1>" + line[1:].rstrip() + " </h1>")
    return html_line


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

# Sorting files

list_input_files = os.listdir(arg.input)
markfiles = md_sort(list_input_files)

# Reading files

for md_file in markfiles:
    with open(md_file) as file_to_read:
        for line in file_to_read:
            # debug(convert2html(line))
            output_file = open(arg.output+"/output.html", "a")
            output_file.write(convert2html(line)+"\n")
            output_file.close()
