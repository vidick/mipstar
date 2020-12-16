python3 make_doc.py
python3 tagger.py make_doc.tex > tags
python3 make_book.py
python3 pdf_tagger.py
python3 make_pdfs.py
