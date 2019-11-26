from sytem_environment import System_Environment

class Main_Controller():

    def __init__(self):
        self.system_environment = System_Environment()
        self.main()


    def run_main_menu(self):
        print("Please choose one of the following by typing the number and hit \"ENTER\":\n")
        print("1) Run Tests")
        print("2) Review Test Logs")
        print("3) Exit Program")
        self.main_first_level_task = input("What do you want to do: ")
        self.execute_main_action()

    def main(self):
        self.run_main_menu()
        while self.main_first_level_task != "3":
            self.run_main_menu()
        self.exit()

    def exit(self):
        print("Bye")

    def execute_main_action(self):

        # Test Environment...
        if self.main_first_level_task == "1":
            self.run_test_suite()

        # Logging Environment....
        elif self.main_first_level_task == "2":
            self.run_log_menu()

        # Exit Path
        elif self.main_first_level_task == "3":
            pass

        # Catch everything else and try again
        else:
            print("\nThe input could not be recognized.\n")
    
    def run_test_suite(self):
        self.run_test_menu()
        self.validate_test_path()

    def validate_test_path(self):
        self.system_environment.get_test_source_type(self.test_source)
        if self.system_environment.source_type == "folder":

            #TODO implement folder test
            print("folder")
            pass

        elif self.system_environment.source_type == "file":
            print("file")
            #TODO implement file test test or bash
            pass
        
        elif not self.system_environment.source_type:
            print("\n\n Folder or file does not exist at: \n %s \n" % (self.test_source))
            # start over, returns to main menu to provide opportunity to exit
        

    def run_test_menu(self):
        
        print("\n\n Please specify the location of the test files, a test file or bash file:\n")
        self.test_source = input()

    def run_log_menu(self):
        print("log")
        


if __name__ == "__main__":
    main_task = Main_Controller()
    