import lexer
from os.path import exists, isfile 
import re

def is_valid_path(path):
    if lexer.patterns["path_pattern"].match(path) and exists(path) and isfile(path):
        return True

def parse(file):
    with open(file, "rt"):
        for line in file.readlines():
            if 