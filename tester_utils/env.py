import os


class Environment:

    BUILD_DIR_NAME = "build"
    MAIN_FILE_NAME = "main.cpp"
    HEADER_FILE_NAME = "tests.h"
    TESTER_DIR_PATH = os.getcwd()
    BUILD_DIR_PATH = os.path.join(TESTER_DIR_PATH, BUILD_DIR_NAME)
    MAIN_FILE_PATH = os.path.join(BUILD_DIR_PATH, MAIN_FILE_NAME)
    HEADER_FILE_PATH = os.path.join(BUILD_DIR_PATH, HEADER_FILE_NAME)

    @classmethod
    def create_build_dir(cls):
        os.mkdir(cls.BUILD_DIR_PATH)

    @classmethod
    def delete_build_dir(cls):
        os.rmdir(cls.BUILD_DIR_PATH)

    @classmethod
    def main_file_write_include(cls, main_file):
        main_file.write("#include <iostream>\n")
        main_file.write("#include <sstream>\n")
        main_file.write(f'#include "{cls.HEADER_FILE_PATH}"\n')
        main_file.write("\n\n")

    @classmethod
    def main_file_write_main_func(cls, main_file):
        main_file.write("int main(int argc, char const *argv[]) {")
        main_file.write("\n")
        main_file.write("  unsigned int test = parse_test(argv[1]);")
        main_file.write("\n")
        main_file.write("  run_test(test);")
        main_file.write("\n")
        main_file.write("  return 0;")
        main_file.write("\n")
        main_file.write("}")
        main_file.write("\n")
        main_file.write("\n\n")

    @classmethod
    def main_file_write_parse_test_func(cls, main_file):
        main_file.write("unsigned int parse_test(char const* test_str) {")
        main_file.write("\n")
        main_file.write("  std::stringstream test_parse;")
        main_file.write("\n")
        main_file.write("  test_parse << test_str;")
        main_file.write("\n")
        main_file.write("  unsigned int test = 0;")
        main_file.write("\n")
        main_file.write("  test_parse >> test;")
        main_file.write("\n")
        main_file.write("  return test;")
        main_file.write("\n")
        main_file.write("}")
        main_file.write("\n")
        main_file.write("\n\n")

    @classmethod
    def main_file_write_run_test_func(cls, main_file, num_of_tests):
        main_file.write("void run_test(unsigned int test) {")
        main_file.write("\n")
        main_file.write("  switch (test) {")
        main_file.write("\n")
        for i in range(num_of_tests):
            main_file.write(f"    case {i}:")
            main_file.write("\n")
            main_file.write(f"      test{i}();")
            main_file.write("\n")
            main_file.write("      break;")
            main_file.write("\n")
        main_file.write("    default:")
        main_file.write("\n")
        main_file.write("      break;")
        main_file.write("\n")
        main_file.write("  }")
        main_file.write("\n")
        main_file.write("}")
        main_file.write("\n")

    @classmethod
    def header_file_start_protection(cls, header_file):
        header_file.write("#ifndef TESTS_H")
        header_file.write("\n")
        header_file.write("#define TESTS_H")
        header_file.write("\n")
        header_file.write("\n\n")

    @classmethod
    def header_file_declare_utils_funcs(cls, header_file):
        header_file.write("unsigned int parse_test(char const* arg);")
        header_file.write("\n")
        header_file.write("void run_test(unsigned int test);")
        header_file.write("\n")
        header_file.write("\n\n")

    @classmethod
    def header_file_declare_tests_funcs(cls, header_file, num_of_tests):
        for i in range(num_of_tests):
            header_file.write(f"void test{i}();")
            header_file.write("\n")
        header_file.write("\n\n")

    @classmethod
    def header_file_end_protection(cls, header_file):
        header_file.write("#endif")
        header_file.write("\n")

    @classmethod
    def create_main_file(cls, num_of_tests):
        with open(cls.MAIN_FILE_PATH, 'w') as main_file:
            cls.main_file_write_include(main_file)
            cls.main_file_write_main_func(main_file)
            cls.main_file_write_parse_test_func(main_file)
            cls.main_file_write_run_test_func(main_file, num_of_tests)

    @classmethod
    def create_header_file(cls, num_of_tests):
        with open(cls.HEADER_FILE_PATH, 'w') as header_file:
            cls.header_file_start_protection(header_file)
            cls.header_file_declare_utils_funcs(header_file)
            cls.header_file_declare_tests_funcs(header_file, num_of_tests)
            cls.header_file_end_protection(header_file)

    @classmethod
    def delete_files(cls):
        os.remove(cls.MAIN_FILE_PATH)
        os.remove(cls.HEADER_FILE_PATH)

    @classmethod
    def set(cls, num_of_tests):
        cls.create_build_dir()
        cls.create_main_file(num_of_tests)
        cls.create_header_file(num_of_tests)

    @classmethod
    def clear(cls):
        cls.delete_files()
        cls.delete_build_dir()
