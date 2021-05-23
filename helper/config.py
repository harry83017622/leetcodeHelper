import os
import configparser
from pathlib import Path

BASE_URL = 'https://leetcode.com'
GRAPHQL_URL = 'https://leetcode.com/graphql'
API_URL = BASE_URL + '/api/problems/algorithms/'
HOME_URL = BASE_URL + '/problemset/algorithms'
SUBMISSION_URL = BASE_URL + '/submissions/detail/{id}/check/'

HOME = Path.cwd()
# HOME = Path.home()
CONFIG_FOLDER = HOME.joinpath('.config')
CONFIG_FILE = CONFIG_FOLDER.joinpath('config.cfg')

SECTION = 'leetcode'

LANG_MAPPING = {
    'C++': 'cpp',
    'Python': 'python',
    'Java': 'java',
    'C': 'c',
    'C#': 'csharp',
    'Javascript': 'javascript',
    'Ruby': 'ruby',
    'Swift': 'swift',
    'Go': 'go',
}


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


class Config(object):
    '''
    Config is a class to get user's configuration from leetcode.cfg
    config.cfg is located ~/.config/leetcdoe/config.cfg
    keys are:
        username
        password
        language
        ext # code file extension
        path # code path
    '''
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser[SECTION] = {
            'username': '',
            'password': '',
            'language': 'C++',
            'ext': '',
            'path': '',
            'keep_quiz_detail': 'false',
            'tmux_support': 'false'}
        self.username = None
        self.password = None
        self.language = 'Python'
        self.ext = '.py'
        self.path = None
        self.keep_quiz_detail = False
        self.tmux_support = False
    def _createConfig(self):
        with open(CONFIG_FILE, 'w') as configfile:
            self.parser.write(configfile)

    def load(self):
        if not CONFIG_FOLDER.exists():
            CONFIG_FOLDER.mkdir()
        if not CONFIG_FILE.exists():
            self._createConfig()
            return True

        self.parser.read(CONFIG_FILE)
        if SECTION not in self.parser.sections():
            return False

        self.username = self.parser.get(SECTION, 'username')
        self.password = self.parser.get(SECTION, 'password')
        self.language = self.parser.get(SECTION, 'language')
        self.ext = self.parser.get(SECTION, 'ext')
        self.path = self.parser.get(SECTION, 'path')
        self.path = os.path.expanduser(self.path)
        self.keep_quiz_detail = self.parser.getboolean(SECTION, 'keep_quiz_detail')
        self.tmux_support = self.parser.getboolean(SECTION, 'tmux_support')
        return True

    def write(self, key, value):
        self.load()
        self.parser.set(SECTION, key, value)
        with open(CONFIG_FILE, 'w') as configfile:
            self.parser.write(configfile)


config = Config()
