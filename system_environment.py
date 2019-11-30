import platform, re, subprocess, os, sys

class System_Environment():

    __patterns = {  "bash_file_name_pattern": r".*?\.sh$",
                    "bash_file_pattern" : r"^#\!\/bin\/bash.*?",
                    "test_file_start_pattern" : r"^test_.*?\.py$",
                    "test_file_end_pattern" : r"^.*?_test\.py$"
                }

    __test_folder_name = "/Test_Repo/"
    
    __venv_amount = 3
    # repository of test files
    _repo_dir = ""
    # Windows, Darwin (Mac) or Linux
    _os_type = ""
    # location of bash installation, usually /bin/bash for unix
    _bash_location = ""



    def __init__(self):
        # initialize self._os_type -- Windows, Darwin (Mac) or Linux
        self.set_os_type()

        # get destination of the working directory file has been executed in,
        # sys pointer is located and bash location folder
        self.set_cwd()
        self.set_pwd()
        self.set_repo_dir()
        self.get_bash_location()

    def set_repo_dir(self):
        self._repo_dir = os.path.dirname(sys.argv[0])+self.__test_folder_name

    def set_cwd(self):
        self.cwd = os.path.dirname(sys.argv[0])

    def get_amount_venv(self):
        return self.__venv_amount

    def get_venv_py_target(self, venv_number):
        return os.path.dirname(sys.argv[0])+'venv'+venv_number+'/bin/python3'

    def get_bash_location(self):
        try:
            self._bash_location = subprocess.check_output(['which', 'bash']).decode()
        except Exception as e:
            # TODO WINDOWS BEHAVIOUR FOR BASH INPUT
            print("No bash location found with error: %s " % (str(e)))
            pass
    
    # look for files in Repository folder
    def discover_test_files(self):

        #working with set to avoid duplicates
        files = set()
        files.update(self.get_test_file_list())
        return files

    def discover_bash_files(self):
        
        #working with set to avoid duplicates
        files = set()
        files.update(self.get_bash_file_list())
        return files

    def set_os_type(self):
        self._os_type = platform.system()

    def set_pwd(self):
        self.pwd = os.getcwd()

    def check_bash_file(self, filepath):
        prog = re.compile(self.__patterns['bash_file_name_pattern'], re.MULTILINE)
        result = prog.findall(filepath)
        if result:
            return True
        else:
            return False

    def check_test_file_start_pattern(self, file_name):
        prog = re.compile(self.__patterns['test_file_start_pattern'], re.MULTILINE)
        result = prog.findall(file_name)
        if result: return True
        else: return False

    def check_test_file_end_pattern(self, file_name):
        prog = re.compile(self.__patterns['test_file_end_pattern'], re.MULTILINE)
        result = prog.findall(file_name)
        if result: return True
        else: return False

    def get_bash_file_list(self):
        return [self._repo_dir+x for x in os.listdir(self._repo_dir) if self.check_bash_file(x)]

    # pytest is able to do this as well, but in order to implement concurrency this is neccessary
    # get test file list in a directory
    # parsing for test_ or _test.py patterns
    def get_test_file_list(self):
        return [self._repo_dir+x for x in os.listdir(self._repo_dir) if self.check_test_file_start_pattern(x) or self.check_test_file_end_pattern(x)]
        
    # checks whether a bash file is sort of properly constructed
    def check_bash_file_content(self, filepath):
        proper_bash_file = False
        if self._bash_location:
            with open(filepath, 'r') as f:
                content = f.read()
                prog = re.compile(self.__patterns['bash_file_pattern'], re.MULTILINE)
                result = prog.findall(content)
                if result: proper_bash_file = True
        return proper_bash_file

    
class Virtual_Environment_Controller():

    def __init__(self):
        pass

#subprocess.run(['python3', '-m', 'venv', os.path.dirname(sys.argv[0])+'/venv1/'])
#subprocess.call([os.path.dirname(sys.argv[0])+'/venv1/bin/pip3', 'install', 'pytest'])
subprocess.run([os.path.dirname(sys.argv[0])+'/venv1/bin/python3', os.path.dirname(sys.argv[0])+'/init.py'])

            

