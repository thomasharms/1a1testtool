import sqlite3

'''
table_schema:
1. testenv
	`id`	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `testname`	    TEXT NOT NULL,
    `environment`   TEXT NOT NULL,
    `start`	        INTEGER NOT NULL,
    `finish`	    INTEGER NOT NULL,
    `logs`	        TEXT NOT NULL,
    `status`	    INTEGER NOT NULL
    `insertion`	    INTEGER NOT NULL
'''
class DB:
    __con = 0
    __cursor = 0
    __db_filename = "pytesttool.db"
    __table_tests = "testenv"
    __error = 0
    # 0 everything seems to be fine
    # 1 
    # 2 IOERROR
    # 3 
    # 9 some other error
    
    # helper list for building queries
    __test_env_fields = ['testname', 'environment', 'teststart', 'testfinish', 'logs', 'status']

    def __init__(self):
        self.__con = sqlite3.connect(self.__db_filename)
        self.__cursor = self.__con.cursor()

    def get_error(self):
        return self.__error

    def execute_sql(self, sql):
        self.__cursor.execute(sql)
        self.__con.commit()

    # expecting data_dict as dictionary of {attribute_name, value}
    def save_test(self, data_dict):
        count = 0
        attribute_names = data_dict.keys()
        max_count = len(attribute_names) - 1

        sql = "INSERT INTO " + self.__table_tests + " ("

        # build the chain of keys
        for key in attribute_names:
            if count == max_count:
                sql = sql + key + ") "
            elif count < max_count:
                sql = sql + key + ", "
                count += 1

        # build intermezzo
        sql = sql + " VALUES (\'"

        # build the chain of values
        count = 0
        for key in attribute_names:

            if count < max_count:
                sql = sql + str(data_dict[key]) + '\', \''
                count += 1
            elif count == max_count:
                sql = sql + str(data_dict[key]) + '\') '
        print(sql)
        # execute insertion
        self.__cursor.execute(sql)
        #commit changes
        self.__con.commit()


    def get_test_data(self):
        sql = "SELECT * FROM " + self.__table_tests
        self.__cursor.execute(sql)
        result_set = self.__cursor.fetchall()
        return result_set

    def build_test_table(self):
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
#db.execute_sql(db.build_test_table())
testdic = {'testname': 'testname1', 'environment': 'env1', 'start': 22, 'finish': 3324, 'logs': 'nologfile','status': 3}
db.save_test(testdic)
print(db.get_test_data())

