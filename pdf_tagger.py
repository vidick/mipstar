"""Add tags and hypertargets to all .tex files"""
import os
from utils import get_chapters, extract_label


# retrieve all tags from tag file
tags = {}
with open('tags', 'r') as tags_file:
    tag_tuples = [line.split(',') for line in tags_file.readlines()]
    tags = {label.rstrip():tag for tag, label in tag_tuples}

# get all chapters
chapter_names, chapters = get_chapters()

# add margin notes/tags to each chapter file
for i, chapter in enumerate(chapters):
    chapname = chapter_names[i]
    first_section = True
    with open(os.path.join('pdfs', chapter), 'w') as tagged_file:
        with open(chapter) as tex_file:
            for line in tex_file:
                # add marginnote package first
                if line.find('\\begin{document}') == 0:
                    print('\\usepackage{marginnote}', file=tagged_file)
                # if found section need to put margin note before \section
                # otherwise note will not be visible
                if line.find('\\section{') >= 0:
                    # offset section numbering so correct ref numbers are displayed
                    if first_section:
                        print('\\addtocounter{section}{' + str(i) + '}', file=tagged_file)
                        first_section = False
                    nextline = next(tex_file)
                    if nextline.find('\\label{') >= 0:
                        label = extract_label(nextline, chapname)
                        if label != chapname and 'book-part' not in label:
                            label = chapname + '-' + label

                        if label in tags.keys():
                            print('\\hypertarget{' + tags[label] + '}{}', file=tagged_file)
                            print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tagged_file)
                            print(line, end='', file=tagged_file)
                            print(nextline, end='', file=tagged_file)
                            continue
                    # if no label, write lines as normal
                    else:
                        print(line, end='', file=tagged_file)
                        print(nextline, end='', file=tagged_file)
                        continue
                # skip part commands in individual chapters
                if line.find('\\part{') >= 0:
                    next(tex_file)
                    continue
                # if label present on line, add margin note to side and hypertarget
                if line.find('\\label{') >= 0:
                    label = extract_label(line, chapname)
                    if label != chapname and 'book-part' not in label:
                        label = chapname + '-' + label

                    if label in tags.keys():
                        print('\\hypertarget{' + tags[label] + '}{}', file=tagged_file)
                        print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tagged_file)
                print(line, end='', file=tagged_file)

# add margin notes/tags to book
with open(os.path.join('pdfs', 'book.tex'), 'w') as tagged_file:
    with open('make_book.tex') as tex_file:
        for line in tex_file:
            # add marginnote package first
            if line.find('\\begin{document}') == 0:
                print('\\usepackage{marginnote}', file=tagged_file)
            # if found section need to put margin note before \section
            # otherwise note will not be visible
            if line.find('\\section{') == 0:
                nextline = next(tex_file)
                if nextline.find('\\label{') >= 0:
                    label = extract_label(nextline, chapname)

                    if label in tags.keys():
                        print('\\hypertarget{' + tags[label] + '}{}', file=tagged_file)
                        print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tagged_file)
                        print(line, end='', file=tagged_file)
                        print(nextline, end='', file=tagged_file)
                        continue
                # if no label, write lines as normal
                else:
                    print(line, end='', file=tagged_file)
                    print(nextline, end='', file=tagged_file)
                    continue
            # if label present on line, add margin note to side and hypertarget;
            # skip tagging parts
            if line.find('\\label{') >= 0:
                label = extract_label(line, chapname)

                if label in tags.keys() and 'book-part' not in label and label != chapname:
                    print('\\hypertarget{' + tags[label] + '}{}', file=tagged_file)
                    print('\\reversemarginpar\\marginnote{\\textnormal{' + tags[label] + '}}', file=tagged_file)
            print(line, end='', file=tagged_file)
