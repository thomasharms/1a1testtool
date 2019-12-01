import sqlite3, time

'''
table_schema:
1. testenv
	`id`	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `testname`	    TEXT NOT NULL,
    `environment`   TEXT NOT NULL,
    `start`	        INTEGER NOT NULL,
    `finish`	    INTEGER NOT NULL,
    `logs`	        TEXT NOT NULL,
    `status`	    TEXT NOT NULL,
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

    def init_test(self, data_dict):
        data_dict['insertion'] = time.time()
        self.save_test(data_dict)

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
                sql = sql + str(data_dict[key]) + '\'); '
        
        # execute insertion
        self.__cursor.execute(sql)
        #commit changes
        self.__con.commit()

    # sqlite v3.3 enabled "table not exists" queries
    # to be sure functionality is there, use this function for now
    def check_table_exists(self):
        sql = 'SELECT name FROM sqlite_master WHERE type=\'table\' AND name= \'%s\'' % self.__table_tests
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        if result: return True
        else: return False


    def get_test_data(self):
        sql = "SELECT * FROM " + self.__table_tests
        self.__cursor.execute(sql)
        result_set = self.__cursor.fetchall()
        return result_set

    def build_test_table(self):
        if not self.check_table_exists():
            sql = "CREATE TABLE `testenv` (\
                `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\
                `testname`	TEXT NOT NULL,\
                `environment`	TEXT NOT NULL,\
                `teststart`	INTEGER NOT NULL,\
                `testfinish`	INTEGER NOT NULL,\
                `logs`	TEXT NOT NULL,\
                `status`	INTEGER NOT NULL\
                `insertion`	INTEGER NOT NULL\
            );"
            # execute creation
            self.__cursor.execute(sql)
            #commit changes
            self.__con.commit()

    def delete_quotes(self, sample):
        return sample.replace("'"," ")

    def update_param_by_name(self, testname, var_name, var_value):
        sql = "UPDATE "+self.__table_tests+" SET "+var_name+ " = ' "+self.delete_quotes(str(var_value))+" ' WHERE testname = '"+testname+"';"
        self.__cursor.execute(sql)
        self.__con.commit()

    def show_last_tests(self, test_count):
        sql = "SELECT testname, environment, teststart, testfinish, logs, status, insertion FROM "+self.__table_tests+" ORDER BY insertion DESC LIMIT %s;" % str(test_count)
        self.__cursor.execute(sql)

        result = self.__cursor.fetchall()
        return result

#db = DB()
#db.execute_sql(db.build_test_table())
#testdic = {'testname': 'testname1', 'environment': 'env1', 'start': 22, 'finish': 3324, 'logs': 'nologfile','status': 3}
#db.save_test(testdic)


