#!/usr/bin/env python3


from tester_utils.args import Args
from tester_utils.config import Config
from tester_utils.env import Environment
import subprocess
import os


class Tester:

    def __init__(self):
        config_list = Config.parse_file()
        self.compiler = config_list[0]
        self.compilition_flags = config_list[1]
        self.source_files = config_list[2]
        self.test_path = config_list[3]
        self.num_of_tests = config_list[4]
        self.args_list = Args.parse_args()

    def set_env(self):
        Environment.set(self.num_of_tests)

    def clear_env(self):
        Environment.clear()

    def get_compilation_cmd(self):
        pass

    def run_compilation_cmd(self):
        pass

    def get_tests_list(self):
        pass

    def run_tests(self):
        pass


def main():
    tester = Tester()
    tester.set_env()
    tester.get_compilation_cmd()
    tester.run_compilation_cmd()
    tester.get_tests_list()
    tester.run_tests()
    tester.clear_env()


if __name__ == '__main__':
    main()
