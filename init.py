from db import DB

def build_test_table():
    sql = "CREATE TABLE `testenv` (\
	        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\
            `testname`	TEXT NOT NULL,\
            `environment`	TEXT NOT NULL,\
            `start`	INTEGER NOT NULL,\
            `finish`	INTEGER NOT NULL,\
            `logs`	TEXT NOT NULL,\
            `status`	INTEGER NOT NULL\
        );"
    return(sql)

db = DB()
db.execute_sql(build_test_table())


