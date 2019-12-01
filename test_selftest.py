import os, sys
from system_environment import System_Environment

# very simple test
# feel free to create more meaningful assertions
def test():
    sysenv = System_Environment()
    assert sysenv.get_test_repo() == os.path.dirname(sys.argv[0])+"/Test_Repo/"
    