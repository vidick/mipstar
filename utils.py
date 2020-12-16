"""Common functions used in scripts."""
def extract_label(line, chapname):
    """Return the \\label on the given line"""
    start = line.find('\\label{')
    for i in range(start, len(line)):
        if line[i] == '}':
            label = line[start + 7 : i]
            break
    # if label != chapname:
    #     label = chapname + '-' + label
    return label


def get_chapters():
    """Retrieves all chapter names and their corresponding .tex files."""
    chapsfile = open('chapters', 'r')
    chapters = [name.rstrip() for name in chapsfile.readlines()]
    chapters_noext = [chapter.split('.')[0] for chapter in chapters]
    chapsfile.close()

    return chapters_noext, chapters


def log_outputs(logger, out, err, prepend_out='', prepend_err=''):
    """Log output and error messages to console."""
    if out:
        logger.info(prepend_out + ''.join(out))
    if err:
        logger.info(prepend_err + ''.join(err))
