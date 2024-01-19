class user:
    def __init__(self,info):
        self.__id,self.__name,self.__phone,self.__ban=info[0],info[1],info[2],info[3]
    def getInfo(self):
        return (self.__id,self.__name,self.__phone,self.__ban)
    def setName(self,name):
        self.__name=name
    def setPhone(self,phone):
        self.__phone=phone
    
class consumer(user):
    def __init__(self,info):
        super().__init__(info)
        self.__cart=info[4]
    def getInfo(self):
        return super().getInfo()+tuple([self.__cart])
    
class store(user):
    def __init__(self,info):
        super().__init__(info)
        self.__level=info[4]
    def getInfo(self):
        return super().getInfo()+tuple([self.__level])

usr=None
#测试商家端
usr=store(("tests","小飞象","68675462",0,10))