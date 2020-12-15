"""Generate PDFs of all .tex files."""
import os
import glob
import subprocess
from utils import *

AUX = ['*.aux', '*.log', '*.out', '*.toc']

chapter_names, chapters = get_chapters()
for chapter in chapters:
    # PDF recipe: pdflatex > bibtex > pdflatex x2
    pdflatex = subprocess.Popen(['pdflatex', chapter], cwd='./pdfs')
    pdflatex.communicate()
    bibtex = subprocess.Popen(['bibtex', chapter], cwd='./pdfs')
    bibtex.communicate()
    pdflatex = subprocess.Popen(['pdflatex', chapter], cwd='./pdfs')
    pdflatex.communicate()
    pdflatex = subprocess.Popen(['pdflatex', chapter], cwd='./pdfs')
    pdflatex.communicate()

    # clean up auxiliary files
    for ext in AUX:
        files = glob.glob(os.path.join('./pdfs', ext))
        for file in files:
            os.remove(file)
