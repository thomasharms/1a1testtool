from db import DB
from datetime import datetime

result_count = 10

def show_last_results(result_count):
        
    db = DB()
    try:
        test_results = db.show_last_tests(result_count)
    except Exception as e:
        print(str(e))

    if type(test_results) is list and test_results:
        for i in range(len(test_results)):
            print("\n *** Test Result Nr. %d ***\n" % i)
            print("TEST NAME : %s" % test_results[i][0])
            print("TEST ENVIRONMENT : %s" % test_results[i][1])
            print("TEST START : " +str(datetime.fromtimestamp(test_results[i][2])))
            print("TEST FINISH : " +str(datetime.fromtimestamp(test_results[i][3])))
            print("TEST LOG : %s" % test_results[i][4])
            print("TEST STATUS : %s" % test_results[i][5])
            print("TEST INSERTION TIME : " +str(datetime.fromtimestamp(test_results[i][6])))
    else:
        print("No tests done yet.")

show_last_results(result_count)