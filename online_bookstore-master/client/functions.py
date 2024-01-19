from sql import DB

def regist_check_usr_id(usr_id,type,cursor):
    #长度检查
    if(len(usr_id)==0):
        return False,"用户ID不能为空。"
    elif(len(usr_id)<5):
        return False,"用户ID过短。"
    elif(len(usr_id)>25):
        return False,"用户ID过长。"
    #字符合法性检查
    legal=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    for char in usr_id:
        if(char not in legal):
            return False,"用户ID中出现非法字符。"
    #用户ID数据冲突检查
    if(type==0):
        ids=DB.get_consuID(cursor)
    elif(type==1):
        ids=DB.get_storeID(cursor)
    if(len(ids)>0):
        for id in ids:
            id_str=id[0].split('_')
            if usr_id == id_str[1]:
                return False,"该用户ID已被占用。"
    return True,None
    
def regist_check_pswd(pswd,pswd_again):
    #长度检查
    if(len(pswd)==0):
        return False,"密码不能为空。"
    elif(len(pswd)<8):
        return False,"密码长度过短。"
    elif(len(pswd)>16):
        return False,"密码长度过长。"
    #字符合法性检查
    legal=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*_')
    for char in pswd:
        if(char not in legal):
            return False,"密码中出现非法字符。"
    #密码一致性检查
    if(pswd!=pswd_again):
        return False,"两次输入的密码不一致。"
    return True,None
    
def regist_check_usr_name(usr_name,cursor):
    #长度检查
    if(len(usr_name)==0):
        return False,"用户名不能为空。"
    # elif(len(usr_name)<5):
    #     return False,"用户名过短。"
    elif(len(usr_name)>15):
        return False,"用户名过长。"
    #字符合法性检查
    illegal=set('（）(){ }<>[],.。，\'\"\n\r\t')
    for char in usr_name:
        if(char in illegal):
            return False,"用户名中出现非法字符。"
    #用户ID数据冲突检查
    names=DB.get_consuName(cursor)
    if(len(names)>0):
        for name in names:
            if usr_name == name[0]:
                return False,"该用户名已被占用。"
    return True,None
    
def regist_check_phone_number(phone_number):
    #长度检查
    if(len(phone_number)==0):
        return False,"电话号码不能为空。"
    elif(len(phone_number)<7 or len(phone_number)>11):
        return False,"电话号码长度不正确。"
    #字符合法性检查
    legal=set('0123456789')
    for char in phone_number:
        if(char not in legal):
            return False,"电话号码中不能出现数字以外的字符。"
    return True,None
    
def regist_check_store_name(store_name,cursor):
    #长度检查
    if(len(store_name)==0):
        return False,"店铺名称不能为空。"
    elif(len(store_name)>35):
        return False,"店铺名称超长。"
    if(store_name.find(' ')!=-1):
        return False,"店铺名称中不能包含空格"
    store_names=DB.get_storeName(cursor)
    if(len(store_names)>0):
        for name in store_names:
            if(store_name == name[0]):
                return False,"该店铺名称已被占用。"
    return True,None
    
def login_check(usr_id,pswd,type,cursor):
    if(type==0):
        usr_id="consu_{}".format(usr_id)
        ids=DB.get_consuID(cursor)
    elif(type==1):
        usr_id="store_{}".format(usr_id)
        ids=DB.get_storeID(cursor)
    for id in ids:
        if(usr_id==id[0]):
            p=DB.get_PW(cursor,usr_id)
            if(pswd==p[0]):
                return True,True
            else:
                return True,False
    return False,False

def check_store_name(store_name,cursor):
    return regist_check_store_name(store_name,cursor)

def check_usr_name(usr_name,cursor):
    return regist_check_usr_name(usr_name,cursor)

def check_phone_number(phone_number):
    return regist_check_phone_number(phone_number)

#加载商家用户
def load_store_user(usr_id,cursor):
    return ()

#加载消费者用户
def load_consu_user(usr_id,cursor):
    return ()