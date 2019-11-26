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
    __test_env_fields = ['testname', 'environment', 'start', 'finish', 'logs', 'status']

    def __init__(self):
        self.__con = sqlite3.connect(self.__db_filename)
        self.__cursor = self.__con.cursor()

    def get_error(self):
        return self.__error

    def execute_sql(self, sql):
        self.__cursor.execute(sql)

    # expecting data_dict as dictionary of {attribute_name, value}
    def save_article(self, data_dict):
        count = 0
        attribute_names = data_dict.keys()
        max_count = len(attribute_names) - 1

        sql = "INSERT INTO " + self.__table_tess + " ("

        # build the chain of keys
        for key in attribute_names:
            if count == max_count:
                sql = sql + key + ") "
            elif count < max_count:
                sql = sql + key + ", "
                count += 1

        # build intermezzo
        sql = sql + " VALUES ("

        # build the chain of values
        count = 0
        for key in attribute_names:

            if count < max_count:
                sql = sql + str(data_dict[key]) + ', '
                count += 1
            elif count == max_count:
                sql = sql + str(data_dict[key]) + ') '

        # execute insertion
        self.__cursor.execute(sql)

'''
def get_test_data(self):
        sql = "SELECT * FROM " + self.__table_tests
        self.__cursor.execute(sql)
        result_set = self.__cursor.fetchall()
        return result_set
db = DB()
print(db.get_test_data())
'''
