import pymysql as sql

class DB():
    __host='10.126.26.53'
    __user='user'
    __password='123456'
    __target='onlineshopping'
    def get_sql_info(self):
        return (self.__host,self.__user,self.__password,self.__target)

    def connectDB(self,sql_info):
        host,user,password,target = sql_info[0],sql_info[1],sql_info[2],sql_info[3]
        self.db = sql.connect(host=host, port=3306, user=user, password=password, db=target,charset='utf8mb4')
        self.cursor = self.db.cursor()

    @staticmethod
    def get_consuID(cursor):
        cursor.execute('select consuID from consumers where consuID like \'consu%\'')
        consuIDs = cursor.fetchall()
        return consuIDs

    @staticmethod
    def get_storeID(cursor):
        cursor.execute('select consuID from consumers where consuID like \'store%\'')
        consuIDs = cursor.fetchall()
        return consuIDs

    @staticmethod
    def get_consuName(cursor):
        cursor.execute('select consuName from consumers')
        consuNames = cursor.fetchall()
        return consuNames

    @staticmethod
    def get_storeName(cursor):
        cursor.execute('select storeName from store')
        storeNames = cursor.fetchall()
        return storeNames

    @staticmethod
    def get_PW(cursor,id):
        cursor.execute('select consuPW from consumers where consuID=\'{}\''.format(id))
        PW = cursor.fetchone()
        return PW
    

    def calculate_shopCart(self):
        self.cursor.execute('select count(*) from consumers where consuID like \'consu%\'')
        num=self.cursor.fetchone()
        return num[0]

    @staticmethod
    def get_shopCart(self):
        self.cursor.execute('select count(*) from consumers where consuID like \'consu%\'')
        num=self.cursor.fetchone()
        return num[0]

    def set_usr(self,info):
        self.cursor.execute('insert into consumers values {}'.format(info))
        self.db.commit()

    #CHY
    def get_memberInfo(self, consuID):
        self.cursor.execute(f"select memberID,memberType,memberLV,memberTime from member where consuID={consuID}")
        return self.cursor.fetchone()

    def insert_memberInfo(self, info):
        self.cursor.execute(f"insert into member values {info}")
        self.db.commit()

    def get_goodInfo(self, storeID):
        self.cursor.execute(f"select goodID,goodName,goodClass,goodPrice,cmtCount,cmttypePCT from goods where storeID={storeID}")
        return self.cursor.fetchone()

    def insert_good(self, info):
        self.cursor.execute(f"insert into goods values {info}")
        self.db.commit()

    def delete_good(self, goodID):
        self.cursor.execute(f"delete from goods where goodID='{goodID}'")
        self.db.commit()

    def get_orderInfo(self, consuID):
        self.cursor.execute(f"select orderID,orderDate,storeID,consuAddr,orderState from orders where consuID={consuID}")
        return self.cursor.fetchone()

    def delete_order(self, orderID):
        self.cursor.execute(f"delete from orders where orderID='{orderID}'")
        self.db.commit()
