with open('make_doc.tex', 'w') as doc:
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

            print(line, end='', file=doc)

    print('\\begin{document}', file=doc)
    # print('\\begin{titlepage}', file=doc)
    # print('\\pagestyle{empty}', file=doc)
    # print('\\setcounter{page}{1}', file=doc)
    # print('\\vskip1in', file=doc)
    # print('\\end{titlepage}', file=doc)

    chapsfile = open('chapters', 'r')
    chapters = chapsfile.readlines()
    chapsfile.close()

    for chapter in chapters:
        chapter = chapter.rstrip()
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