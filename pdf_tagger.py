"""Add tags and hypertargets to all chapter .tex files"""
import os
from utils import *


# retrieve all tags from tag file
tags = {}
with open('tags', 'r') as tags_file:
    tag_tuples = [line.split(',') for line in tags_file.readlines()]
    tags = {label.rstrip():tag for tag, label in tag_tuples}

# get all chapters
chapter_names, chapters = get_chapters()

for i, chapter in enumerate(chapters):
    chapname = chapter_names[i]

    with open(os.path.join('pdfs', chapter), 'w') as tex_file:
        with open(chapter) as texfile:
            for line in texfile:
                # add marginnote package first
                if line.find('\\begin{document}') == 0:
                    print('\\usepackage{marginnote}', file=tex_file)
                # if found section need to put margin note before \section
                # otherwise note will not be visible
                if line.find('\\section{') == 0:
                    nextline = next(texfile)
                    if nextline.find('\\label{') >= 0:
                        label = extract_label(nextline, chapname)
                        if label in tags.keys():
                            print('\\hypertarget{' + tags[label] + '}{}', file=tex_file)
                            print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tex_file)
                            print(line, end='', file=tex_file)
                            print(nextline, end='', file=tex_file)
                            continue
                    # if no label, write lines as normal
                    else:
                        print(line, end='', file=tex_file)
                        print(nextline, end='', file=tex_file)
                        continue
                # if label present on line, add margin note to side and hypertarget
                if line.find('\\label{') >= 0:
                    label = extract_label(line, chapname)
                    if label in tags.keys():
                        print('\\hypertarget{' + tags[label] + '}{}', file=tex_file)
                        print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tex_file)
                print(line, end='', file=tex_file)