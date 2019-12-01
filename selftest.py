from pytesttool import Test_Handler
from system_environment import System_Environment
import os, sys

class Self_Test():

    __selftest_file_name = "test_selftest.py"

    def __init__(self):
        self.set_test_file_list()
        self.set_bash_file_list()
        self.set_sysenv()
        self.set_test_handler()
        self.main()

    def get_selftest_file_name(self):
        return self.__selftest_file_name

    def set_sysenv(self):
        self.sysenv = System_Environment()

    def set_test_handler(self):
        self.test_handler = Test_Handler(self.sysenv, self.selftest_file_list, self.selftest_bash_file_list)

    # append bash file paths here in case you want to test them
    def set_bash_file_list(self):
        self.selftest_bash_file_list = list()

    def set_test_file_list(self):
        self.selftest_file_list = list()
        self.selftest_file_list.append(os.path.dirname(sys.argv[0])+'/'+self.__selftest_file_name)

    def main(self):
        self.test_handler.main()

s = Self_Test()
