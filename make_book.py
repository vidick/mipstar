"""Generate .tex file for entire book"""
from utils import *


with open('make_book.tex', 'w') as doc:
    print('\\documentclass{book}', file=doc)
    print('\\usepackage{amsmath}', file=doc)
    
    with open('preamble.tex', 'r') as preamble:
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

            print(line, end='', file=doc)

    print('\\begin{document}', file=doc)
    # print('\\begin{titlepage}', file=doc)
    # print('\\pagestyle{empty}', file=doc)
    # print('\\setcounter{page}{1}', file=doc)
    # print "\\centerline{\\LARGE\\bfseries MIP*}"
    # print('\\vskip1in', file=doc)
    # print('\\end{titlepage}', file=doc)

    _, chapters = get_chapters()

    for chapter in chapters:
        with open(chapter) as texfile:
            for line in texfile:
                if line.find('\\input{preamble}') == 0:
                    continue
                if line.find('\\begin{document}') == 0:
                    continue
                if line.find('\\title{') == 0:
                    line = line.replace('\\title{', '\\chapter{')
                if line.find('\\maketitle') == 0:
                    continue
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