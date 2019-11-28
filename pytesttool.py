import pytest, subprocess

class Test_Task():

    def __init(self, test):
        self.test = test


class Test_Handler():

    def __init__(self, sys_env):
        self.__test_queue = list()
        self.__sys_env = sys_env
        
        # fixed length of number of installed venvs -> system_environment.get_amount_venv()
        # lock will be False if unused, True if locked
        self.init_venv_locks()

    def init_venv_locks(self):

        self.__venv_locks = list()
        for i in range(self.__sys_env.get_amount_venv()):
            self.__venv_locks[i] = False

    # returns the lowest number of free venv channel or false if there is none
    def check_free_venv(self):

        free = 0
        while free < self.__sys_env.get_amount_venv():
            if self.__venv_locks[free]:
                free += 1
            else: found = True
        if found: return free
        else: return False

    
            






#subprocess.call(pwd/bashtest.sh')
#r = subprocess.run(['ls', '-lha'])



