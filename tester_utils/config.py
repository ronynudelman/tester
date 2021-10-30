class Config:

    FILENAME = "config"
    OPTIONS = [
        "COMPILER",
        "COMPILATION_FLAGS",
        "SOURCE_FILES",
        "TEST_PATH",
        "NUM_OF_TESTS"
    ]
    MULTIPLE_VALUES_OPTIONS = [
        "COMPILATION_FLAGS",
        "SOURCE_FILES"
    ]
    NUMERICAL_VALUES_OPTIONS = [
        "NUM_OF_TESTS"
    ]
    MANDATORY_OPTIONS = [
        "COMPILER",
        "SOURCE_FILES",
        "NUM_OF_TESTS"
    ]
    NUM_OF_OPTIONS = len(OPTIONS)

    @classmethod
    def create_empty_config_file(cls):
        with open(cls.FILENAME, 'w') as config_file:
            for i in range(cls.NUM_OF_OPTIONS):
                config_file.write(cls.OPTIONS[i] + "=\n")

    @classmethod
    def is_mandatory_option_empty(cls, next_line_splited):
        if next_line_splited[0] in cls.MANDATORY_OPTIONS:
            return len(next_line_splited[1]) == 0
        else:
            return False

    @classmethod
    def has_multiple_values(cls, arg):
        return arg in cls.MULTIPLE_VALUES_OPTIONS

    @classmethod
    def has_numerical_value(cls, arg):
        return arg in cls.NUMERICAL_VALUES_OPTIONS

    @classmethod
    def check_next_line(cls, next_line):
        next_line_splited = next_line.strip("\n").split("=")
        if cls.is_mandatory_option_empty(next_line_splited):
            # TODO: print proper message
            print("INVALID OPTION")
            exit()
        if cls.has_multiple_values(next_line_splited[0]):
            option_value = next_line_splited[1].split(' ')
        elif cls.has_numerical_value(next_line_splited[0]):
            option_value = int(next_line_splited[1])
        else:
            option_value = next_line_splited[1]
        return option_value

    @classmethod
    def parse_file(cls):
        config_list = []
        with open(cls.FILENAME, 'r') as config_file:
            for i in range(cls.NUM_OF_OPTIONS):
                next_line = config_file.readline()
                option_value = cls.check_next_line(next_line)
                config_list.append(option_value)
        return config_list
