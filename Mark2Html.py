import argparse
import os
import sys
import shutil
import markdown2
from markdown2 import Markdown
from pathlib import Path
from shutil import copytree, ignore_patterns
import re


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
    if not os.path.isfile(arg.template):
        print(arg.template, "template file doesn't exist")
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
markdownfiles = md_sort(list_input_files)

# Translating files

htmlfiles = []
url = []
markdowner = Markdown()
for markdownfile in markdownfiles:
    with open(markdownfile, "r", encoding="utf-8") as f:
        # htmlfiles_url.append(f.read())
        htmlfiles.append(markdowner.convert(f.read()))
        # htmlfiles_url.append(f.read())
        title = os.path.basename(markdownfile)[:-3]

    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))[^<>()"]+', htmlfiles[-1])
    for url in urls:
        htmlfiles[-1] = htmlfiles[-1].replace(url, "<a href= "+url+" > "+url+" </a>")

    with open(arg.output+"/"+title+".html", "x", encoding="utf-8") as f:
        f.write(htmlfiles[-1])

# Copying in template

if arg.template is not None:
    list_output_files = os.listdir(arg.output)

    for output_file, html_translation in zip(list_output_files, htmlfiles):
        lines_template = []
        with open(arg.template, "r", encoding="utf_8") as template:
            for line in template:
                lines_template.append(line)
        index_replace_me = lines_template.index("[REPLACE_ME]\n")

        title = os.path.basename(output_file)[:-5]

        lines_template[index_replace_me] = html_translation
        with open(arg.output+"/"+title+"_template.html", "x", encoding="utf-8") as index_file:
            index_file.write("\n".join(lines_template))

    # Copying template files

    print("Do you want to copy template files in ouput directory ? (y/n)", end=" ")
    if input() == "y":
        path = arg.template.replace(os.path.basename(arg.template), "")
        shutil.copytree(path, arg.output+"/TEMPLATE",
                        ignore=ignore_patterns(os.path.basename(arg.template)))
        list_translated_template = os.listdir(arg.output)
        for translated_template in list_translated_template:
            if translated_template.find("_template.html") == -1:
                list_translated_template.remove(translated_template)
        for translated_template in list_translated_template:
            shutil.copy(arg.output+"/"+translated_template, arg.output+"/TEMPLATE")
print("DONE")
