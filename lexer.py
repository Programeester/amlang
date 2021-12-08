import datatypes as dt
import re

patterns = {
    "path_pattern" : re.compile(r".*\.uh"),  #  controleerd of het bestand eindigd op de goede extensie
}

math_characters = {
    "+" : "PLUS",
    "-" : "MIN",
    "*" : "KEER",
    "/" : "GEDEELD_DOOR",
    "%" : "REST",
    "^" : "MACHT",
}

logical_characters = {
    "&" : "EN",
    "|" : "OF",
}

comparison_characters = {
    "<" : "MINDER_DAN",
    "<=" : "MINDER_DAN_OF_GELIJK_AAN",
    "==" : "GELIJK_AAN",
    ">" : "MEER_DAN",
    "<=" : "MEER_DAN_OF_GELIJK_AAN",
}

keywords = {
    "return" : "RETURN",
    "if" : "IF",
    "elif" : "ELIF",
    "else" : "ELSE",
    "class" : "CLASS",
    "pass" : "PASS",
    "break" : "BREAK",
    "func" : "FUNC",
    "raar" : "RAAR",
    "ettol" : "ETTOL",
    "ray" : "RAY",
}

data_types = {
    "int" : int,
    "float" : float,
    "string" : str,
    "list" : list,
    "object" : dt.class_,
}
