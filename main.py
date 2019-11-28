from system_environment import System_Environment
import os, sys

class Main_Controller():

    def __init__(self):
        self.system_environment = System_Environment()
        self.main()

    def main(self):
        pass
''' 
    def run_test_suite(self):
        self.validate_test_path()

    def validate_test_path(self):
        #self.system_environment.get_test_source_type(self.test_source)
        if self.system_environment.source_type == "folder":

            #TODO implement folder test
            
            print("folder")
            pass

        elif self.system_environment.source_type == "file":
            print("file")
            #TODO implement file test test or bash
            pass
        
        elif not self.system_environment.source_type:
            #print("\n\n Folder or file does not exist at: \n %s \n" % (self.test_source))
            # start over, returns to main menu to provide opportunity to exit
            pass
'''
if __name__ == "__main__":
    main_task = Main_Controller()
    print(main_task.system_environment.discover_files())