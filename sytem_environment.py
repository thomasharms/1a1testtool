import platform, re, subprocess, os

class System_Environment():

    __patterns = {  "bash_file_name_pattern": r".*?\.sh$",
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
            self.bash_location = subprocess.check_output(['which', 'bash']).decode()
        except Exception as e:
            # TODO WINDOWS BEHAVIOUR FOR BASH INPUT
            print("No bash location found with error: %s " % (str(e)))
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

    # file is a path and not just a name
    def check_bash_file(self, filepath):
        prog = re.compile(self.__patterns['bash_file_name_pattern'], re.MULTILINE)
        result = prog.findall(filepath)
        if result:
            return True
        else:
            return False

    # file is a path and not just a name
    def check_bash_file_content(self, filepath):
        proper_bash_file = False
        if self.bash_location:
            with open(filepath, 'r') as f:
                content = f.read()
                prog = re.compile(self.__patterns['bash_file_pattern'], re.MULTILINE)
                result = prog.findall(content)
                if result: proper_bash_file = True
        return proper_bash_file

            

