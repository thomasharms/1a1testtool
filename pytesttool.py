import pytest, subprocess, time, threading
from db import DB

class Test_Task():

    testname = ""
    environment = ""
    start = 0
    finish = 0

    # preparing
    # running
    # finished
    status = 'preparing'
    logs = "no entry"

    def __init__(self, test_file, venv_pytest_target):
        self.test_file = test_file
        self.venv_pytest_target = venv_pytest_target
        self.set_test_name()
        self.prepare_test()
        self.run_test()
        self.post_process_test()

    def run_test(self):
        try:
            self.set_status_running()
            r = subprocess.run([self.venv_pytest_target, self.test_file])
            self.logs = str(r)
        except Exception as e:
            self.logs = str(e)

    # set parameters and handle db save procedures before test starts
    def prepare_test(self):
        self.set_permissions()
        self.start = time.time()
        db = DB()
        db.init_test(self.set_test_data_save_params())

    def post_process_test(self):
        self.finish = time.time()
        db = DB()
        db.update_param_by_name(self.testname, 'testfinish', self.finish)
        self.status = 'finished'
        db.update_param_by_name(self.testname, 'status', self.status)
        db.update_param_by_name(self.testname, 'logs', self.logs)

    def set_status_running(self):
        db = DB()
        self.status = 'running'
        db.update_param_by_name(self.testname, 'status', self.status)

    def set_test_data_save_params(self):
        data_dict = dict()
        data_dict['testname'] = self.testname
        data_dict['status'] = self.status
        data_dict['teststart'] = self.start
        data_dict['testfinish'] = self.finish
        data_dict['logs'] = self.logs
        data_dict['environment'] = self.environment
        return data_dict

    def set_test_name(self):
        self.testname = str(self.test_file)+'__'+str(int(time.time()))
        self.environment = self.venv_pytest_target

    # this is really ugly, but for now there is no way to get around it for demo purposes
    def set_permissions(self):
        try:
            subprocess.run(['chmod', '777', self.test_file])
        except Exception as e:
            print(str(e))

class Test_Bash():

    '''
        For Demo puposes bash files run pytest out of one of the venvs and a static test file right now
        This could easily be setup to any other fashion
        F.i. only bash files or the flexible test way presented with multiple files or folders aso.
        ./$bashfilename.sh ./venvxyz/bin/pytest ./Test_Repo/test_example1.py
    '''

    testname = ""
    environment = ""
    start = 0
    finish = 0

    # preparing
    # running
    # finished
    status = 'preparing'
    logs = "no entry"

    def __init__(self, bash_file, venv_pytest_target, repo_dir):
        self.bash_file = bash_file
        self.repo_dir = repo_dir
        self.venv_pytest_target = venv_pytest_target
        self.set_test_name()
        self.prepare_test()
        self.run_test()
        self.post_process_test()

    # TODO assign some other way of files for bash files
    def get_test_file(self):
        return str(self.repo_dir)+"/test_example1.py"

    def run_test(self):
        try:
            self.set_status_running()
            r = subprocess.call([self.bash_file, self.venv_pytest_target, self.get_test_file()])
            self.logs = str(r)
        except Exception as e:
            self.logs = str(e)

    # set parameters and handle db save procedures before test starts
    def prepare_test(self):
        self.set_permissions()
        self.start = time.time()
        db = DB()
        db.init_test(self.set_test_data_save_params())

    def post_process_test(self):
        self.finish = time.time()
        db = DB()
        db.update_param_by_name(self.testname, 'testfinish', self.finish)
        self.status = 'finished'
        db.update_param_by_name(self.testname, 'status', self.status)
        db.update_param_by_name(self.testname, 'logs', self.logs)

    def set_status_running(self):
        db = DB()
        self.status = 'running'
        db.update_param_by_name(self.testname, 'status', self.status)

    def set_test_data_save_params(self):
        data_dict = dict()
        data_dict['testname'] = self.testname
        data_dict['status'] = self.status
        data_dict['teststart'] = self.start
        data_dict['testfinish'] = self.finish
        data_dict['logs'] = self.logs
        data_dict['environment'] = self.environment
        return data_dict

    def set_test_name(self):
        self.testname = str(self.bash_file)+'__'+str(int(time.time()))
        self.environment = self.venv_pytest_target

    # this is really ugly, but for now there is no way to get around it for demo purposes
    def set_permissions(self):
        try:
            subprocess.run(['chmod', '777', self.bash_file])
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
        return self.__sys_env.get_venv_pytest_target(venv_number)

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
            # lock is True if locked
            if self.__venv_locks[free]:
                free += 1
            else: found = True
        if found: return free
        else: return False

    # lock a venv if used
    def lock_venv(self, channel):
        while self.__venv_locks[channel]:
            pass
        self.__venv_locks[channel] = True

    # unlock the venv for further usage
    def unlock_venv(self, channel):
        self.__venv_locks[channel] = False

    def main(self):
        '''
        threads = [ threading.Thread(target=self.test_file) for _i in range(len(self.__test_file_list)) ]
        for thread in threads:
            thread.start()
        '''
        bash_threads = [ threading.Thread(target=self.test_bash_file) for _i in range(len(self.__bash_file_list)) ]
        for bthread in bash_threads:
            bthread.start()
            
    def test_file(self):
        active_test = self.__test_file_list.pop(0)
        self.assign_test_to_venv(active_test)

    def assign_test_to_venv(self, test_file):
        channel = -1
        while channel < 0:
            channel = self.check_free_venv()
        self.lock_venv(channel)

        Test_Task(test_file, self.set_venv_path(channel))

        self.unlock_venv(channel)
    
    def assign_bash_to_venv(self, bash_file):
        channel = -1
        while channel < 0:
            channel = self.check_free_venv()
        self.lock_venv(channel)
        
        Test_Bash(bash_file, self.set_venv_path(channel), self.__sys_env.get_test_repo())
        self.unlock_venv(channel)

    def test_bash_file(self):
        active_bash = self.__bash_file_list.pop(0)
        self.assign_bash_to_venv(active_bash)
