from db import DB
import subprocess, os, sys

def build_test_table():
    db = DB()
    sql = "CREATE TABLE `testenv` (\
	        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\
            `testname`	TEXT NOT NULL,\
            `environment`	TEXT NOT NULL,\
            `start`	INTEGER NOT NULL,\
            `finish`	INTEGER NOT NULL,\
            `logs`	TEXT NOT NULL,\
            `status`	INTEGER NOT NULL\
        );"
    db.execute_sql(sql)

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

#build_test_table()
build_virtual_environments()
install_pytest()


