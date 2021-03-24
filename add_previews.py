from bs4 import BeautifulSoup
import os

def find_ref_doc(tag, root, files):
    for file in files:
        if tag in file.split('-'):
            preview = BeautifulSoup(open(os.path.join(root, file)), 'lxml')
            all_text = preview.findAll(text=True)
            content = ''
            
            char_count = 0
            i = 0
            while char_count < 250 and i < len(all_text):
                content += all_text[i]
                char_count += len(all_text[i])
                i += 1
            return content
    return ''

for root, dirs, files in os.walk('./latex/make_doc/'):
    for file in files:
        if file.endswith('.tag'):
            doc = BeautifulSoup(open(os.path.join(root, file)), 'lxml')
            refs = doc.select('p a[data-tag]')
            for ref in refs:
                if ref['data-tag']:
                    content = find_ref_doc(ref['data-tag'], root, files)
                    if content:
                        ref['data-content'] = content
                        ref['class'] = 'page-preview'
                        ref['data-animation'] = 'false'
                        ref['data-toggle'] = 'preview'
            print(os.path.join(root, file[:-4] + '-new.html'))
            with open(os.path.join(root, file[-3] + '-new.html'), 'w') as f:
                f.write(str(doc.prettify()))