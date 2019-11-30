from db import DB
import subprocess, os, sys

# fixed for three environments
#  TODO implemented in a more flexible fashion regarding amounts of venvs
def build_virtual_environments():
    subprocess.run(['python3', '-m', 'venv', os.path.dirname(sys.argv[0])+'/venv1/'])
    subprocess.run(['python3', '-m', 'venv', os.path.dirname(sys.argv[0])+'/venv2/'])
    subprocess.run(['python3', '-m', 'venv', os.path.dirname(sys.argv[0])+'/venv3/'])

#  TODO implemented in a more flexible fashion regarding amounts of venvs
def install_pytest():
    subprocess.call([os.path.dirname(sys.argv[0])+'/venv1/bin/pip3', 'install', 'pytest'])
    subprocess.call([os.path.dirname(sys.argv[0])+'/venv2/bin/pip3', 'install', 'pytest'])
    subprocess.call([os.path.dirname(sys.argv[0])+'/venv3/bin/pip3', 'install', 'pytest'])

def build_db_table():
    db = DB()
    try:
        db.build_test_table()
    except Exception as e:
        print(str(e))

build_db_table()
build_virtual_environments()
install_pytest()


