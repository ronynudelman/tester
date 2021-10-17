#!/usr/bin/env python3


from tester_utils.config import Config


class Tester:
    def __init__(self):
        config_list = Config.parse_file()
        self.compiler = config_list[0]
        self.compilition_flags = config_list[1]
        self.source_files = config_list[2]
        self.test_path = config_list[3]
        self.num_of_tests = config_list[4]


def main():
    tester = Tester()


if __name__ == '__main__':
    main()
