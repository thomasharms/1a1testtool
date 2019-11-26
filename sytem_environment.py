import platform, re, subprocess, os

class System_Environment():

    __patterns = {"bash_file_name_pattern": r".*?\.sh$",
                "bash_file_pattern" : r"^#!\/bin\/bash.*?"
                }

    def __init__(self):
        # initialize self.os_type -- Windows, Darwin (Mac) or Linux
        self.set_os_type()
        # get destination of the working directory file has been executed in
        self.set_pwd()
        self.get_bash_location()

    def get_bash_location(self):
        try:
            self.bash_location = str(subprocess.check_output(['which', 'bash']))
        except Exception as e:
            # TODO WINDOWS BEHAVIOUR FOR BASH INPUT
            pass

    # get source type of test suite
    # self.source_type = folder, file, bash, False if not existent
    def get_test_source_type(self, source=""):

        if os.path.isdir(source):
            self.source_type = "folder"
            print("looking for tests in folder.....")
        elif os.path.exists(source):
            self.source_type = "file"
            print("looking for tests in file or bash.....")
        else:
            self.source_type = False


    def set_os_type(self):
        self.os_type = platform.system()

    def set_pwd(self):
        self.pwd = os.getcwd()

    def check_bash_file(self, file_name):
        bash_pattern = 
        prog = re.compile(bash_pattern, , re.MULTILINE)
        result = prog.findall(file_name)

