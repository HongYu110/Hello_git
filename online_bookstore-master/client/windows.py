from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from Ui_welcomeWidget import Ui_welcomeWidget as welcomeWidget
from Ui_registWidget import Ui_registWidget as registWidget
from Ui_storeManageWidget import Ui_storeManageWidget as storeManageWidget
from Ui_storeMainWidget import Ui_storeMainWidget as storeMainWidget
from Ui_storeEditWidget import Ui_storeEditWidget as storeEditWidget
import functions as f
import time
import user

#开始界面
class welcomeWindow(QWidget,welcomeWidget):
    __registeWindow=None
    __storeMainWindow=None
    def __init__(self,database):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.show()
        self.registButton.clicked.connect(self.regist)
        self.loginButton.clicked.connect(self.login)
        self.database=database
        self.cursor=database.cursor
        self.db=database.db
    def regist(self):#注册键槽函数
        welcomeWindow.__registWindow=registWindow(self.database)
    def login(self):
        legal_id,legal_pswd=f.login_check(self.usr_id.text(),self.pswd.text(),self.type.currentIndex(),self.cursor)
        if(legal_id and legal_pswd):
            if(self.type.currentIndex()==0):
                id=f"consu_{self.usr_id.text()}"
            elif(self.type.currentIndex()==1):
                id=f"store_{self.usr_id.text()}"
            print(f"At {time.time()} user {id} login success.")
            #登陆完成部分#
            type=self.type.currentIndex()
            if(type==0):
                user.usr=user.consumer(f.load_consu_user(self.usr_id.text(),self.cursor))
                pass#消费者用户主界面
            elif(type==1):
                welcomeWindow.__storemainWindow=storeMainWindow(self.database)
                user.usr=user.store(f.load_store_user(self.usr_id.text(),self.cursor))
            self.close()
        if(not legal_id):
            message=QMessageBox.warning(self,"提示信息","用户ID错误！",QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        else:
            if(not legal_pswd):
                message=QMessageBox.warning(self,"提示信息","密码错误！",QMessageBox.Ok,QMessageBox.Ok)
                if(message==QMessageBox.Ok):
                    return

#注册界面
class registWindow(QWidget,registWidget):
    def __init__(self,database):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.show()
        self.confirmButton.clicked.connect(self.confirm)
        self.type.currentIndexChanged.connect(self.type_switched)
        self.label_7.hide()
        self.store_name.hide()
        self.database=database
        self.cursor=database.cursor
        self.db=database.db
    def confirm(self):
        legal_usr_id,info_usr_id=f.regist_check_usr_id(self.usr_id.text(),self.type.currentIndex(),self.cursor)
        if(not legal_usr_id):
            message=QMessageBox.information(self,"提示信息",info_usr_id,QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        legal_pswd,info_pswd=f.regist_check_pswd(self.pswd.text(),self.pswd_again.text())
        if(not legal_pswd):
            message=QMessageBox.information(self,"提示信息",info_pswd,QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        legal_phone_number,info_phone_number=f.regist_check_phone_number(self.phone_number.text())
        if(not legal_phone_number):
            message=QMessageBox.information(self,"提示信息",info_phone_number,QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        if(self.type.currentIndex()==0):
            legal_usr_name,info_usr_name=f.regist_check_usr_name(self.usr_name.text(),self.cursor)
            if(not legal_usr_name):
                message=QMessageBox.information(self,"提示信息",info_usr_name,QMessageBox.Ok,QMessageBox.Ok)
                if(message==QMessageBox.Ok):
                    return
            regist_info=(f"consu_{self.usr_id.text()}",self.usr_name.text(),self.pswd.text(),self.phone_number.text(),1001,f"shopcart_{self.database.get_shopCart()+1}",0)
        elif(self.type.currentIndex()==1):
            legal_store_name,info_store_name=f.regist_check_store_name(self.store_name.text(),self.cursor)
            if(not legal_store_name):
                message=QMessageBox.information(self,"提示信息",info_store_name,QMessageBox.Ok,QMessageBox.Ok)
                if(message==QMessageBox.Ok):
                    return
            regist_info=(f"store_{self.usr_id.text()}",self.store_name.text(),self.pswd.text(),self.phone_number.text(),1001,f"shopcart_{0}",0)
        self.database.set_usr(regist_info)
        print("Regist success : {}".format(regist_info))
        message=QMessageBox.information(self,"提示信息","注册成功！",QMessageBox.Ok,QMessageBox.Ok)
        if(message==QMessageBox.Ok):
            self.close()
            return
    def type_switched(self):
        if(self.type.currentIndex()==1):
            self.label_7.show()
            self.store_name.show()
            self.label_5.hide()
            self.usr_name.hide()
        elif(self.type.currentIndex()==0):
            self.label_5.show()
            self.usr_name.show()
            self.label_7.hide()
            self.store_name.hide()

#商家用户主界面
class storeMainWindow(QWidget,storeMainWidget):
    __storeEditWindow=None
    __storeEditWindow=None
    __welcomeWindow=None
    def __init__(self,database):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.show()
        self.logoutButton.clicked.connect(self.logout)
        self.editStoreBotton.clicked.connect(self.edit_store)
        self.goodsAndOrdersButton.clicked.connect(self.goods_and_orders)
        self.database=database
        self.cursor=database.cursor
        self.db=database.db
        self.print_info()
        self.setWindowTitle("商家：{}".format(user.usr.getInfo()[1]))
    def edit_store(self):
        if(user.usr.getInfo()[3]):
            message=QMessageBox.information(self,"提示信息","您已被封禁，不能编辑个人信息",QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
            if(message==QMessageBox.Ok):
                return
        else:
            storeMainWindow.__storeManageWindow=storeEditWindow(self.database)
            self.close()
    def goods_and_orders(self):
        if(user.usr.getInfo()[3]):
            message=QMessageBox.information(self,"提示信息","您已被封禁，不能管理商品以及订单",QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
            if(message==QMessageBox.Ok):
                return
        else:
            storeMainWindow.__storeEditWindow=storeManageWindow(self.database)
            self.close()
    def logout(self):
        message=QMessageBox.information(self,"提示信息","确定要退出当前账户？",QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if(message==QMessageBox.Ok):
            storeMainWindow.__welcomeWindow=welcomeWindow(self.database)
            user.usr=None
            self.close()
    def print_info(self):
        self.store_id.setText(user.usr.getInfo()[0])
        self.store_name.setText(user.usr.getInfo()[1])
        self.store_level.setText(str(user.usr.getInfo()[4]))
        if(user.usr.getInfo()[3]):
            self.store_ban.setText("封禁")
        else:
            self.store_ban.setText("正常")

#商家用户管理界面
class storeManageWindow(QWidget,storeManageWidget):
    __storeMainWindow=None
    def __init__(self,database):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.show()
        self.backButton.clicked.connect(self.back)
        self.database=database
        self.cursor=database.cursor
        self.db=database.db
    def back(self):
        storeManageWindow.__storeMainWindow=storeMainWindow(self.database)
        self.close()

#商家用户编辑个人信息界面
class storeEditWindow(QWidget,storeEditWidget):
    __storeMainWindow=None
    def __init__(self,database):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.show()
        self.backButton.clicked.connect(self.back)
        self.confirmButton.clicked.connect(self.confirm)
        self.resetButton.clicked.connect(self.reset)
        self.database=database
        self.cursor=database.cursor
        self.db=database.db
        self.preset_values()
    def back(self):
        storeEditWindow.__storeMainWindow=storeMainWindow(self.database)
        self.close()
    def confirm(self):
        legal_store_name,info_store_name=f.check_store_name(self.store_name.text(),self.cursor)
        if(not legal_store_name):
            message=QMessageBox.information(self,"提示信息",info_store_name,QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        legal_phone_number,info_phone_number=f.regist_check_phone_number(self.phone_number.text())
        if(not legal_phone_number):
            message=QMessageBox.information(self,"提示信息",info_phone_number,QMessageBox.Ok,QMessageBox.Ok)
            if(message==QMessageBox.Ok):
                return
        user.usr.setName(self.store_name.text())
        user.usr.setPhone(self.phone_num.text())
        #数据库更新
        message=QMessageBox.information(self,"提示信息","更改成功！",QMessageBox.Ok | QMessageBox.Cancel,QMessageBox.Cancel)
        if(message==QMessageBox.Ok):
            return
    def reset(self):
        self.preset_values()
    def preset_values(self):
        self.store_id.setText(user.usr.getInfo()[0])
        self.store_name.setText(user.usr.getInfo()[1])
        self.phone_num.setText(user.usr.getInfo()[2])
        if(user.usr.getInfo()[3]):
            self.store_ban.setText("封禁")
        else:
            self.store_ban.setText("正常")
        self.store_level.setText(str(user.usr.getInfo()[4]))