import pytest, subprocess

class Test_Task():

    testname = ""
    environment = ""
    start = 0
    finish = 0

    # 0 about to start, preparing
    # 1 running
    # 2 finished
    status = 0
    logs = ""

    def __init(self, test_file, venv_py_target):
        self.test_file = test_file
        self.venv_py_target = venv_py_target
        self.set_permissions()
        self.run_test()

    

    def run_test(self):
        try:
            subprocess.run([self.venv_py_target, self.test_file])
        except Exception as e:
            print(str(e))

    # this is really ugly, but for now there is no way to get around it for demo purposes
    def set_permissions(self):
        try:
            subprocess.run(['chmod', '777', self.test_file])
        except Exception as e:
            print(str(e))

    
class Test_Handler():

    __test_queue = list()
    __test_file_list = list()
    __bash_file_list = list()
    __venv_locks = list()

    def __init__(self, sys_env, test_file_list, bash_file_list):
        self.set_file_lists(test_file_list, bash_file_list)
        self.__sys_env = sys_env
        
        # fixed length of number of installed venvs -> system_environment.get_amount_venv()
        # lock will be False if unused(unlocked), True if used(locked)
        self.init_venv_locks()

    def set_venv_path(self, venv_number):
        return self.__sys_env.get_venv_py_target(venv_number)

    def set_file_lists(self, test_file_list, bash_file_list):
        self.__test_file_list = test_file_list
        self.__bash_file_list = bash_file_list

    def init_venv_locks(self):
        for _ in range(self.__sys_env.get_amount_venv()):
            self.__venv_locks.append(False)

    # returns the lowest number of free venv channel or false if there is none
    def check_free_venv(self):

        free = 0
        found = False
        while free < self.__sys_env.get_amount_venv() and not found:
            if self.__venv_locks[free]:
                free += 1
            else: found = True
        if found: return free
        else: return False

    # lock a venv if used
    def lock_venv(self, channel):
        while not self.__venv_locks[channel]:
            pass
        self.__venv_locks[channel] = True

    # unlock the venv for further usage
    def unlock_venv(self, channel):
        self.__venv_locks[channel] = False

    def main(self):
        while self.__test_queue:
            pass

    def test_files(self):
        while self.__test_file_list:
            active_test = self.__test_file_list.pop(0)
            self.assign_test_to_venv(active_test)

    def assign_test_to_venv(self, test_file):
        channel = False
        while not channel:
            channel = self.check_free_venv()
        self.lock_venv(channel)
        Test_Task(test_file, self.set_venv_path(channel))
        self.unlock_venv(channel)


#subprocess.call(pwd/bashtest.sh')
#subprocess.run(['ls', '-lha'])
