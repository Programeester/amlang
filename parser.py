import lexer
from os.path import exists, isfile 

def is_valid_path(path):
    if lexer.patterns["path_pattern"].match(path) and exists(path) and isfile(path):
        return True

def parse(file):
    pass