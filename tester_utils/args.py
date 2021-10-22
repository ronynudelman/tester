import argparse


class Args:
    ARGS_HELP_FILE = "tester_utils/args_help.txt"
    lines_counter = 0
    with open(ARGS_HELP_FILE, 'r') as args_help_file:
        while len(args_help_file.readline()) > 0:
            lines_counter += 1
    ARGS_HELP_FILE_SIZE = lines_counter

    @classmethod
    def read_help_values(cls):
        args_help = {}
        with open(cls.ARGS_HELP_FILE, 'r') as args_help_file:
            for i in range(cls.ARGS_HELP_FILE_SIZE):
                next_line = args_help_file.readline()
                help_option = next_line.strip("\n").split("=")[0]
                help_value = next_line.strip("\n").split("=")[1]
                args_help[help_option] = help_value
        return args_help

    @classmethod
    def parse_args(cls):
        args_help = cls.read_help_values()
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--tests",
                            default="all",
                            help=args_help.get("TESTS_HELP"))
        parser.add_argument("-c", "--comp",
                            action="store_true",
                            default=False,
                            help=args_help.get("COMP_HELP"))
        parser.add_argument("-f", "--flags",
                            action="store_true",
                            default=False,
                            help=args_help.get("FLAGS_HELP"))
        return parser.parse_args()
