import datatypes as dt
import re

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
    "pass" : "PASS",
    "break" : "BREAK",
    "func" : "FUNC",
}

line_filling_keywords = {
    "raar" : "RAAR",
    "ettol" : "ETTOL",
    "ray" : "RAY",
}

data_types = {
    r"\d+" : dt.getal,
    r"[\d\w\s\t\f]*" : dt.string,
    r"\[([\d\w\s\t\f]*,)*\]" : dt.list,
}

patterns = {
    "path_pattern" : re.compile(r".*\.uh"),  #  controleerd of het bestand eindigd op de goede extensie
    "keyword_pattern" : re.compile(rf"[{keywords.keys()}]([{data_types.keys()}][])")  #  kijken voor keywords
    "comparison_pattern" : re.compile(rf"([{data_types.keys()}][])\s[{comparison_characters.keys()}]\s([{data_types.keys()}][])")
}
