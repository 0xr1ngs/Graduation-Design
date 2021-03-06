# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowFront.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from qqwry import QQwry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Core.base import dns_resolver
import os
import sys
import json
import time
import AddShell
import GenShellPhp
import GenShellJsp
import DisplayShellDataTab


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/knife_easyicon.net.svg'),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shellTableWidget = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shellTableWidget.sizePolicy().hasHeightForWidth())
        self.shellTableWidget.setSizePolicy(sizePolicy)
        self.shellTableWidget.setMinimumSize(QtCore.QSize(256, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.shellTableWidget.setFont(font)
        self.shellTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.shellTableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shellTableWidget.setAutoFillBackground(False)
        self.shellTableWidget.setAutoScrollMargin(15)
        self.shellTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shellTableWidget.setRowCount(0)
        self.shellTableWidget.setObjectName("tableWidget")
        self.shellTableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.shellTableWidget.setHorizontalHeaderItem(7, item)
        self.shellTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.shellTableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.shellTableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 23))
        self.menubar.setObjectName("menubar")
        self.menu_shell = QtWidgets.QMenu(self.menubar)
        self.menu_shell.setObjectName("menu_shell")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.genShellPhp = QtWidgets.QAction(MainWindow)
        self.genShellPhp.setObjectName("genShellPhp")
        self.genShellJsp = QtWidgets.QAction(MainWindow)
        self.genShellJsp.setObjectName("genShellJsp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("aactionExit")
        self.menu_shell.addAction(self.genShellPhp)
        self.menu_shell.addAction(self.genShellJsp)
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_shell.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shell管理工具"))
        item = self.shellTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL链接"))
        item = self.shellTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP地址"))
        item = self.shellTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "密码"))
        item = self.shellTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "物理位置"))
        item = self.shellTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "网站备注"))
        item = self.shellTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "修改时间"))
        item = self.shellTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "流量加密"))
        item = self.shellTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "脚本类型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主页面"))
        self.menu_shell.setTitle(_translate("MainWindow", "生成shell"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.genShellPhp.setText(_translate("MainWindow", "php RSA流量加密"))
        self.genShellJsp.setText(_translate("MainWindow", "jsp Shell"))
        self.actionExit.setText(_translate("MainWindow", "退出（不保存数据）"))

    '''
    +--------------------------------------+
    |     以上是UI设置， 以下是界面功能        |
    +--------------------------------------+    
    '''

    '''
    从cache中读取shell数据，并且重写close方法，在点击关闭后自动保存当前的数据到cache里面
    '''

    def initTable(self):

        #相关参数
        self.tabMaxIndex = 0
        self.tabIndex = [0] #tab的标签序号，用于关闭标签
        self.row_num = -1
        self.index = -1

        '''
        信号和槽函数
        '''
        self.genShellPhp.triggered.connect(self.gen_shell_php)
        self.genShellJsp.triggered.connect(self.gen_shell_Jsp)
        self.actionExit.triggered.connect(quit)
        self.shellTableWidget.customContextMenuRequested.connect(self.generateMenu)
        self.shellTableWidget.doubleClicked.connect(self.shellTableDoubleClicked)
        self.ds = DisplayShellDataTab.DisplayShellData(self)

        '''
        从cache中读取数据，也可能没有
        '''
        try:
            current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
            with open(current_path + "/Cache/db.json", "r") as f:
                d = json.load(f)
                for index, data in d.items():
                    self.shellTableWidget.setRowCount(int(index) + 1)
                    # 添加URL
                    newItem = QtWidgets.QTableWidgetItem(data["URL链接"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 0, newItem)

                    # 添加IP
                    newItem = QtWidgets.QTableWidgetItem(data["IP地址"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 1, newItem)

                    # 添加密码
                    newItem = QtWidgets.QTableWidgetItem(data["密码"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 2, newItem)

                    # 添加物理地址
                    newItem = QtWidgets.QTableWidgetItem(data["物理位置"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 3, newItem)

                    # 添加备注
                    newItem = QtWidgets.QTableWidgetItem(data["网站备注"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 4, newItem)

                    # 添加时间
                    newItem = QtWidgets.QTableWidgetItem(data["修改时间"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 5, newItem)

                    # 流量加密选项
                    newItem = QtWidgets.QTableWidgetItem(data["流量加密"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 6, newItem)

                    # 脚本类型选项
                    newItem = QtWidgets.QTableWidgetItem(data["脚本类型"])
                    newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.shellTableWidget.setItem(int(index), 7, newItem)
        except:
            pass

        self.shellTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.shellTableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.shellTableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.shellTableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

    '''
    重写close方法，使得退出之前自动保存shell数据
    '''

    def closeEvent(self, Event):
        if self.index != -1:
            js = {}
            current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
            for i in range(self.index + 1):
                data = {}
                data["URL链接"] = self.shellTableWidget.item(i, 0).text()
                data["IP地址"] = self.shellTableWidget.item(i, 1).text()
                data["密码"] = self.shellTableWidget.item(i, 2).text()
                data["物理位置"] = self.shellTableWidget.item(i, 3).text()
                data["网站备注"] = self.shellTableWidget.item(i, 4).text()
                data["修改时间"] = self.shellTableWidget.item(i, 5).text()
                data["流量加密"] = self.shellTableWidget.item(i, 6).text()
                data["脚本类型"] = self.shellTableWidget.item(i, 7).text()
                js[i] = data

            with open(current_path + "/Cache/db.json", "w") as f:
                json.dump(js, f)
                # print("加载入文件完成...")
        Event.accept()

    '''
    生成全加密流量的shell
    '''

    def gen_shell_php(self):
        phpShell = GenShellPhp.Ui_Dialog()
        phpShell.exec()

    def gen_shell_Jsp(self):
        jspShell = GenShellJsp.Ui_Dialog()
        jspShell.exec()

    '''
    展示添加数据页面
    '''

    def addShell(self):
        dg = AddShell.Ui_dialog()
        dg.signalDgData.connect(self.dealEmitSlot)
        dg.exec()

    '''
    处理窗口关闭前传过来的URL等数据
    '''

    def dealEmitSlot(self, data):
        url = data[0]
        password = data[1]
        memo = data[2]
        UseRSA = data[3]
        script = data[4]
        if self.row_num == -1:
            self.index = self.shellTableWidget.rowCount()
            self.shellTableWidget.setRowCount(self.index + 1)
        else:
            self.index = self.row_num

        # 添加URL
        newItem = QtWidgets.QTableWidgetItem(url)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 0, newItem)

        # 添加IP
        ip = dns_resolver(url)
        newItem = QtWidgets.QTableWidgetItem(ip)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 1, newItem)

        # 添加密码
        newItem = QtWidgets.QTableWidgetItem(password)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 2, newItem)

        # 添加物理地址
        q = QQwry()
        q.load_file(os.path.dirname(__file__) + '/qqwry.dat')
        try:
            res = q.lookup(ip)
            addr = res[0] + ' ' + res[1]
        except:
            addr = ''
        newItem = QtWidgets.QTableWidgetItem(addr)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 3, newItem)

        # 添加备注
        newItem = QtWidgets.QTableWidgetItem(memo)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 4, newItem)

        # 添加时间
        newItem = QtWidgets.QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 5, newItem)

        # 是否进行流量加密
        if UseRSA:
            newItem = QtWidgets.QTableWidgetItem('是')
        else:
            newItem = QtWidgets.QTableWidgetItem('否')
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 6, newItem)


        # 添加脚本类型
        newItem = QtWidgets.QTableWidgetItem(script)
        newItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.shellTableWidget.setItem(self.index, 7, newItem)


    '''
    数据列表右键打开菜单
    '''

    def generateMenu(self, pos):
        menu = QtWidgets.QMenu()
        # 计算当前行数
        self.row_num = -1
        for i in self.shellTableWidget.selectionModel().selection().indexes():
            self.row_num = i.row()

        if self.row_num != -1:
            item1 = menu.addAction('打开')
            item1.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/shell_easyicon.svg'))
            item2 = menu.addAction('编辑')
            item2.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/edit_easyicon.svg'))
            item3 = menu.addAction('删除')
            item3.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/delete_easyicon.svg'))
            item4 = menu.addAction('查看')
            item4.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/web_easyicon.svg'))
            action = menu.exec_(self.shellTableWidget.mapToGlobal(pos))

            if action == item1:
                self.ds.displayShell()

            elif action == item2:
                dg = AddShell.Ui_dialog()
                dg.pushButton.setText("保存")

                dg.lineEdit.setText(self.shellTableWidget.item(self.row_num, 0).text())
                dg.lineEdit_2.setText(self.shellTableWidget.item(self.row_num, 2).text())
                dg.lineEdit_3.setText(self.shellTableWidget.item(self.row_num, 4).text())
                if self.shellTableWidget.item(self.row_num, 6).text() == '是':
                    dg.checkBox.setChecked(True)
                dg.signalDgData.connect(self.dealEmitSlot)

                dg.exec()
            elif action == item3:
                self.shellTableWidget.removeRow(self.row_num)
            elif action == item4:
                self.displayWeb(self.shellTableWidget.item(self.row_num, 0).text())
        else:
            item = menu.addAction('新建')
            item.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(sys.argv[0])) + '/Icons/add_button_easyicon.svg'))
            action = menu.exec_(self.shellTableWidget.mapToGlobal(pos))
            if action == item:
                self.addShell()

    '''
    双击数据列表时，展示数据详情
    '''

    def shellTableDoubleClicked(self):
        # 计算当前行数
        self.row_num = -1
        for i in self.shellTableWidget.selectionModel().selection().indexes():
            self.row_num = i.row()
        self.ds.displayShell()

    '''
    展示shell得web页面
    '''

    def displayWeb(self, url):
        self.tabMaxIndex += 1
        # tb是TabIndex中的元素
        tb = self.tabMaxIndex
        self.tabIndex.append(tb)

        new_tab = QtWidgets.QWidget()

        self.browser = QWebEngineView()
        self.browser.load(QtCore.QUrl(url))
        self.gridLayout = QtWidgets.QGridLayout(new_tab)
        self.gridLayout.addWidget(self.browser, 0, 0)
        self.tabWidget.addTab(new_tab, url)
        xbutton = QtWidgets.QPushButton("x")
        xbutton.setFixedSize(16, 16)
        xbutton.clicked.connect(lambda: self.delTab(tb))
        # 用index方法找到标签页的相对位置
        self.tabWidget.tabBar().setTabButton(self.tabIndex.index(tb), self.tabWidget.tabBar().RightSide, xbutton)
        self.tabWidget.setCurrentIndex(self.tabIndex.index(tb))

    '''
    删除标签页的方法
    '''

    def delTab(self, tb):
        # 依据相对位置进行tab页面的删除
        self.tabWidget.removeTab(self.tabIndex.index(tb))
        self.tabIndex.remove(tb)
