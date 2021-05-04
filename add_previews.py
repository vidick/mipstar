from bs4 import BeautifulSoup
import os

def find_ref_doc(tag, root, files):
    for file in files:
        if tag in file.split('-') and file.endswith('.tag'):
            preview = BeautifulSoup(open(os.path.join(root, file)), 'lxml')
            all_text = preview.findAll(text=True)
            content = ''
            
            char_count = 0
            i = 0
            while char_count < 250 and i < len(all_text):
                label_pos = all_text[i].find('\\label{')
                while label_pos != -1:
                    end_brace_pos = all_text[i].find('}', label_pos)
                    all_text[i] = all_text[i][:label_pos] + all_text[i][end_brace_pos + 1:]
                    label_pos = all_text[i].find('\\label{')

                content += all_text[i]
                char_count += len(all_text[i])
                i += 1
            content = content.replace('\n', ' ')
            print('extra text: ' + str(all_text[i:]))
            return (content, i != len(all_text))
    return ('', False)

for root, dirs, files in os.walk('./latex/make_doc/'):
    for file in files:
        if file.endswith('.tag'):
            doc = BeautifulSoup(open(os.path.join(root, file)), 'lxml')
            refs = doc.select('p a[data-tag]')
            # span_refs = doc.select('span.equation-label a[data-tag]')

            # intersect = set(refs) & set(span_refs)

            for ref in refs:
                # make sure current reference link has a data-tag and
                # is not an equation label
                if ref['data-tag'] and (ref.parent.name != 'span' or 'equation-label' not in ref.parent['class']):
                    content, shortened = find_ref_doc(ref['data-tag'], root, files)
                    if content:
                        ref['data-content'] = content
                        if shortened:
                            ref['data-shortened'] = '[...]'
                        ref['class'] = 'page-preview'

            with open(os.path.join(root, file), 'w') as f:
                f.write(str(doc))