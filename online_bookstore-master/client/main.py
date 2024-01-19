from PyQt5.QtWidgets import *
from windows import *
from sql import DB
import sys

class DB_test:
    def __init__(self):
        self.db=1
        self.cursor=2

database_test=DB_test()

#数据库身份信息
# database=DB()
# sql_info=database.get_sql_info()
# database.connectDB(sql_info)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    # window=welcomeWindow(database)
    window=storeMainWindow(database_test)
    sys.exit(app.exec())