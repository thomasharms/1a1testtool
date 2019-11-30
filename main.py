from system_environment import System_Environment
from pytesttool import Test_Handler
import os, sys, subprocess

class Main_Controller():

    # list of test files and bash files
    __test_file_list = list()
    __bash_file_list = list()

    __test_handler = None

    def __init__(self):
        self.system_environment = System_Environment()
        self.set_test_file_list()
        self.set_bash_file_list()
        self.set_test_handler()
        self.main()

    def main(self):
        self.__test_handler.main()

    def set_test_file_list(self):
        self.__test_file_list = list(self.system_environment.discover_test_files())

    def set_bash_file_list(self):
        self.__bash_file_list = list(self.system_environment.discover_bash_files())

    def set_test_handler(self):
        self.__test_handler = Test_Handler(self.system_environment, self.__test_file_list, self.__bash_file_list)

if __name__ == "__main__":
    main_task = Main_Controller()
    