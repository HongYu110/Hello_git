# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\online_bookstore\client\ui\storeMainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_storeMainWidget(object):
    def setupUi(self, storeMainWidget):
        storeMainWidget.setObjectName("storeMainWidget")
        storeMainWidget.resize(1280, 720)
        self.cards = QtWidgets.QTableView(storeMainWidget)
        self.cards.setGeometry(QtCore.QRect(50, 270, 461, 361))
        self.cards.setObjectName("cards")
        self.logoutButton = QtWidgets.QPushButton(storeMainWidget)
        self.logoutButton.setGeometry(QtCore.QRect(50, 650, 131, 41))
        self.logoutButton.setObjectName("logoutButton")
        self.label_1 = QtWidgets.QLabel(storeMainWidget)
        self.label_1.setGeometry(QtCore.QRect(50, 250, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(storeMainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 270, 271, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.card_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.card_id.setObjectName("card_id")
        self.verticalLayout_2.addWidget(self.card_id)
        self.verticalLayout_1.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.card_type = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.card_type.setObjectName("card_type")
        self.verticalLayout_3.addWidget(self.card_type)
        self.verticalLayout_1.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.card_level = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.card_level.setObjectName("card_level")
        self.verticalLayout_4.addWidget(self.card_level)
        self.verticalLayout_1.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.card_time = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.card_time.setObjectName("card_time")
        self.verticalLayout_5.addWidget(self.card_time)
        self.verticalLayout_1.addLayout(self.verticalLayout_5)
        self.genCardButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.genCardButton.setObjectName("genCardButton")
        self.verticalLayout_1.addWidget(self.genCardButton)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(storeMainWidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(940, 270, 291, 361))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.consu_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.consu_id.setObjectName("consu_id")
        self.horizontalLayout_1.addWidget(self.consu_id)
        self.id_confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.id_confirm.setObjectName("id_confirm")
        self.horizontalLayout_1.addWidget(self.id_confirm)
        self.verticalLayout_7.addLayout(self.horizontalLayout_1)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.card_id_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.card_id_input.setObjectName("card_id_input")
        self.horizontalLayout_2.addWidget(self.card_id_input)
        self.confirm_card = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.confirm_card.setObjectName("confirm_card")
        self.horizontalLayout_2.addWidget(self.confirm_card)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.sendCardButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.sendCardButton.setObjectName("sendCardButton")
        self.verticalLayout_6.addWidget(self.sendCardButton)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(storeMainWidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(510, 20, 551, 191))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.store_id = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.store_id.setText("")
        self.store_id.setObjectName("store_id")
        self.horizontalLayout_4.addWidget(self.store_id)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.store_name = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.store_name.setText("")
        self.store_name.setObjectName("store_name")
        self.horizontalLayout_5.addWidget(self.store_name)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.store_level = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.store_level.setText("")
        self.store_level.setObjectName("store_level")
        self.horizontalLayout_6.addWidget(self.store_level)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.store_ban = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.store_ban.setText("")
        self.store_ban.setObjectName("store_ban")
        self.horizontalLayout_7.addWidget(self.store_ban)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editStoreBotton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.editStoreBotton.setObjectName("editStoreBotton")
        self.horizontalLayout_3.addWidget(self.editStoreBotton)
        self.goodsAndOrdersButton = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.goodsAndOrdersButton.setObjectName("goodsAndOrdersButton")
        self.horizontalLayout_3.addWidget(self.goodsAndOrdersButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.picture = QtWidgets.QGraphicsView(storeMainWidget)
        self.picture.setGeometry(QtCore.QRect(160, 20, 200, 200))
        self.picture.setObjectName("picture")
        self.line = QtWidgets.QFrame(storeMainWidget)
        self.line.setGeometry(QtCore.QRect(0, 230, 1281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(storeMainWidget)
        QtCore.QMetaObject.connectSlotsByName(storeMainWidget)

    def retranslateUi(self, storeMainWidget):
        _translate = QtCore.QCoreApplication.translate
        storeMainWidget.setWindowTitle(_translate("storeMainWidget", "Form"))
        self.logoutButton.setText(_translate("storeMainWidget", "注销"))
        self.label_1.setText(_translate("storeMainWidget", "会员卡信息"))
        self.label_2.setText(_translate("storeMainWidget", "会员卡ID  "))
        self.label_3.setText(_translate("storeMainWidget", "会员卡类型"))
        self.label_4.setText(_translate("storeMainWidget", "会员卡等级"))
        self.label.setText(_translate("storeMainWidget", "到期时间  "))
        self.genCardButton.setText(_translate("storeMainWidget", "生成卡片"))
        self.label_5.setText(_translate("storeMainWidget", "输入用户ID"))
        self.id_confirm.setText(_translate("storeMainWidget", "确定"))
        self.label_6.setText(_translate("storeMainWidget", "输入会员卡ID"))
        self.confirm_card.setText(_translate("storeMainWidget", "确定"))
        self.sendCardButton.setText(_translate("storeMainWidget", "发送卡片"))
        self.label_7.setText(_translate("storeMainWidget", "商家用户ID："))
        self.label_8.setText(_translate("storeMainWidget", "店铺名称："))
        self.label_9.setText(_translate("storeMainWidget", "店铺等级："))
        self.label_10.setText(_translate("storeMainWidget", "店铺状态："))
        self.editStoreBotton.setText(_translate("storeMainWidget", "编辑店铺"))
        self.goodsAndOrdersButton.setText(_translate("storeMainWidget", "商品、订单管理"))
