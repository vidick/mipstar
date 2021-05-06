"""Common functions used in scripts."""


def extract_label(line):
    """Return the \\label on the given line"""
    start = line.find('\\label{')
    for i in range(start, len(line)):
        if line[i] == '}':
            label = line[start + 7 : i]
            break
    return label

def extract_ref(line, refType):
    """Return the \\ref or \\eqref or \\eref on the given line"""
    target = '\\' + refType + '{'

    start = line.find(target)
    for i in range(start, len(line)):
        if line[i] == '}':
            ref = line[start + len(target) : i]
            break
    return ref

def get_chapters():
    """Retrieves all chapter names and their corresponding .tex files."""
    chapsfile = open('chapters', 'r')
    chapters = [name.rstrip() for name in chapsfile.readlines()]
    chapters_noext = [chapter.split('.')[0] for chapter in chapters]
    chapsfile.close()

    return chapters_noext, chapters
