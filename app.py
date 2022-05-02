#!venv/bin/python3.8
import sys
from lib import methods
from sys import argv


def run(args: list) -> None:
    """
    This function runs the program
    :param args: command line arguments
    :return: None
    """
    if len(args) == 1 or args[1] == "--help" and len(args) == 2:
        methods.helping_info()
        sys.exit()

    if len(args) != 3:
        print("Incorrect command line. Waited: app.py input_file.txt output_file.txt")
        print("Add key '--help' to check more info.")
        sys.exit()

    file_in, file_out = args[1:]
    container = methods.create_container()

    # Running methods
    methods.read_file(container, file_in)
    methods.print_filtered_data(container)
    methods.write_file(container, file_out)
    methods.clear(container)


if __name__ == '__main__':
    console_args = argv
    run(argv)
