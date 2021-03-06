"""Generate .tex file suitable for plasTeX parsing/importing into gerby"""
from utils import *


with open('latex/make_doc.tex', 'w') as doc:
    print('\\documentclass{book}', file=doc)
    print('\\usepackage{amsmath}', file=doc)
    # print('\\usepackage{amsbook}', file=doc)
    
    with open('latex/preamble.tex', 'r') as preamble:
        next(preamble)
        next(preamble)
        next(preamble)

        for line in preamble:
            if line.find('%') == 0:
                continue
            if line.find('externaldocument') >= 0:
                continue
            if line.find('\\newenvironment{reference}') >= 0:
                continue
            if line.find('\\newenvironment{slogan}') >= 0:
                continue
            if line.find('\\newenvironment{history}') >= 0:
                continue
            if line.find('multicol') >= 0:
                continue
            if line.find('xr-hyper') >= 0:
                continue
            if line.find('\\ensuremath{') >= 0:
                line = line.replace('\\ensuremath{', '{')
            if line.find('\\displaylimits') >= 0:
                line = line.replace('\\displaylimits', '')
            if line.find('\\textsc{') >= 0:
                line = line.replace('\\textsc{', '{')
            if line.find('\\textcolor{blue}') >= 0:
                line = line.replace('\\textcolor{blue}', '')

            print(line, end='', file=doc)

    print('\\begin{document}', file=doc)
    # print('\\begin{titlepage}', file=doc)
    # print('\\pagestyle{empty}', file=doc)
    # print('\\setcounter{page}{1}', file=doc)
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
                if line.find('\\title{') == 0:
                    line = line.replace('\\title{', '\\chapter{')
                if line.find('\\maketitle') == 0:
                    continue
                if line.find('\\label{') >= 0:
                    label = extract_label(line)
                    if label != chapname and 'book-part' not in label:
                        line = line.replace('\\label{', '\\label{' + chapname + '-')
                if line.find('\\ref{') >= 0:
                    ref = extract_ref(line, 'ref')
                    if ref.split('-')[0] not in chapter_names:
                        line = line.replace('\\ref{', '\\ref{' + chapname + '-')
                if line.find('\\eqref{') >= 0:
                    ref = extract_ref(line, 'eqref')
                    if ref.split('-')[0] not in chapter_names:
                        line = line.replace('\\eqref{', '\\eqref{' + chapname + '-')
                if line.find('\\eref{') >= 0:
                    ref = extract_ref(line, 'eref')
                    if ref.split('-')[0] not in chapter_names:
                        line = line.replace('\\eref{', '\\eref{' + chapname + '-')
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