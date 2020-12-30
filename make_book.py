"""Generate .tex file for entire book"""
from utils import *


with open('latex/make_book.tex', 'w') as doc:
    print('\\documentclass{book}', file=doc)
    print('\\usepackage{amsmath}', file=doc)
    print('\\usepackage{amsthm}', file=doc)
    print('\\usepackage{amsfonts}', file=doc)
    
    with open('latex/preamble.tex', 'r') as preamble:
        next(preamble)
        next(preamble)
        next(preamble)

        for line in preamble:
            if line.find('%') == 0:
                continue
            if line.find('externaldocument') >= 0:
                continue
            if line.find('xr-hyper') >= 0:
                continue
            if line.find('\\newcommand{\\cal}[1]{\\mathcal{#1}}') == 0:
                line = line.replace('\\newcommand{\\cal}[1]{\\mathcal{#1}}', '\\renewcommand{\\cal}[1]{\\mathcal{#1}}')
            print(line, end='', file=doc)

    print('\\begin{document}', file=doc)
    # print('\\begin{titlepage}', file=doc)
    # print('\\pagestyle{empty}', file=doc)
    # print('\\setcounter{page}{1}', file=doc)
    # print "\\centerline{\\LARGE\\bfseries MIP*}"
    # print('\\vskip1in', file=doc)
    # print('\\end{titlepage}', file=doc)

    chapter_names, chapters = get_chapters()

    for i, chapter in enumerate(chapters):
        chapname = chapter_names[i]
        with open('latex/' + chapter) as texfile:
            print('% chapter-' + chapname, file=doc)
            for line in texfile:
                if line.find('\\input{preamble}') == 0:
                    continue
                if line.find('\\begin{document}') == 0:
                    continue
                if line.find('\\part{') == 0:
                    next(texfile)
                if line.find('\\title{') == 0:
                    line = line.replace('\\title{', '\\chapter{')
                if line.find('\\maketitle') == 0:
                    continue
                if line.find('\\label{') >= 0:
                    label = extract_label(line, chapname)
                    if label != chapname and 'book-part' not in label:
                        line = line.replace('\\label{', '\\label{' + chapname + '-')
                if line.find('\\tableofcontents') == 0:
                    continue
                if line.find('\\input{chapters}') == 0:
                    continue
                if line.find('\\bibliography') == 0:
                    continue
                if line.find('\\end{document}') == 0:
                    continue
                print(line, end='', file=doc)

    print('\\bibliography{my}', file=doc)
    print('\\bibliographystyle{amsalpha}', file=doc)
    print('\\end{document}', file=doc)