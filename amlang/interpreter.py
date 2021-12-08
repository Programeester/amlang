import parser, sys

def run_on_command_line(path):
    if parser.is_valid_path(path):
        print("ja dit gedeelte werkt!!! :D")
        parsed = parser.parse(path)
    else:
        print("dat bestand bestaat niet")


path = sys.argv[1]
run_on_command_line(path)