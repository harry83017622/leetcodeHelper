from pathlib import Path
from functools import wraps
from helper.config import CONFIG_FOLDER, config


SNIPPET_FOLDER = Path(CONFIG_FOLDER) / Path('snippet')
BEFORE = SNIPPET_FOLDER.joinpath('before')
AFTER = SNIPPET_FOLDER.joinpath('after')


def get_data(filepath):
    if filepath.exists():
        with open(filepath, 'r') as f:
            return f.read()
    return ''



def unique_file_name(filepath):
    if isinstance(filepath, str):
        filepath = Path(filepath)

    if not filepath.exists():
        return filepath

    path = filepath.parent
    filename = filepath.stem
    ext = filepath.suffix
    index = 1
    while filepath.exists():
        filepath = path / Path(filename + '-' + str(index) + ext)
        index = index + 1
    return filepath


def get_code_file_path(quiz_id):
    path = config.path
    if not path or not Path(config.path).exists():
        path = Path.home() / 'leetcode'
        if not path.exists():
            path.mkdir()
    else:
        path = Path(path)

    return path / Path(str(quiz_id) + '.' + config.ext)


def get_code_for_submission(filepath):
    data = get_data(filepath)
    before = get_data(BEFORE)
    after = get_data(AFTER)
    return data.replace(before, '').replace(after, '')


def edit_code(quiz_id, code, newcode=False):
    filepath = get_code_file_path(quiz_id)
    if newcode:
        filepath = unique_file_name(filepath)

    code = prepare_code(code, config.language, filepath)
    if not filepath.exists():
        with open(filepath, 'w') as f:
            f.write(code)
    return filepath


@enhance_code
@generate_makefile
def prepare_code(code, language, filepath):
    return code
