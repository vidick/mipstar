from bs4 import BeautifulSoup
import glob, os

def find_ref_doc(tag, files):
    for file in files:
        if tag in file.split('-'):
            preview = BeautifulSoup(open(file), 'lxml')
            all_text = preview.findAll(text=True)
            content = ''
            
            char_count = 0
            i = 0
            while char_count < 250:
                content += all_text[i]
                char_count += len(all_text[i])
                i += 1
            return content
    return ''

for root, dirs, files in os.walk('./latex/make_doc/'):
    for file in files:
        if file.endswith('.tag'):
            doc = BeautifulSoup(open(file), 'lxml')
            refs = doc.select('p a[data-tag]')
            for ref in refs:
                if ref['data-tag']:
                    content = find_ref_doc(ref['data-tag'], files)
                    if content:
                        ref['data-content'] = content
                        ref['class'] = 'page-preview'
            with open(file, 'w') as f:
                f.write(str(doc))