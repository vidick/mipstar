"""Generate PDFs of all .tex files."""
import os
import glob
import subprocess
from utils import get_chapters

AUX = ['*.log', '*.out', '*.toc']

_, chapters = get_chapters()
chapters.append('book.tex')

for chapter in chapters:
    # PDF recipe: pdflatex x2 -> bibtex -> pdflatex x2
    # pdflatex = subprocess.Popen(['latex', chapter], cwd='./pdfs')
    # pdflatex.communicate()
    pdflatex = subprocess.Popen(['latex', chapter], cwd='./pdfs')
    pdflatex.communicate()
    bibtex = subprocess.Popen(['bibtex', chapter], cwd='./pdfs')
    bibtex.communicate()
    pdflatex = subprocess.Popen(['latex', chapter], cwd='./pdfs')
    pdflatex.communicate()
    pdflatex = subprocess.Popen(['latex', chapter], cwd='./pdfs')
    pdflatex.communicate()

    # clean up auxiliary files
    # for ext in AUX:
    #     files = glob.glob(os.path.join('./pdfs', ext))
    #     for file in files:
    #         os.remove(file)