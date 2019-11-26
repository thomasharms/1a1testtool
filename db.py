import sqlite3

'''
table_scheme:
1. article
id INTEGER
author TEXT
creation REAL
header TEXT
sub_header TEXT
short_header BLOB
article_text BLOB
rubricID INTEGER
html BLOB
url TEXT
offline_date REAL
comments INTEGER
comment_on_date REAL
comment_off_date REAL
insertion REAL
references TEXT
last_crawled REAL
outletID INTEGER
ispublic INTEGER
tagset TEXT

2. version
id INTEGER
articleID INTEGER
author TEXT
creation REAL
header TEXT
sub_header TEXT
short_header BLOB
article_text BLOB
rubricID INTEGER
html BLOB
url TEXT
offline_date REAL
comments INTEGER
comment_on_date REAL
comment_off_date REAL
insertion REAL
references TEXT
last_crawled REAL
outletID INTEGER
ispublic INTEGER
tagset TEXT

3. interview
id INTEGER
author TEXT
interviewer TEXT
guest TEXT
creation REAL
header TEXT
sub_header TEXT
short_header BLOB
article_text BLOB
rubricID INTEGER
html BLOB
url TEXT
offline_date REAL
comments INTEGER
comment_on_date REAL
comment_off_date REAL
insertion REAL
references TEXT
last_crawled REAL
outletID INTEGER
ispublic INTEGER
tagset TEXT

4. newsoutlet
id INTEGER
name TEXT
domain TEXT
crawling_intervall INTEGER

5. rubric
id INTEGER
name TEXT
outletID INTEGER
url TEXT
'''

class DB:
    __con = 0
    __cursor = 0
    __db_filename = "news.db"
    __table_articles = "article"
    __table_versions = "version"
    __table_interview = "interview"
    __table_rubric = "rubric"
    __table_news_outlets = "newsoutlet"
    __error = 0
    # 0 everything seems to be fine
    # 1 domain does not exist
    # 2 IOERROR
    # 3 no rubric found
    # 9 some other error

    def __init__(self):
        self.__con = sqlite3.connect(self.__db_filename)
        self.__cursor = self.__con.cursor()

    def get_error(self):
        return self.__error

    def execute_sql(self, sql):
        self.__cursor.execute(sql)

    def get_article_by_title(self, title):
        sql = "SELECT * FROM " + self.__table_articles
              #+ " WHERE Header == " + title
        self.__cursor.execute(sql)

    # expecting data_dict as dictionary of {attribute_name, value}
    def save_article(self, data_dict):
        count = 0
        attribute_names = data_dict.keys()
        max_count = len(attribute_names) - 1

        sql = "INSERT INTO " + self.__table_articles + " ("

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

        # expecting data_dict as dictionary of {attribute_name, value}
        def save_version(self, data_dict):

            attribute_names = data_dict.keys()
            max_count = len(attribute_names) - 1

            sql = "INSERT INTO " + self.__table_articles + " ("

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

    # to initialize service domain and crawling interval have tb fetched
    def get_domain_crawling_interval(self):
        sql = "SELECT name, crawling_interval FROM "+self.__table_news_outlets
        self.__cursor.execute(sql)
        result_set = self.__cursor.fetchall()
        if result_set:
            return result_set
        else:
            return False

    # function to check if article is stored
    # in case data set is already stored return data set to check if something changed
    def get_article_by_url(self, url):
        sql = "SELECT * FROM " + self.__table_articles + "WHERE url = " + url + "LIMIT 1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        if result[0]:
            return result[0]
        else:
            return False

    def get_parser_class_by_domain_name(self, domain_name):
        sql = "SELECT parser_class FROM " + self.__table_news_outlets + " WHERE name = " + domain_name + " LIMIT 1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        if result[0]:
            return result[0]
        else:
            return False

    # returns a set like: [(name, url),(name, url),...] or False if an error occured
    def get_rubricset_by_domain(self, domain):
        domainid = self.get_domainid_by_name(domain)
        sql = "SELECT name, url FROM "+self.__table_rubric+" WHERE outletID = "+str(domainid)
        try:
            self.__cursor.execute(sql)
            resp = self.__cursor.fetchall()
            if resp:
                return resp
            else:
                return False
        except ValueError:
                self.__error = 1
        except IOError:
            self.__error = 2
        except:
            self.__error = 9

    def get_domainid_by_name(self, domain):
        sql = "SELECT id FROM "+self.__table_news_outlets+" WHERE name = \""+domain+"\" LIMIT 1"
        self.__cursor.execute(sql)
        resp = self.__cursor.fetchone()
        try:
            domainid = resp[0]
            if domainid is not None or domainid > 0:
                return domainid
            else:
                return False
        except ValueError:
            self.__error = 3
        except IOError:
            self.__error = 2
        except:
            self.__error = 9

    def get_rubric_by_id(self, rubric_id):
        sql = "SELECT name FROM "+self.__table_rubric+" WHERE id = "+rubric_id+" LIMIT 1"

        self.__cursor.execute(sql)
        resp = self.__cursor.fetchone()
        try:
            rubric_name = resp[0]
            if rubric_name:
                return rubric_name
            else:
                return False
        except ValueError:
            self.__error = 3
        except IOError:
            self.__error = 2
        except:
            self.__error = 9

    def get_domain_url_by_name(self, domain):
        sql = "SELECT domain FROM " + self.__table_news_outlets + " WHERE name = \"" + domain + "\" LIMIT 1"
        self.__cursor.execute(sql)
        resp = self.__cursor.fetchone()
        try:
            url = resp[0]
            if url is not None or url > 0:
                return url
            else:
                return False
        except ValueError:
            self.__error = 3
        except IOError:
            self.__error = 2
        except:
            self.__error = 9

    # might return FALSE if there is no version stored
    # might return set of data even if there is only one element stored
    # as soon there is a stored version available, there will be a list available
    def get_version_by_url(self, url):
        sql = "SELECT * FROM "+self.__table_versions+" WHERE url = \""+url+"\" ORDER BY insertion"

        self.__cursor.execute(sql)
        resp = self.__cursor.fetchall()
        try:
            if resp:
                return resp
            else:
                return False
        except ValueError:
            self.__error = 3
        except IOError:
            self.__error = 2
        except:
            self.__error = 9

    def test_get_tables(self):
        sql = "SELECT * FROM article"
        self.__cursor.execute(sql)
        re = self.__cursor.fetchall()
        print(db.__error)

db = DB()
if db.get_error() == 0:
    print(1)
else:
    print(2)
#db.test_get_tables()
'''
url = db.get_rubricset_by_domain("ZEIT ONLINE")
print(url)
for rubric in url:
    print(rubric)
    print(rubric[1])
    print("\n")
'''
