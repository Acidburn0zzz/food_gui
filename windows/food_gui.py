#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Do not touch!
# Magick!
 
import os, shutil,  sys
from PyQt4 import QtCore, QtGui

#from about import Ui_About_Window
#from add import Ui_Add
#from calcwin import Ui_Calc_Window
#from complete import Ui_Complete_Window
#from dbcp import Ui_db_cp_window
#from dbselect import Ui_DB_Select
#from edit import Ui_Edit
#from help import Ui_Help_Window
#from language import Ui_Language
#from notfound import Ui_NotFound
#from search import Ui_Search_Window
#from mainwin import Ui_Food

db = "db.dat"
lang = "ENG"


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


# Graphic object that described in source files

class Ui_Food(object):
    def setupUi(self, Food):
        Food.setObjectName(_fromUtf8("Food"))
        Food.resize(421, 266)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Food.sizePolicy().hasHeightForWidth())
        Food.setSizePolicy(sizePolicy)
        Food.setMinimumSize(QtCore.QSize(421, 266))
        self.centralwidget = QtGui.QWidget(Food)
        self.centralwidget.setMinimumSize(QtCore.QSize(421, 225))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setMinimumSize(QtCore.QSize(100, 25))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_line.setText(_fromUtf8(""))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.horizontalLayout.addWidget(self.search_line)
        self.mass_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mass_lab.sizePolicy().hasHeightForWidth())
        self.mass_lab.setSizePolicy(sizePolicy)
        self.mass_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.mass_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.mass_lab.setObjectName(_fromUtf8("mass_lab"))
        self.horizontalLayout.addWidget(self.mass_lab)
        self.mass_line = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mass_line.sizePolicy().hasHeightForWidth())
        self.mass_line.setSizePolicy(sizePolicy)
        self.mass_line.setMinimumSize(QtCore.QSize(100, 25))
        self.mass_line.setMaximumSize(QtCore.QSize(100, 25))
        self.mass_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mass_line.setObjectName(_fromUtf8("mass_line"))
        self.horizontalLayout.addWidget(self.mass_line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_lab.sizePolicy().hasHeightForWidth())
        self.lip_lab.setSizePolicy(sizePolicy)
        self.lip_lab.setMinimumSize(QtCore.QSize(175, 25))
        self.lip_lab.setMaximumSize(QtCore.QSize(175, 25))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.horizontalLayout_4.addWidget(self.lip_lab)
        self.lip_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_sec_lab.sizePolicy().hasHeightForWidth())
        self.lip_sec_lab.setSizePolicy(sizePolicy)
        self.lip_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.lip_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lip_sec_lab.setObjectName(_fromUtf8("lip_sec_lab"))
        self.horizontalLayout_4.addWidget(self.lip_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_lab.sizePolicy().hasHeightForWidth())
        self.ccal_lab.setSizePolicy(sizePolicy)
        self.ccal_lab.setMinimumSize(QtCore.QSize(175, 25))
        self.ccal_lab.setMaximumSize(QtCore.QSize(175, 25))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.horizontalLayout_6.addWidget(self.ccal_lab)
        self.ccal_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_sec_lab.sizePolicy().hasHeightForWidth())
        self.ccal_sec_lab.setSizePolicy(sizePolicy)
        self.ccal_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.ccal_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ccal_sec_lab.setObjectName(_fromUtf8("ccal_sec_lab"))
        self.horizontalLayout_6.addWidget(self.ccal_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_lab.sizePolicy().hasHeightForWidth())
        self.carb_lab.setSizePolicy(sizePolicy)
        self.carb_lab.setMinimumSize(QtCore.QSize(175, 25))
        self.carb_lab.setMaximumSize(QtCore.QSize(175, 25))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.horizontalLayout_5.addWidget(self.carb_lab)
        self.carb_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_sec_lab.sizePolicy().hasHeightForWidth())
        self.carb_sec_lab.setSizePolicy(sizePolicy)
        self.carb_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.carb_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carb_sec_lab.setObjectName(_fromUtf8("carb_sec_lab"))
        self.horizontalLayout_5.addWidget(self.carb_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbut.sizePolicy().hasHeightForWidth())
        self.searchbut.setSizePolicy(sizePolicy)
        self.searchbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        self.horizontalLayout_2.addWidget(self.searchbut)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.substitutebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substitutebut.sizePolicy().hasHeightForWidth())
        self.substitutebut.setSizePolicy(sizePolicy)
        self.substitutebut.setMinimumSize(QtCore.QSize(100, 25))
        self.substitutebut.setMaximumSize(QtCore.QSize(100, 25))
        self.substitutebut.setDefault(True)
        self.substitutebut.setObjectName(_fromUtf8("substitutebut"))
        self.horizontalLayout_2.addWidget(self.substitutebut)
        self.calcbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcbut.sizePolicy().hasHeightForWidth())
        self.calcbut.setSizePolicy(sizePolicy)
        self.calcbut.setMinimumSize(QtCore.QSize(100, 25))
        self.calcbut.setMaximumSize(QtCore.QSize(100, 25))
        self.calcbut.setDefault(True)
        self.calcbut.setObjectName(_fromUtf8("calcbut"))
        self.horizontalLayout_2.addWidget(self.calcbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_lab.sizePolicy().hasHeightForWidth())
        self.prot_lab.setSizePolicy(sizePolicy)
        self.prot_lab.setMinimumSize(QtCore.QSize(175, 25))
        self.prot_lab.setMaximumSize(QtCore.QSize(175, 25))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.horizontalLayout_3.addWidget(self.prot_lab)
        self.prot_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_sec_lab.sizePolicy().hasHeightForWidth())
        self.prot_sec_lab.setSizePolicy(sizePolicy)
        self.prot_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.prot_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prot_sec_lab.setObjectName(_fromUtf8("prot_sec_lab"))
        self.horizontalLayout_3.addWidget(self.prot_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_lab.sizePolicy().hasHeightForWidth())
        self.glyc_lab.setSizePolicy(sizePolicy)
        self.glyc_lab.setMinimumSize(QtCore.QSize(175, 25))
        self.glyc_lab.setMaximumSize(QtCore.QSize(175, 25))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.horizontalLayout_7.addWidget(self.glyc_lab)
        self.glyc_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_sec_lab.sizePolicy().hasHeightForWidth())
        self.glyc_sec_lab.setSizePolicy(sizePolicy)
        self.glyc_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.glyc_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.glyc_sec_lab.setObjectName(_fromUtf8("glyc_sec_lab"))
        self.horizontalLayout_7.addWidget(self.glyc_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 2, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 111, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        Food.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Food)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        Food.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Food)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Food.setStatusBar(self.statusbar)
        self.menu_add = QtGui.QAction(Food)
        self.menu_add.setObjectName(_fromUtf8("menu_add"))
        self.menu_edit = QtGui.QAction(Food)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_create = QtGui.QAction(Food)
        self.menu_create.setObjectName(_fromUtf8("menu_create"))
        self.menu_dbcp = QtGui.QAction(Food)
        self.menu_dbcp.setObjectName(_fromUtf8("menu_dbcp"))
        self.menu_exit = QtGui.QAction(Food)
        self.menu_exit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.menu_exit.setMenuRole(QtGui.QAction.QuitRole)
        self.menu_exit.setPriority(QtGui.QAction.HighPriority)
        self.menu_exit.setObjectName(_fromUtf8("menu_exit"))
        self.menu_about = QtGui.QAction(Food)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        self.menu_dbsel = QtGui.QAction(Food)
        self.menu_dbsel.setObjectName(_fromUtf8("menu_dbsel"))
        self.menu_search = QtGui.QAction(Food)
        self.menu_search.setObjectName(_fromUtf8("menu_search"))
        self.menu_lang = QtGui.QAction(Food)
        self.menu_lang.setObjectName(_fromUtf8("menu_lang"))
        self.menu_help = QtGui.QAction(Food)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        self.menu.addAction(self.menu_search)
        self.menu.addAction(self.menu_add)
        self.menu.addAction(self.menu_edit)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_create)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_exit)
        self.menu_2.addAction(self.menu_help)
        self.menu_2.addAction(self.menu_about)
        self.menu_3.addAction(self.menu_dbsel)
        self.menu_3.addAction(self.menu_dbcp)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.menu_lang)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        #self.retranslateUi(Food)
        QtCore.QObject.connect(self.menu_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), Food.close)
        QtCore.QMetaObject.connectSlotsByName(Food)

    def retranslateUi(self, Food):
        Food.setWindowTitle(_translate("Food", "Food", None))
        self.mass_lab.setText(_translate("Food", "Масса, г", None))
        self.lip_lab.setText(_translate("Food", "Жиры", None))
        self.lip_sec_lab.setText(_translate("Food", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.ccal_lab.setText(_translate("Food", "Калорийность, ккал", None))
        self.ccal_sec_lab.setText(_translate("Food", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.carb_lab.setText(_translate("Food", "Углеводы", None))
        self.carb_sec_lab.setText(_translate("Food", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.searchbut.setText(_translate("Food", "Окно поиска", None))
        self.substitutebut.setText(_translate("Food", "Подставить", None))
        self.calcbut.setText(_translate("Food", "Посчитать", None))
        self.prot_lab.setText(_translate("Food", "Белки", None))
        self.prot_sec_lab.setText(_translate("Food", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.glyc_lab.setText(_translate("Food", "Гликемический индекс", None))
        self.glyc_sec_lab.setText(_translate("Food", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.menu.setTitle(_translate("Food", "&Меню", None))
        self.menu_2.setTitle(_translate("Food", "&Справка", None))
        self.menu_3.setTitle(_translate("Food", "&Настройки", None))
        self.menu_add.setText(_translate("Food", "&Добавить продукт в базу данных", None))
        self.menu_add.setShortcut(_translate("Food", "Ctrl+N", None))
        self.menu_edit.setText(_translate("Food", "&Редактировать базу данных", None))
        self.menu_edit.setShortcut(_translate("Food", "Ctrl+W", None))
        self.menu_create.setText(_translate("Food", "&Создать меню", None))
        self.menu_create.setShortcut(_translate("Food", "Ctrl+M", None))
        self.menu_dbcp.setText(_translate("Food", "С&копировать базу данных", None))
        self.menu_exit.setText(_translate("Food", "&Выход", None))
        self.menu_exit.setShortcut(_translate("Food", "Ctrl+Q", None))
        self.menu_about.setText(_translate("Food", "&О программе", None))
        self.menu_dbsel.setText(_translate("Food", "Выбрать &базу данных", None))
        self.menu_search.setText(_translate("Food", "&Искать продукт в базе данных", None))
        self.menu_search.setShortcut(_translate("Food", "Ctrl+S", None))
        self.menu_lang.setText(_translate("Food", "Выбрать &язык", None))
        self.menu_help.setText(_translate("Food", "&Помощь", None))
        self.menu_help.setShortcut(_translate("Food", "F1", None))


class Ui_About_Window(object):
    def setupUi(self, About_Window):
        About_Window.setObjectName(_fromUtf8("About_Window"))
        About_Window.resize(361, 236)
        About_Window.setMinimumSize(QtCore.QSize(361, 236))
        self.centralwidget = QtGui.QWidget(About_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(361, 236))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.about = QtGui.QTextBrowser(self.centralwidget)
        self.about.setEnabled(True)
        self.about.setFocusPolicy(QtCore.Qt.NoFocus)
        self.about.setAutoFillBackground(True)
        self.about.setObjectName(_fromUtf8("about"))
        self.gridLayout.addWidget(self.about, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QtCore.QSize(100, 25))
        self.exit.setMaximumSize(QtCore.QSize(100, 25))
        self.exit.setDefault(True)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.horizontalLayout.addWidget(self.exit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        About_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(About_Window)
        QtCore.QMetaObject.connectSlotsByName(About_Window)

    def retranslateUi(self, About_Window):
        About_Window.setWindowTitle(_translate("About_Window", "О программе", None))
        self.about.setHtml(_translate("About_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Food 1.1.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Лицензия: GPL</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Простенькая программа-калькулятор на питоне, подсчитывающая БЖУ, калорийность и гликемический индекс употребляемых продуктов на основании базы данных.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Евгений Алексеев aka arcanis</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>", None))
        self.exit.setText(_translate("About_Window", "Закрыть", None))


class Ui_Add(object):
    def setupUi(self, Add):
        Add.setObjectName(_fromUtf8("Add"))
        Add.resize(321, 225)
        Add.setMinimumSize(QtCore.QSize(321, 225))
        self.centralwidget = QtGui.QWidget(Add)
        self.centralwidget.setMinimumSize(QtCore.QSize(321, 225))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.subs_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subs_lab.sizePolicy().hasHeightForWidth())
        self.subs_lab.setSizePolicy(sizePolicy)
        self.subs_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.subs_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.subs_lab.setObjectName(_fromUtf8("subs_lab"))
        self.horizontalLayout.addWidget(self.subs_lab)
        self.subs_line = QtGui.QLineEdit(self.centralwidget)
        self.subs_line.setMinimumSize(QtCore.QSize(100, 25))
        self.subs_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.subs_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subs_line.setObjectName(_fromUtf8("subs_line"))
        self.horizontalLayout.addWidget(self.subs_line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_lab.sizePolicy().hasHeightForWidth())
        self.prot_lab.setSizePolicy(sizePolicy)
        self.prot_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.prot_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.horizontalLayout_2.addWidget(self.prot_lab)
        self.prot_line = QtGui.QLineEdit(self.centralwidget)
        self.prot_line.setMinimumSize(QtCore.QSize(100, 25))
        self.prot_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prot_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prot_line.setObjectName(_fromUtf8("prot_line"))
        self.horizontalLayout_2.addWidget(self.prot_line)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_lab.sizePolicy().hasHeightForWidth())
        self.lip_lab.setSizePolicy(sizePolicy)
        self.lip_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.lip_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.horizontalLayout_3.addWidget(self.lip_lab)
        self.lip_line = QtGui.QLineEdit(self.centralwidget)
        self.lip_line.setMinimumSize(QtCore.QSize(100, 25))
        self.lip_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lip_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lip_line.setObjectName(_fromUtf8("lip_line"))
        self.horizontalLayout_3.addWidget(self.lip_line)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_lab.sizePolicy().hasHeightForWidth())
        self.carb_lab.setSizePolicy(sizePolicy)
        self.carb_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.carb_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.horizontalLayout_4.addWidget(self.carb_lab)
        self.carb_line = QtGui.QLineEdit(self.centralwidget)
        self.carb_line.setMinimumSize(QtCore.QSize(100, 25))
        self.carb_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carb_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carb_line.setObjectName(_fromUtf8("carb_line"))
        self.horizontalLayout_4.addWidget(self.carb_line)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_lab.sizePolicy().hasHeightForWidth())
        self.ccal_lab.setSizePolicy(sizePolicy)
        self.ccal_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.horizontalLayout_5.addWidget(self.ccal_lab)
        self.ccal_line = QtGui.QLineEdit(self.centralwidget)
        self.ccal_line.setMinimumSize(QtCore.QSize(100, 25))
        self.ccal_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ccal_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ccal_line.setObjectName(_fromUtf8("ccal_line"))
        self.horizontalLayout_5.addWidget(self.ccal_line)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_lab.sizePolicy().hasHeightForWidth())
        self.glyc_lab.setSizePolicy(sizePolicy)
        self.glyc_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.glyc_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.horizontalLayout_6.addWidget(self.glyc_lab)
        self.glyc_line = QtGui.QLineEdit(self.centralwidget)
        self.glyc_line.setMinimumSize(QtCore.QSize(100, 25))
        self.glyc_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.glyc_line.setText(_fromUtf8(""))
        self.glyc_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.glyc_line.setObjectName(_fromUtf8("glyc_line"))
        self.horizontalLayout_6.addWidget(self.glyc_line)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.horizontalLayout_7.addWidget(self.okbut)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.horizontalLayout_7.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        Add.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Add)
        QtCore.QMetaObject.connectSlotsByName(Add)

    def retranslateUi(self, Add):
        Add.setWindowTitle(_translate("Add", "Добавить", None))
        self.subs_lab.setText(_translate("Add", "Продукт", None))
        self.prot_lab.setText(_translate("Add", "Белки", None))
        self.lip_lab.setText(_translate("Add", "Жиры", None))
        self.carb_lab.setText(_translate("Add", "Углеводы", None))
        self.ccal_lab.setText(_translate("Add", "Калорийность, ккал", None))
        self.glyc_lab.setText(_translate("Add", "Гликемический индекс", None))
        self.okbut.setText(_translate("Add", "Ok", None))
        self.cancelbut.setText(_translate("Add", "Отмена", None))


class Ui_Calc_Window(object):
    def setupUi(self, Calc_Window):
        Calc_Window.setObjectName(_fromUtf8("Calc_Window"))
        Calc_Window.resize(403, 581)
        Calc_Window.setMinimumSize(QtCore.QSize(403, 581))
        self.centralwidget = QtGui.QWidget(Calc_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(403, 581))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lab.sizePolicy().hasHeightForWidth())
        self.search_lab.setSizePolicy(sizePolicy)
        self.search_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.search_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.search_lab.setObjectName(_fromUtf8("search_lab"))
        self.horizontalLayout.addWidget(self.search_lab)
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setMinimumSize(QtCore.QSize(100, 25))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.horizontalLayout.addWidget(self.search_line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mass_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mass_lab.sizePolicy().hasHeightForWidth())
        self.mass_lab.setSizePolicy(sizePolicy)
        self.mass_lab.setMinimumSize(QtCore.QSize(70, 25))
        self.mass_lab.setMaximumSize(QtCore.QSize(70, 25))
        self.mass_lab.setObjectName(_fromUtf8("mass_lab"))
        self.horizontalLayout_2.addWidget(self.mass_lab)
        self.mass_line = QtGui.QLineEdit(self.centralwidget)
        self.mass_line.setMinimumSize(QtCore.QSize(100, 25))
        self.mass_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mass_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mass_line.setObjectName(_fromUtf8("mass_line"))
        self.horizontalLayout_2.addWidget(self.mass_line)
        self.substitutebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substitutebut.sizePolicy().hasHeightForWidth())
        self.substitutebut.setSizePolicy(sizePolicy)
        self.substitutebut.setMinimumSize(QtCore.QSize(100, 25))
        self.substitutebut.setMaximumSize(QtCore.QSize(100, 25))
        self.substitutebut.setDefault(True)
        self.substitutebut.setObjectName(_fromUtf8("substitutebut"))
        self.horizontalLayout_2.addWidget(self.substitutebut)
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbut.sizePolicy().hasHeightForWidth())
        self.searchbut.setSizePolicy(sizePolicy)
        self.searchbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        self.horizontalLayout_2.addWidget(self.searchbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_lab.sizePolicy().hasHeightForWidth())
        self.prot_lab.setSizePolicy(sizePolicy)
        self.prot_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.prot_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.horizontalLayout_3.addWidget(self.prot_lab)
        self.prot_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_sec_lab.sizePolicy().hasHeightForWidth())
        self.prot_sec_lab.setSizePolicy(sizePolicy)
        self.prot_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.prot_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prot_sec_lab.setObjectName(_fromUtf8("prot_sec_lab"))
        self.horizontalLayout_3.addWidget(self.prot_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_lab.sizePolicy().hasHeightForWidth())
        self.lip_lab.setSizePolicy(sizePolicy)
        self.lip_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.lip_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.horizontalLayout_4.addWidget(self.lip_lab)
        self.lip_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_sec_lab.sizePolicy().hasHeightForWidth())
        self.lip_sec_lab.setSizePolicy(sizePolicy)
        self.lip_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.lip_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lip_sec_lab.setObjectName(_fromUtf8("lip_sec_lab"))
        self.horizontalLayout_4.addWidget(self.lip_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_lab.sizePolicy().hasHeightForWidth())
        self.carb_lab.setSizePolicy(sizePolicy)
        self.carb_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.carb_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.horizontalLayout_5.addWidget(self.carb_lab)
        self.carb_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_sec_lab.sizePolicy().hasHeightForWidth())
        self.carb_sec_lab.setSizePolicy(sizePolicy)
        self.carb_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.carb_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carb_sec_lab.setObjectName(_fromUtf8("carb_sec_lab"))
        self.horizontalLayout_5.addWidget(self.carb_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_lab.sizePolicy().hasHeightForWidth())
        self.ccal_lab.setSizePolicy(sizePolicy)
        self.ccal_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.horizontalLayout_6.addWidget(self.ccal_lab)
        self.ccal_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_sec_lab.sizePolicy().hasHeightForWidth())
        self.ccal_sec_lab.setSizePolicy(sizePolicy)
        self.ccal_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.ccal_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ccal_sec_lab.setObjectName(_fromUtf8("ccal_sec_lab"))
        self.horizontalLayout_6.addWidget(self.ccal_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_lab.sizePolicy().hasHeightForWidth())
        self.glyc_lab.setSizePolicy(sizePolicy)
        self.glyc_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.glyc_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.horizontalLayout_7.addWidget(self.glyc_lab)
        self.glyc_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_sec_lab.sizePolicy().hasHeightForWidth())
        self.glyc_sec_lab.setSizePolicy(sizePolicy)
        self.glyc_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.glyc_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.glyc_sec_lab.setObjectName(_fromUtf8("glyc_sec_lab"))
        self.horizontalLayout_7.addWidget(self.glyc_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.searchwinbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchwinbut.sizePolicy().hasHeightForWidth())
        self.searchwinbut.setSizePolicy(sizePolicy)
        self.searchwinbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchwinbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchwinbut.setDefault(True)
        self.searchwinbut.setObjectName(_fromUtf8("searchwinbut"))
        self.horizontalLayout_8.addWidget(self.searchwinbut)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.addbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addbut.sizePolicy().hasHeightForWidth())
        self.addbut.setSizePolicy(sizePolicy)
        self.addbut.setMinimumSize(QtCore.QSize(100, 25))
        self.addbut.setMaximumSize(QtCore.QSize(100, 25))
        self.addbut.setDefault(True)
        self.addbut.setObjectName(_fromUtf8("addbut"))
        self.horizontalLayout_8.addWidget(self.addbut)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        self.text_selected = QtGui.QTextBrowser(self.centralwidget)
        self.text_selected.setMinimumSize(QtCore.QSize(381, 141))
        self.text_selected.setObjectName(_fromUtf8("text_selected"))
        self.gridLayout.addWidget(self.text_selected, 8, 0, 1, 1)
        self.total_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_lab.sizePolicy().hasHeightForWidth())
        self.total_lab.setSizePolicy(sizePolicy)
        self.total_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.total_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.total_lab.setObjectName(_fromUtf8("total_lab"))
        self.gridLayout.addWidget(self.total_lab, 9, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.tot_prot_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_prot_lab.sizePolicy().hasHeightForWidth())
        self.tot_prot_lab.setSizePolicy(sizePolicy)
        self.tot_prot_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.tot_prot_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.tot_prot_lab.setObjectName(_fromUtf8("tot_prot_lab"))
        self.horizontalLayout_9.addWidget(self.tot_prot_lab)
        self.tot_prot_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_prot_sec_lab.sizePolicy().hasHeightForWidth())
        self.tot_prot_sec_lab.setSizePolicy(sizePolicy)
        self.tot_prot_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.tot_prot_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tot_prot_sec_lab.setObjectName(_fromUtf8("tot_prot_sec_lab"))
        self.horizontalLayout_9.addWidget(self.tot_prot_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_9, 10, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.tot_lip_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_lip_lab.sizePolicy().hasHeightForWidth())
        self.tot_lip_lab.setSizePolicy(sizePolicy)
        self.tot_lip_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.tot_lip_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.tot_lip_lab.setObjectName(_fromUtf8("tot_lip_lab"))
        self.horizontalLayout_10.addWidget(self.tot_lip_lab)
        self.tot_lip_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_lip_sec_lab.sizePolicy().hasHeightForWidth())
        self.tot_lip_sec_lab.setSizePolicy(sizePolicy)
        self.tot_lip_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.tot_lip_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tot_lip_sec_lab.setObjectName(_fromUtf8("tot_lip_sec_lab"))
        self.horizontalLayout_10.addWidget(self.tot_lip_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_10, 11, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.tot_carb_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_carb_lab.sizePolicy().hasHeightForWidth())
        self.tot_carb_lab.setSizePolicy(sizePolicy)
        self.tot_carb_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.tot_carb_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.tot_carb_lab.setObjectName(_fromUtf8("tot_carb_lab"))
        self.horizontalLayout_11.addWidget(self.tot_carb_lab)
        self.tot_carb_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_carb_sec_lab.sizePolicy().hasHeightForWidth())
        self.tot_carb_sec_lab.setSizePolicy(sizePolicy)
        self.tot_carb_sec_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.tot_carb_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tot_carb_sec_lab.setObjectName(_fromUtf8("tot_carb_sec_lab"))
        self.horizontalLayout_11.addWidget(self.tot_carb_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_11, 12, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.tot_ccal_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_ccal_lab.sizePolicy().hasHeightForWidth())
        self.tot_ccal_lab.setSizePolicy(sizePolicy)
        self.tot_ccal_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.tot_ccal_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.tot_ccal_lab.setObjectName(_fromUtf8("tot_ccal_lab"))
        self.horizontalLayout_12.addWidget(self.tot_ccal_lab)
        self.tot_ccal_sec_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tot_ccal_sec_lab.sizePolicy().hasHeightForWidth())
        self.tot_ccal_sec_lab.setSizePolicy(sizePolicy)
        self.tot_ccal_sec_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.tot_ccal_sec_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.tot_ccal_sec_lab.setObjectName(_fromUtf8("tot_ccal_sec_lab"))
        self.horizontalLayout_12.addWidget(self.tot_ccal_sec_lab)
        self.gridLayout.addLayout(self.horizontalLayout_12, 13, 0, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.savebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savebut.sizePolicy().hasHeightForWidth())
        self.savebut.setSizePolicy(sizePolicy)
        self.savebut.setMinimumSize(QtCore.QSize(150, 25))
        self.savebut.setMaximumSize(QtCore.QSize(150, 25))
        self.savebut.setDefault(True)
        self.savebut.setObjectName(_fromUtf8("savebut"))
        self.horizontalLayout_13.addWidget(self.savebut)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.deletebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletebut.sizePolicy().hasHeightForWidth())
        self.deletebut.setSizePolicy(sizePolicy)
        self.deletebut.setMinimumSize(QtCore.QSize(100, 25))
        self.deletebut.setMaximumSize(QtCore.QSize(100, 25))
        self.deletebut.setDefault(True)
        self.deletebut.setObjectName(_fromUtf8("deletebut"))
        self.horizontalLayout_13.addWidget(self.deletebut)
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbut.sizePolicy().hasHeightForWidth())
        self.exitbut.setSizePolicy(sizePolicy)
        self.exitbut.setMinimumSize(QtCore.QSize(100, 25))
        self.exitbut.setMaximumSize(QtCore.QSize(100, 25))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.horizontalLayout_13.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout_13, 14, 0, 1, 1)
        Calc_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Calc_Window)
        QtCore.QMetaObject.connectSlotsByName(Calc_Window)

    def retranslateUi(self, Calc_Window):
        Calc_Window.setWindowTitle(_translate("Calc_Window", "Расчитать", None))
        self.search_lab.setText(_translate("Calc_Window", "Продукт", None))
        self.mass_lab.setText(_translate("Calc_Window", "Масса, г", None))
        self.substitutebut.setText(_translate("Calc_Window", "Подставить", None))
        self.searchbut.setText(_translate("Calc_Window", "Искать", None))
        self.prot_lab.setText(_translate("Calc_Window", "Белки", None))
        self.prot_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.lip_lab.setText(_translate("Calc_Window", "Жиры", None))
        self.lip_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.carb_lab.setText(_translate("Calc_Window", "Углеводы", None))
        self.carb_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.ccal_lab.setText(_translate("Calc_Window", "Калорийность, ккал", None))
        self.ccal_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.glyc_lab.setText(_translate("Calc_Window", "Гликемический индекс", None))
        self.glyc_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.searchwinbut.setText(_translate("Calc_Window", "Окно поиска", None))
        self.addbut.setText(_translate("Calc_Window", "Добавить", None))
        self.total_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"center\">Всего:</p></body></html>", None))
        self.tot_prot_lab.setText(_translate("Calc_Window", "Белки", None))
        self.tot_prot_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.tot_lip_lab.setText(_translate("Calc_Window", "Жиры", None))
        self.tot_lip_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.tot_carb_lab.setText(_translate("Calc_Window", "Углеводы", None))
        self.tot_carb_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.tot_ccal_lab.setText(_translate("Calc_Window", "Калорийность, ккал", None))
        self.tot_ccal_sec_lab.setText(_translate("Calc_Window", "<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.savebut.setText(_translate("Calc_Window", "Сохранить в файл", None))
        self.deletebut.setText(_translate("Calc_Window", "Очистить", None))
        self.exitbut.setText(_translate("Calc_Window", "Закрыть", None))


class Ui_Complete_Window(object):
    def setupUi(self, Complete_Window):
        Complete_Window.setObjectName(_fromUtf8("Complete_Window"))
        Complete_Window.resize(311, 259)
        Complete_Window.setMinimumSize(QtCore.QSize(311, 259))
        self.centralwidget = QtGui.QWidget(Complete_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(311, 259))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.list = QtGui.QListWidget(self.centralwidget)
        self.list.setMinimumSize(QtCore.QSize(291, 211))
        self.list.setObjectName(_fromUtf8("list"))
        self.gridLayout.addWidget(self.list, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbut.sizePolicy().hasHeightForWidth())
        self.exitbut.setSizePolicy(sizePolicy)
        self.exitbut.setMinimumSize(QtCore.QSize(100, 25))
        self.exitbut.setMaximumSize(QtCore.QSize(100, 25))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.horizontalLayout.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Complete_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Complete_Window)
        QtCore.QMetaObject.connectSlotsByName(Complete_Window)

    def retranslateUi(self, Complete_Window):
        Complete_Window.setWindowTitle(_translate("Complete_Window", "Подставить", None))
        self.exitbut.setText(_translate("Complete_Window", "Закрыть", None))


class Ui_db_cp_window(object):
    def setupUi(self, db_cp_window):
        db_cp_window.setObjectName(_fromUtf8("db_cp_window"))
        db_cp_window.resize(451, 101)
        db_cp_window.setMinimumSize(QtCore.QSize(451, 101))
        self.centralwidget = QtGui.QWidget(db_cp_window)
        self.centralwidget.setMinimumSize(QtCore.QSize(451, 101))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.old_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.old_lab.sizePolicy().hasHeightForWidth())
        self.old_lab.setSizePolicy(sizePolicy)
        self.old_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.old_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.old_lab.setObjectName(_fromUtf8("old_lab"))
        self.horizontalLayout.addWidget(self.old_lab)
        self.old_line = QtGui.QLineEdit(self.centralwidget)
        self.old_line.setMinimumSize(QtCore.QSize(100, 25))
        self.old_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.old_line.setObjectName(_fromUtf8("old_line"))
        self.horizontalLayout.addWidget(self.old_line)
        self.oldbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldbut.sizePolicy().hasHeightForWidth())
        self.oldbut.setSizePolicy(sizePolicy)
        self.oldbut.setMinimumSize(QtCore.QSize(100, 25))
        self.oldbut.setMaximumSize(QtCore.QSize(100, 25))
        self.oldbut.setObjectName(_fromUtf8("oldbut"))
        self.horizontalLayout.addWidget(self.oldbut)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.new_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_lab.sizePolicy().hasHeightForWidth())
        self.new_lab.setSizePolicy(sizePolicy)
        self.new_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.new_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.new_lab.setObjectName(_fromUtf8("new_lab"))
        self.horizontalLayout_2.addWidget(self.new_lab)
        self.new_line = QtGui.QLineEdit(self.centralwidget)
        self.new_line.setMinimumSize(QtCore.QSize(100, 25))
        self.new_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.new_line.setObjectName(_fromUtf8("new_line"))
        self.horizontalLayout_2.addWidget(self.new_line)
        self.newbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newbut.sizePolicy().hasHeightForWidth())
        self.newbut.setSizePolicy(sizePolicy)
        self.newbut.setMinimumSize(QtCore.QSize(100, 25))
        self.newbut.setMaximumSize(QtCore.QSize(100, 25))
        self.newbut.setObjectName(_fromUtf8("newbut"))
        self.horizontalLayout_2.addWidget(self.newbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.horizontalLayout_3.addWidget(self.okbut)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.horizontalLayout_3.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        db_cp_window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(db_cp_window)
        QtCore.QMetaObject.connectSlotsByName(db_cp_window)

    def retranslateUi(self, db_cp_window):
        db_cp_window.setWindowTitle(_translate("db_cp_window", "Скопировать базу данных", None))
        self.old_lab.setText(_translate("db_cp_window", "Старый файл", None))
        self.oldbut.setText(_translate("db_cp_window", "Обзор", None))
        self.new_lab.setText(_translate("db_cp_window", "Новый файл", None))
        self.newbut.setText(_translate("db_cp_window", "Обзор", None))
        self.okbut.setText(_translate("db_cp_window", "Ok", None))
        self.cancelbut.setText(_translate("db_cp_window", "Отмена", None))


class Ui_DB_Select(object):
    def setupUi(self, DB_Select):
        DB_Select.setObjectName(_fromUtf8("DB_Select"))
        DB_Select.resize(422, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DB_Select.sizePolicy().hasHeightForWidth())
        DB_Select.setSizePolicy(sizePolicy)
        DB_Select.setMinimumSize(QtCore.QSize(422, 70))
        self.centralwidget = QtGui.QWidget(DB_Select)
        self.centralwidget.setMinimumSize(QtCore.QSize(422, 70))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dbstring = QtGui.QLineEdit(self.centralwidget)
        self.dbstring.setMinimumSize(QtCore.QSize(100, 25))
        self.dbstring.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dbstring.setObjectName(_fromUtf8("dbstring"))
        self.horizontalLayout.addWidget(self.dbstring)
        self.dbsearch = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbsearch.sizePolicy().hasHeightForWidth())
        self.dbsearch.setSizePolicy(sizePolicy)
        self.dbsearch.setMinimumSize(QtCore.QSize(100, 25))
        self.dbsearch.setMaximumSize(QtCore.QSize(100, 25))
        self.dbsearch.setDefault(True)
        self.dbsearch.setObjectName(_fromUtf8("dbsearch"))
        self.horizontalLayout.addWidget(self.dbsearch)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.dbselect = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbselect.sizePolicy().hasHeightForWidth())
        self.dbselect.setSizePolicy(sizePolicy)
        self.dbselect.setMinimumSize(QtCore.QSize(100, 25))
        self.dbselect.setMaximumSize(QtCore.QSize(100, 25))
        self.dbselect.setDefault(True)
        self.dbselect.setObjectName(_fromUtf8("dbselect"))
        self.horizontalLayout_2.addWidget(self.dbselect)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.horizontalLayout_2.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        DB_Select.setCentralWidget(self.centralwidget)

        #self.retranslateUi(DB_Select)
        QtCore.QMetaObject.connectSlotsByName(DB_Select)

    def retranslateUi(self, DB_Select):
        DB_Select.setWindowTitle(_translate("DB_Select", "Выбор базы данных", None))
        self.dbsearch.setText(_translate("DB_Select", "Обзор", None))
        self.dbselect.setText(_translate("DB_Select", "Ok", None))
        self.cancelbut.setText(_translate("DB_Select", "Отмена", None))


class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName(_fromUtf8("Edit"))
        Edit.resize(336, 256)
        Edit.setMinimumSize(QtCore.QSize(336, 256))
        self.centralwidget = QtGui.QWidget(Edit)
        self.centralwidget.setMinimumSize(QtCore.QSize(336, 256))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.subs_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subs_lab.sizePolicy().hasHeightForWidth())
        self.subs_lab.setSizePolicy(sizePolicy)
        self.subs_lab.setMinimumSize(QtCore.QSize(100, 25))
        self.subs_lab.setMaximumSize(QtCore.QSize(100, 25))
        self.subs_lab.setObjectName(_fromUtf8("subs_lab"))
        self.horizontalLayout.addWidget(self.subs_lab)
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setMinimumSize(QtCore.QSize(100, 25))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.horizontalLayout.addWidget(self.search_line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbut.sizePolicy().hasHeightForWidth())
        self.searchbut.setSizePolicy(sizePolicy)
        self.searchbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        self.horizontalLayout_2.addWidget(self.searchbut)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.substitutebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substitutebut.sizePolicy().hasHeightForWidth())
        self.substitutebut.setSizePolicy(sizePolicy)
        self.substitutebut.setMinimumSize(QtCore.QSize(100, 25))
        self.substitutebut.setMaximumSize(QtCore.QSize(100, 25))
        self.substitutebut.setDefault(True)
        self.substitutebut.setObjectName(_fromUtf8("substitutebut"))
        self.horizontalLayout_2.addWidget(self.substitutebut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.prot_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prot_lab.sizePolicy().hasHeightForWidth())
        self.prot_lab.setSizePolicy(sizePolicy)
        self.prot_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.prot_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.prot_lab.setObjectName(_fromUtf8("prot_lab"))
        self.horizontalLayout_3.addWidget(self.prot_lab)
        self.prot_line = QtGui.QLineEdit(self.centralwidget)
        self.prot_line.setMinimumSize(QtCore.QSize(100, 25))
        self.prot_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.prot_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prot_line.setObjectName(_fromUtf8("prot_line"))
        self.horizontalLayout_3.addWidget(self.prot_line)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lip_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lip_lab.sizePolicy().hasHeightForWidth())
        self.lip_lab.setSizePolicy(sizePolicy)
        self.lip_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.lip_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.lip_lab.setObjectName(_fromUtf8("lip_lab"))
        self.horizontalLayout_4.addWidget(self.lip_lab)
        self.lip_line = QtGui.QLineEdit(self.centralwidget)
        self.lip_line.setMinimumSize(QtCore.QSize(100, 25))
        self.lip_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lip_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lip_line.setObjectName(_fromUtf8("lip_line"))
        self.horizontalLayout_4.addWidget(self.lip_line)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.carb_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carb_lab.sizePolicy().hasHeightForWidth())
        self.carb_lab.setSizePolicy(sizePolicy)
        self.carb_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.carb_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.carb_lab.setObjectName(_fromUtf8("carb_lab"))
        self.horizontalLayout_5.addWidget(self.carb_lab)
        self.carb_line = QtGui.QLineEdit(self.centralwidget)
        self.carb_line.setMinimumSize(QtCore.QSize(100, 25))
        self.carb_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carb_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carb_line.setObjectName(_fromUtf8("carb_line"))
        self.horizontalLayout_5.addWidget(self.carb_line)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ccal_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ccal_lab.sizePolicy().hasHeightForWidth())
        self.ccal_lab.setSizePolicy(sizePolicy)
        self.ccal_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setMaximumSize(QtCore.QSize(150, 25))
        self.ccal_lab.setObjectName(_fromUtf8("ccal_lab"))
        self.horizontalLayout_6.addWidget(self.ccal_lab)
        self.ccal_line = QtGui.QLineEdit(self.centralwidget)
        self.ccal_line.setMinimumSize(QtCore.QSize(100, 25))
        self.ccal_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ccal_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ccal_line.setObjectName(_fromUtf8("ccal_line"))
        self.horizontalLayout_6.addWidget(self.ccal_line)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.glyc_lab = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glyc_lab.sizePolicy().hasHeightForWidth())
        self.glyc_lab.setSizePolicy(sizePolicy)
        self.glyc_lab.setMinimumSize(QtCore.QSize(150, 25))
        self.glyc_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.glyc_lab.setObjectName(_fromUtf8("glyc_lab"))
        self.horizontalLayout_7.addWidget(self.glyc_lab)
        self.glyc_line = QtGui.QLineEdit(self.centralwidget)
        self.glyc_line.setMinimumSize(QtCore.QSize(100, 25))
        self.glyc_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.glyc_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.glyc_line.setObjectName(_fromUtf8("glyc_line"))
        self.horizontalLayout_7.addWidget(self.glyc_line)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.deletebut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletebut.sizePolicy().hasHeightForWidth())
        self.deletebut.setSizePolicy(sizePolicy)
        self.deletebut.setMinimumSize(QtCore.QSize(100, 25))
        self.deletebut.setMaximumSize(QtCore.QSize(100, 25))
        self.deletebut.setDefault(True)
        self.deletebut.setObjectName(_fromUtf8("deletebut"))
        self.horizontalLayout_8.addWidget(self.deletebut)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.horizontalLayout_8.addWidget(self.okbut)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.horizontalLayout_8.addWidget(self.cancelbut)
        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        Edit.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(_translate("Edit", "Редактировать", None))
        self.subs_lab.setText(_translate("Edit", "Продукт", None))
        self.searchbut.setText(_translate("Edit", "Окно поиска", None))
        self.substitutebut.setText(_translate("Edit", "Подставить", None))
        self.prot_lab.setText(_translate("Edit", "Белки", None))
        self.lip_lab.setText(_translate("Edit", "Жиры", None))
        self.carb_lab.setText(_translate("Edit", "Углеводы", None))
        self.ccal_lab.setText(_translate("Edit", "Калорийность, ккал", None))
        self.glyc_lab.setText(_translate("Edit", "Гликемический индекс", None))
        self.deletebut.setText(_translate("Edit", "Удалить", None))
        self.okbut.setText(_translate("Edit", "Ok", None))
        self.cancelbut.setText(_translate("Edit", "Отмена", None))


class Ui_Help_Window(object):
    def setupUi(self, Help_Window):
        Help_Window.setObjectName(_fromUtf8("Help_Window"))
        Help_Window.resize(583, 431)
        Help_Window.setMinimumSize(QtCore.QSize(583, 431))
        self.centralwidget = QtGui.QWidget(Help_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(583, 431))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.text = QtGui.QTextBrowser(self.centralwidget)
        self.text.setObjectName(_fromUtf8("text"))
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbut.sizePolicy().hasHeightForWidth())
        self.exitbut.setSizePolicy(sizePolicy)
        self.exitbut.setMinimumSize(QtCore.QSize(100, 25))
        self.exitbut.setMaximumSize(QtCore.QSize(100, 25))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.horizontalLayout.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        Help_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Help_Window)
        QtCore.QMetaObject.connectSlotsByName(Help_Window)

    def retranslateUi(self, Help_Window):
        Help_Window.setWindowTitle(_translate("Help_Window", "Помощь", None))
        self.text.setHtml(_translate("Help_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О проекте</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Простая программа сделанная &quot;Just-for-fun&quot;. Может оказаться полезной, например, спортсменам, худеющим или просто следящим за своим здоровьем. Не троян и не патч Бармина. При попытке пользователя выстрелить себе в ногу, будет отчаянно сопротивляться.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Что она делает?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Первоначально она задумывалась, как довольно простая программа (такой она и осталась), в процессе реализации она обросла различными функциями. Таким образом, помимо быстрой оценки &quot;Сколько я получу калорий, если съем %food&quot;, она может считать более сложные составы, составлять меню. А также работа с базой данных и небольшие удобства для пользователя.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Об использовании</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Основное окно:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Вводим название продукта, массу в граммах и жмем &quot;Посчитать&quot;. &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+S - Открыть окно поиска</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+N - Добавить запись в базу данных</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+W - Редактировать запись в базе данных</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+M - Открыть окно с продвинутым калькулятором. Возможность сохранения в файл</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+Q - Выход</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    F1     - Эта справка</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Окно поиска:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Вводим что-нибудь. Что-нибудь получим в ответ.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - аналогично нажатию на кнопку &quot;Искать&quot;</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Добавление записи в базу данных:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Запись в базу данных. Оставлять числовые поля пустыми не возбраняется.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Редактирование записи в базе данных:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Редактирование базы данных. Имя изменить нельзя. Оставлять числовые поля пустыми не возбраняется. &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска, &quot;Удалить&quot; - удалить запись из базы данных.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Создать меню:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Можно посчитать несколько продуктов. И сохранить их в файл (&quot;Сохранить в файл&quot;). &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска, &quot;Искать&quot; ищет искомое в базе данных и обновляет числа, &quot;Добавить&quot; - добавляет  продукт и его массу в общий список.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Выбрать базу данных:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Выбирает базу данных и пишет в файл настроек.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Г<span style=\" font-style:italic;\">орячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Скопировать базу данных:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Копирует текущую базу данных.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Выбрать язык:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Выбор языка.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Помощь:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Эта справка.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">О программе:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Небольшое окно &quot;About&quot;.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Окно подстановки:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Подставляет выбранную позицию в строку поиска. Навигация как мышкой, так и стрелочками.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    DoubleClick, Enter - выбор позиции</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Ошибка:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Мифическое окно. У хороших пользователей его не бывает.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О базе данных</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Существует две базы данных, сделанных в полуавтоматическом режиме - одна на английском, другая на русском. Остальное сами. Я бы не советовал вписывать ручками - лучше пользоваться интерфейсом программы. Однако, на всякий случай замечу, что в базе данных строки содержатся в следующем виде:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  наименование_продукта;;белки;;жиры;;углеводы;;калорийность;;гликемический_индекс</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Все числа хранятся в формате float (то есть что-то вроде 1.23 или 0.0). Названия лучше вводить нижним регистром, пробелы допускаются.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О локализациях</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Собственно, тут мне сказать нечего. Существует русский язык и английский. Сильно сомневаюсь, что будет добавлено что-то еще.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Технические характеристики</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Зависимости:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Python2.7</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  PyQt4</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Qt4</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Файл настроек (food_gui.ini):</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Windows</span> - рабочая директория</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux</span>   - ~/.config/food_gui/</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">База данных:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Лучше скопировать ее в рабочую директорию (Windows) или в директорию ~/.config/food_gui/ (Linux). Но, в принципе, она может быть где угодно.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Установка:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Убедиться, что все на месте (зависимости, наличие /usr/bin/python2.7).</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Запустить скрипт.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) Можно скопировать куда-нибудь.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Windows:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Установить все зависимости.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2a) Запустить скрипт</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    или</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2b) Установить pyinstaller.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3b) Запустить скрипт pyinstaller.bat.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4b) Запустить полученный *.exe файл (где-то .\\food_gui\\dist\\).</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    или</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1с) Взять уже готовый *.exe файл. Однако, его работа под всеми системами не гарантируется (скомпилен под Windows7-x64).</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">MacOS:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Удалить MacOS.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Поставить Linux.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) См. установку для Linux.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    P.S.: или подработать скрипт самостоятельно.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Об ошибках, предложениях</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ошибки буду фиксить по мере возможности. Насчет предложений ничего не обещаю. По всем вопросам стучитесь:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">e-mail: esalexeev@gmail.com</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Jabber: arcanis@jabber.ru</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  ICQ: 407-398-235</span></p></body></html>", None))
        self.exitbut.setText(_translate("Help_Window", "Закрыть", None))


class Ui_Language(object):
    def setupUi(self, Language):
        Language.setObjectName(_fromUtf8("Language"))
        Language.resize(232, 66)
        Language.setMinimumSize(QtCore.QSize(232, 66))
        self.centralwidget = QtGui.QWidget(Language)
        self.centralwidget.setMinimumSize(QtCore.QSize(232, 66))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rus_radio = QtGui.QRadioButton(self.centralwidget)
        self.rus_radio.setMinimumSize(QtCore.QSize(100, 25))
        self.rus_radio.setMaximumSize(QtCore.QSize(16777215, 25))
        self.rus_radio.setObjectName(_fromUtf8("rus_radio"))
        self.gridLayout.addWidget(self.rus_radio, 1, 0, 1, 1)
        self.cancelbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelbut.sizePolicy().hasHeightForWidth())
        self.cancelbut.setSizePolicy(sizePolicy)
        self.cancelbut.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelbut.setMaximumSize(QtCore.QSize(100, 25))
        self.cancelbut.setDefault(True)
        self.cancelbut.setObjectName(_fromUtf8("cancelbut"))
        self.gridLayout.addWidget(self.cancelbut, 1, 1, 1, 1)
        self.eng_radio = QtGui.QRadioButton(self.centralwidget)
        self.eng_radio.setMinimumSize(QtCore.QSize(100, 25))
        self.eng_radio.setMaximumSize(QtCore.QSize(16777215, 25))
        self.eng_radio.setObjectName(_fromUtf8("eng_radio"))
        self.gridLayout.addWidget(self.eng_radio, 0, 0, 1, 1)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.gridLayout.addWidget(self.okbut, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        Language.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Language)
        QtCore.QMetaObject.connectSlotsByName(Language)
        Language.setTabOrder(self.eng_radio, self.rus_radio)
        Language.setTabOrder(self.rus_radio, self.okbut)
        Language.setTabOrder(self.okbut, self.cancelbut)

    def retranslateUi(self, Language):
        Language.setWindowTitle(_translate("Language", "Change language", None))
        self.rus_radio.setText(_translate("Language", "Русский", None))
        self.cancelbut.setText(_translate("Language", "Отмена", None))
        self.eng_radio.setText(_translate("Language", "English", None))
        self.okbut.setText(_translate("Language", "Ok", None))


class Ui_NotFound(object):
    def setupUi(self, NotFound):
        NotFound.setObjectName(_fromUtf8("NotFound"))
        NotFound.resize(320, 89)
        NotFound.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget = QtGui.QWidget(NotFound)
        self.centralwidget.setMinimumSize(QtCore.QSize(320, 89))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okbut.sizePolicy().hasHeightForWidth())
        self.okbut.setSizePolicy(sizePolicy)
        self.okbut.setMinimumSize(QtCore.QSize(100, 25))
        self.okbut.setMaximumSize(QtCore.QSize(100, 25))
        self.okbut.setDefault(True)
        self.okbut.setObjectName(_fromUtf8("okbut"))
        self.horizontalLayout.addWidget(self.okbut)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        NotFound.setCentralWidget(self.centralwidget)

        #self.retranslateUi(NotFound)
        QtCore.QMetaObject.connectSlotsByName(NotFound)

    def retranslateUi(self, NotFound):
        NotFound.setWindowTitle(_translate("NotFound", "Ошибка!", None))
        self.label.setText(_translate("NotFound", "<html><head/><body><p align=\"justify\">Продукт %s не найден в базе данных</p></body></html>", None))
        self.okbut.setText(_translate("NotFound", "Ok", None))


class Ui_Search_Window(object):
    def setupUi(self, Search_Window):
        Search_Window.setObjectName(_fromUtf8("Search_Window"))
        Search_Window.resize(322, 330)
        Search_Window.setMinimumSize(QtCore.QSize(322, 330))
        self.centralwidget = QtGui.QWidget(Search_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(322, 330))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.search_line = QtGui.QLineEdit(self.centralwidget)
        self.search_line.setMinimumSize(QtCore.QSize(100, 25))
        self.search_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_line.setText(_fromUtf8(""))
        self.search_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.gridLayout.addWidget(self.search_line, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchbut.sizePolicy().hasHeightForWidth())
        self.searchbut.setSizePolicy(sizePolicy)
        self.searchbut.setMinimumSize(QtCore.QSize(100, 25))
        self.searchbut.setMaximumSize(QtCore.QSize(100, 25))
        self.searchbut.setDefault(True)
        self.searchbut.setObjectName(_fromUtf8("searchbut"))
        self.horizontalLayout.addWidget(self.searchbut)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.search_box = QtGui.QTextBrowser(self.centralwidget)
        self.search_box.setMinimumSize(QtCore.QSize(301, 231))
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.gridLayout.addWidget(self.search_box, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.exitbut = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbut.sizePolicy().hasHeightForWidth())
        self.exitbut.setSizePolicy(sizePolicy)
        self.exitbut.setMinimumSize(QtCore.QSize(100, 25))
        self.exitbut.setMaximumSize(QtCore.QSize(100, 25))
        self.exitbut.setDefault(True)
        self.exitbut.setObjectName(_fromUtf8("exitbut"))
        self.horizontalLayout_2.addWidget(self.exitbut)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        Search_Window.setCentralWidget(self.centralwidget)

        #self.retranslateUi(Search_Window)
        QtCore.QMetaObject.connectSlotsByName(Search_Window)
        Search_Window.setTabOrder(self.search_line, self.search_box)

    def retranslateUi(self, Search_Window):
        Search_Window.setWindowTitle(_translate("Search_Window", "Поиск", None))
        self.searchbut.setText(_translate("Search_Window", "Искать", None))
        self.exitbut.setText(_translate("Search_Window", "Закрыть", None))



# Main block

class AboutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_About_Window()
        self.ui.setupUi(self)
        
        self.load_text()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"О программе")
            self.ui.about.setHtml(u"""<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">food_gui 1.2.0</p>
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Лицензия: GPL</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Простенькая программа-калькулятор на питоне, подсчитывающая БЖУ, калорийность и гликемический индекс употребляемых продуктов на основании базы данных.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Автор: Евгений Алексеев aka arcanis</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>""")
            self.ui.exit.setText("Закрыть")
        else:
            self.setWindowTitle(u"About")
            self.ui.about.setHtml(u"""<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">food_gui 1.2.0</p>
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License: GPL</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simple program-calculator used self database and written on Python, that calculates proteins, fats, carbohydrates, food energy and glycemic index eaten food.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author: Evgeniy Alexeev aka arcanis</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e-mail: esalexeev@gmail.com</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jabber: arcanis@jabber.ru</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ICQ: 407-398-235</p></body></html>""")
            self.ui.exit.setText("Close")

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class AddWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Add()
        self.ui.setupUi(self)
        
        self.load_text()
        
        self.ui.subs_line.setText("")
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.add)
        QtCore.QObject.connect(self.ui.cancelbut,  QtCore.SIGNAL("clicked()"),  self.close_win)
    
    def add(self):
        global db
        global lang
        
        if (len(self.ui.subs_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.subs_line.text().toLower()
        
        if (len(self.ui.prot_line.text()) == 0):
            prot = 0.0
        else:
            if (self.ui.prot_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.prot_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    prot = self.ui.prot_line.text().toFloat()[0]
        
        if (len(self.ui.lip_line.text()) == 0):
            lip = 0.0
        else:
            if (self.ui.lip_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.lip_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    lip = self.ui.lip_line.text().toFloat()[0]
        
        if (len(self.ui.carb_line.text()) == 0):
            carb = 0.0
        else:
            if (self.ui.carb_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.carb_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    carb = self.ui.carb_line.text().toFloat()[0]
        
        if (len(self.ui.ccal_line.text()) == 0):
            ccal = 0.0
        else:
            if (self.ui.ccal_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.ccal_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    ccal = self.ui.ccal_line.text().toFloat()[0]
        
        if (len(self.ui.glyc_line.text()) == 0):
            glyc = 0.0
        else:
            if (self.ui.glyc_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.glyc_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    glyc = self.ui.glyc_line.text().toFloat()[0]
        
        dbold = db+".bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    dbfile.write (line)
                    if (subs == line.split(';;')[0]):
                        i = 1
                        if (lang == 'RUS'):
                            inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+subs+u"\"<br>уже существует в базе данных</p></body></html>"
                        else:
                            inv_subs = u"<html><head/><body><p align=\"center\">Food \""+subs+u"\"<br>already exists in the database</p></body></html>"
                        not_found = NotFound(parent=self, text=inv_subs)
                        not_found.show()
        
        os.remove (dbold)
    
        if (i == 0):
            dbfile = open (db,  'a')
            dbfile.write (subs+";;"+str(round(prot, 3))+";;"+str(round(lip, 3))+";;"+str(round(carb, 3))+";;"+str(round(ccal, 3))+";;"+str(round(glyc, 3))+"\n")
            dbfile.close()
            
            self.ui.subs_line.clear()
            self.ui.prot_line.setText("0.0")
            self.ui.lip_line.setText("0.0")
            self.ui.carb_line.setText("0.0")
            self.ui.ccal_line.setText("0.0")
            self.ui.glyc_line.setText("0.0")
    
    def close_win(self):
        self.ui.subs_line.clear()
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        self.close()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Добавить")
            self.ui.cancelbut.setText(u"Отмена")
            self.ui.okbut.setText(u"Ok")
            self.ui.subs_lab.setText(u"Продукт")
            self.ui.prot_lab.setText(u"Белки")
            self.ui.lip_lab.setText(u"Жиры")
            self.ui.carb_lab.setText(u"Углеводы")
            self.ui.ccal_lab.setText(u"Калорийность, ккал")
            self.ui.glyc_lab.setText(u"Гликемический индекс")
        else:
            self.setWindowTitle(u"Add")
            self.ui.cancelbut.setText(u"Cancel")
            self.ui.okbut.setText(u"Ok")
            self.ui.subs_lab.setText(u"Food")
            self.ui.prot_lab.setText(u"Proteins")
            self.ui.lip_lab.setText(u"Fats")
            self.ui.carb_lab.setText(u"Carbohydrates")
            self.ui.ccal_lab.setText(u"Food energy, kcal")
            self.ui.glyc_lab.setText(u"Glycemic index")

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class CalcWindow(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_Calc_Window()
        self.ui.setupUi(self)
        
        self.load_text()
        
        self.ui.mass_line.setText("100")
        self.ui.tot_prot_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_lip_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_ccal_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_carb_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        
        search_window = SearchWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), self.search)
        QtCore.QObject.connect(self.ui.addbut,  QtCore.SIGNAL("clicked()"),  self.add)
        QtCore.QObject.connect(self.ui.savebut,  QtCore.SIGNAL("clicked()"),  self.save)
        QtCore.QObject.connect(self.ui.deletebut,  QtCore.SIGNAL("clicked()"),  self.clear)
        QtCore.QObject.connect(self.ui.searchwinbut, QtCore.SIGNAL("clicked()"), search_window.show)
        QtCore.QObject.connect(self.ui.exitbut, QtCore.SIGNAL("clicked()"), self.close_win)
        QtCore.QObject.connect(self.ui.substitutebut, QtCore.SIGNAL("clicked()"), self.complete)
        QtCore.QObject.connect(self.ui.search_line, QtCore.SIGNAL("returnPressed()"), self.complete)
    
    def add(self):
        global db
        global lang
        
        if (self.ui.search_line.text() != ""):
            search = self.ui.search_line.text().toLower()
        else:
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        if (self.ui.mass_line.text() != ""):
            mass = float(self.ui.mass_line.text())
        else:
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Weight isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = [mass/100*float(num) for num in line.split(';;')[1:5]]
                    i = 1
                    break
        
            if (i == 0):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">Food \""+search+u"\"<br>isn't found in database</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
        
        prot_fl = float(self.ui.tot_prot_sec_lab.text()[36:-18]) + round(prop[0], 3)
        lip_fl = float(self.ui.tot_lip_sec_lab.text()[36:-18]) + round(prop[1], 3)
        carb_fl = float(self.ui.tot_carb_sec_lab.text()[36:-18]) + round(prop[2], 3)
        ccal_fl = float(self.ui.tot_ccal_sec_lab.text()[36:-18]) + round(prop[3], 3)
        
        prot = "<html><head/><body><p align=\"right\">"+str(prot_fl)+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(lip_fl)+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(carb_fl)+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(ccal_fl)+"</p></body></html>"
        
        self.ui.tot_prot_sec_lab.setText(prot)
        self.ui.tot_lip_sec_lab.setText(lip)
        self.ui.tot_carb_sec_lab.setText(carb)
        self.ui.tot_ccal_sec_lab.setText(ccal)
        
        self.ui.text_selected.append(search+u", "+str(round(mass,  3))+u" г")
        
        self.ui.mass_line.setText("100")
        self.ui.search_line.clear()

    def clear(self):
        self.ui.search_line.clear()
        self.ui.mass_line.setText("100")
        
        self.ui.prot_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.lip_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.ccal_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.carb_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        self.ui.glyc_sec_lab.setText("<html><head/><body><p align=\"right\"></br></p></body></html>")
        
        self.ui.text_selected.clear()
        
        self.ui.tot_prot_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_lip_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_ccal_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
        self.ui.tot_carb_sec_lab.setText("<html><head/><body><p align=\"right\">0.0</p></body></html>")
    
    def close_win(self):
        self.clear()
        self.close()
    
    def complete(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
    
        if (len(search) < 3):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Задано короткое имя</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Set too short food name</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (line.split(';;')[0].find(search) > -1):
                    output = line.split(';;')[0]
                    i = i + 1
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт, содержащий \""+search+u"\",<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food name with \""+search+u"\",<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        elif (i == 1):
            self.ui.search_line.setText(output)
        elif (i > 1):
            complete_window = CompleteWindow (parent=self,  search=search,  put_search_line=self.ui.search_line)
            complete_window.show()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Расcчитать")
            self.ui.search_lab.setText(u"Продукт")
            self.ui.searchbut.setText(u"Искать")
            self.ui.prot_lab.setText(u"Белки")
            self.ui.lip_lab.setText(u"Жиры")
            self.ui.prot_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.lip_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_lab.setText(u"Углеводы")
            self.ui.ccal_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.ccal_lab.setText(u"Калорийность, ккал")
            self.ui.glyc_lab.setText(u"Гликемический индекс")
            self.ui.glyc_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.addbut.setText(u"Добавить")
            self.ui.mass_lab.setText(u"Масса, г")
            self.ui.tot_ccal_lab.setText(u"Калорийность, ккал")
            self.ui.tot_lip_lab.setText(u"Жиры")
            self.ui.tot_prot_lab.setText(u"Белки")
            self.ui.tot_carb_lab.setText(u"Углеводы")
            self.ui.total_lab.setText(u"<html><head/><body><p align=\"center\">Всего:</p></body></html>")
            self.ui.savebut.setText(u"Сохранить в файл")
            self.ui.exitbut.setText(u"Закрыть")
            self.ui.deletebut.setText(u"Очистить")
            self.ui.searchwinbut.setText(u"Окно поиска")
            self.ui.substitutebut.setText(u"Подставить")
        else:
            self.setWindowTitle(u"Calculate")
            self.ui.search_lab.setText(u"Food")
            self.ui.searchbut.setText(u"Search")
            self.ui.prot_lab.setText(u"Proteins")
            self.ui.lip_lab.setText(u"Fats")
            self.ui.prot_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.lip_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_lab.setText(u"Carbohydrates")
            self.ui.ccal_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.ccal_lab.setText(u"Food energy, kcal")
            self.ui.glyc_lab.setText(u"Glycemic index")
            self.ui.glyc_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.addbut.setText(u"Add")
            self.ui.mass_lab.setText(u"Weight, g")
            self.ui.tot_ccal_lab.setText(u"Food energy, kcal")
            self.ui.tot_lip_lab.setText(u"Fats")
            self.ui.tot_prot_lab.setText(u"Proteins")
            self.ui.tot_carb_lab.setText(u"Carbohydrates")
            self.ui.total_lab.setText(u"<html><head/><body><p align=\"center\">Total:</p></body></html>")
            self.ui.savebut.setText(u"Save as ...")
            self.ui.exitbut.setText(u"Close")
            self.ui.deletebut.setText(u"Clear")
            self.ui.searchwinbut.setText(u"Search window")
            self.ui.substitutebut.setText(u"Autocomplete")
    
    def save(self):
        global lang
        
        if (lang == 'RUS'):
            menu_name = QtGui.QFileDialog.getSaveFileName(self, u'Выбор файла меню','','Текст, *.txt (*.txt);;Все файлы (*)')
        else:
            menu_name = QtGui.QFileDialog.getSaveFileName(self, u'Save as ...','','Text, *.txt (*.txt);;All files (*)')
        if (len(menu_name) > 0):
            with open(menu_name,'w') as menu_file:
                prot = self.ui.tot_prot_sec_lab.text()[36:-18]
                lip = self.ui.tot_lip_sec_lab.text()[36:-18]
                carb = self.ui.tot_carb_sec_lab.text()[36:-18]
                ccal = self.ui.tot_ccal_sec_lab.text()[36:-18]
                if (lang == 'RUS'):
                    menu_file.write (u"Белки: "+prot+u"\nЖиры: "+lip+u"\nУглеводы: "+carb+u"\nКалорийность, ккал: "+ccal+u"\n\n")
                else:
                    menu_file.write (u"Proteins: "+prot+u"\nFats: "+lip+u"\nCarbohydrates: "+carb+u"\nFood energy, kcal: "+ccal+u"\n\n")
                
                for line in self.ui.text_selected.toPlainText():
                    menu_file.write(line)
    
    def search(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
    
        if (len(search) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        if (len(self.ui.mass_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Weight isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            mass = float(self.ui.mass_line.text())
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = [mass/100*float(num) for num in line.split(';;')[1:5]]
                    glyc_fl = float(line.split(';;')[5])
                    i = 1
                    break
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food \""+search+u"\"<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
    
        prot = "<html><head/><body><p align=\"right\">"+str(round(prop[0], 3))+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(round(prop[1], 3))+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(round(prop[2], 3))+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(round(prop[3], 3))+"</p></body></html>"
        glyc = "<html><head/><body><p align=\"right\">"+str(round(glyc_fl, 3))+"</p></body></html>"
    
        self.ui.prot_sec_lab.setText(prot)
        self.ui.lip_sec_lab.setText(lip)
        self.ui.carb_sec_lab.setText(carb)
        self.ui.ccal_sec_lab.setText(ccal)
        self.ui.glyc_sec_lab.setText(glyc)

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()
    
    
class CompleteWindow(QtGui.QMainWindow):
    def __init__(self, parent=None,  search=None,  put_search_line=None, put_prot_line=None, put_lip_line=None, put_carb_line=None, put_ccal_line=None, put_glyc_line=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Complete_Window()
        self.ui.setupUi(self)
        
        global db
        global lang
        
        self.load_text()
        
        self._put_search_line = put_search_line
        self._put_prot_line = put_prot_line
        self._put_lip_line = put_lip_line
        self._put_carb_line = put_carb_line
        self._put_ccal_line = put_ccal_line
        self._put_glyc_line = put_glyc_line
    
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (line.split(';;')[0].find(search) > -1):
                    if (i == 0):
                        text = line.split(';;')[0]
                    else:
                        text = text+';;'+line.split(';;')[0]
                    i = i + 1

        for string in text.split(';;'):
            self.ui.list.addItem(string)
        
        QtCore.QObject.connect(self.ui.list, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.putitem)
        QtCore.QObject.connect(self.ui.list, QtCore.SIGNAL("itemActivated(QListWidgetItem*)"), self.putitem)
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Подставить")
            self.ui.exitbut.setText(u"Закрыть")
        else:
            self.setWindowTitle(u"Autocomplete")
            self.ui.exitbut.setText(u"Close")
    
    def putitem(self):        
        string = str(QtCore.QString.toUtf8(self.ui.list.currentItem().text()))
        self._put_search_line.setText(string)
        
        if (self._put_prot_line != None):
            with open(db,'r') as dbfile:
                for line in dbfile:
                    if (string == line.split(';;')[0]):
                        prot = str(round(float(line.split(';;')[1]),  3))
                        lip = str(round(float(line.split(';;')[2]),  3))
                        carb = str(round(float(line.split(';;')[3]),  3))
                        ccal = str(round(float(line.split(';;')[4]),  3))
                        glyc = str(round(float(line.split(';;')[5]),  3))
                        break
        
            self._put_prot_line.setText(prot)
            self._put_lip_line.setText(lip)
            self._put_carb_line.setText(carb)
            self._put_ccal_line.setText(ccal)
            self._put_glyc_line.setText(glyc)
    
        self.close()
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class DBcpWindow(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_db_cp_window()
        self.ui.setupUi(self)
        
        self.load_text()
        
        if (sys.platform[0:3] == 'win'):
            db_new = os.getcwd()+"\\db_new.dat"
        else:
            db_new = os.path.abspath(os.path.expanduser('~/db_new.dat'))
        db_old = db
        self.ui.new_line.setText(db_new)
        self.ui.old_line.setText(db_old)
        
        QtCore.QObject.connect(self.ui.oldbut, QtCore.SIGNAL("clicked()"), self.old_select)
        QtCore.QObject.connect(self.ui.newbut, QtCore.SIGNAL("clicked()"), self.new_select)
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.dbcp)
    
    def dbcp(self):
        global lang
        
        if (len(self.ui.new_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Имя новой базы данных не задано</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">New database name isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            db_new = self.ui.new_line.text()
        
        if (len(self.ui.old_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Имя старой базы данных не задано</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Old database name isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            db_old = self.ui.old_line.text()
        
        shutil.copy(db_old,  db_new)
        self.close()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Скопировать базу данных")
            self.ui.oldbut.setText(u"Обзор")
            self.ui.newbut.setText(u"Обзор")
            self.ui.cancelbut.setText(u"Отмена")
            self.ui.okbut.setText(u"Ok")
            self.ui.old_lab.setText(u"Старый файл")
            self.ui.new_lab.setText(u"Новый файл")
        else:
            self.setWindowTitle(u"Copy database")
            self.ui.oldbut.setText(u"Browse")
            self.ui.newbut.setText(u"Browse")
            self.ui.cancelbut.setText(u"Cancel")
            self.ui.okbut.setText(u"Ok")
            self.ui.old_lab.setText(u"Old file")
            self.ui.new_lab.setText(u"New file")

    def new_select(self):
        global lang
        
        if (lang == 'RUS'):
            db_new = QtGui.QFileDialog.getSaveFileName(self, u'Выбор новой базы данных','','Файл базы данных, *.dat (*.dat);;Все файлы (*)')
        else:
            db_new = QtGui.QFileDialog.getSaveFileName(self, u'New database','','Database, *.dat (*.dat);;All files (*)')
        if (len(db_new) > 0):
            self.ui.new_line.setText(db_new)
    
    def old_select(self):
        if (lang == 'RUS'):
            db_old = QtGui.QFileDialog.getOpenFileNames(self, u'Выбор старой базы данных','','Файл базы данных, *.dat (*.dat);;Все файлы (*)')
        else:
            db_old = QtGui.QFileDialog.getOpenFileNames(self, u'Old database','','Database, *.dat (*.dat);;All files (*)')
        if (len(db_old) > 0):
            db_old_string = QtCore.QString(u'')
            for liter in db_old:
                db_old_string.append(liter)
            self.ui.old_line.setText(db_old_string)
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()
    
    
class DBselWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_DB_Select()
        self.ui.setupUi(self)
        
        self.load_text()
        
        self.ui.dbstring.setText(db)
        
        QtCore.QObject.connect(self.ui.dbsearch, QtCore.SIGNAL("clicked()"), self.db_select)
        QtCore.QObject.connect(self.ui.dbselect, QtCore.SIGNAL("clicked()"), self.db_set)
    
    def db_select(self):
        global db
        global lang
        
        if (lang == 'RUS'):
            db_name = QtGui.QFileDialog.getOpenFileNames(self, u'Выбор базы данных','','Файл базы данных, *.dat(*.dat);;Все файлы (*)')
        else:
            db_name = QtGui.QFileDialog.getOpenFileNames(self, u'Database','','Database, *.dat(*.dat);;All files (*)')
        if (len(db_name) > 0):
            dbfile_string = QtCore.QString(u'')
            for liter in db_name:
                dbfile_string.append(liter)
            self.ui.dbstring.setText(dbfile_string)
            db = dbfile_string

    def db_set(self):
        global db
        
        if (len(self.ui.dbstring.text()) > 0):
            dbfile_string = self.ui.dbstring.text()
            
            if (sys.platform[0:3] == 'win'):
                config_new = os.getcwd()+"\\food_gui.ini"
                config_old = os.getcwd()+"/food_gui.ini.bckp"
            else:
                config_new = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini'))
                config_old = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini.bckp'))
            os.rename(config_new,  config_old)
            
            with open(config_old,  'r') as config_old_file:
                with open(config_new,  'w') as config_new_file:
                    for line in config_old_file:
                        if (line.split('==')[0] == 'DATABASE'):
                            config_new_file.write('DATABASE=='+dbfile_string+'==\n')
                        else:
                            config_new_file.write(line)
            
            mainwin = MainWindow()
            mainwin.setup_database()
            os.remove (config_old)
            self.close()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Выбор базы данных")
            self.ui.dbselect.setText(u"Ok")
            self.ui.dbsearch.setText(u"Обзор")
            self.ui.cancelbut.setText(u"Отмена")
        else:
            self.setWindowTitle(u"Select database")
            self.ui.dbselect.setText(u"Ok")
            self.ui.dbsearch.setText(u"Browse")
            self.ui.cancelbut.setText(u"Cancel")
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()
    

class EditWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Edit()
        self.ui.setupUi(self)
        
        self.load_text()
        
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        search_window = SearchWindow(parent=self)
        
        QtCore.QObject.connect(self.ui.deletebut, QtCore.SIGNAL("clicked()"), self.delete)
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.edit)
        QtCore.QObject.connect(self.ui.cancelbut,  QtCore.SIGNAL("clicked()"),  self.close_win)
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), search_window.show)
        QtCore.QObject.connect(self.ui.substitutebut, QtCore.SIGNAL("clicked()"), self.complete)
        QtCore.QObject.connect(self.ui.search_line, QtCore.SIGNAL("returnPressed()"), self.complete)
    
    def close_win(self):
        self.ui.search_line.clear()
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
        
        self.close()
    
    def complete(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
    
        if (len(search) < 3):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Задано короткое имя</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Set too short food name</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (line.split(';;')[0].find(search) > -1):
                    output = line.split(';;')[0]
                    i = i + 1
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт, содержащий \""+search+u"\",<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food name with \""+search+u"\",<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        elif (i == 1):
            self.ui.search_line.setText(output)
            with open(db,'r') as dbfile:
                for line in dbfile:
                    if (output == line.split(';;')[0]):
                        prot = str(round(float(line.split(';;')[1]),  3))
                        lip = str(round(float(line.split(';;')[2]),  3))
                        carb = str(round(float(line.split(';;')[3]),  3))
                        ccal = str(round(float(line.split(';;')[4]),  3))
                        glyc = str(round(float(line.split(';;')[5]),  3))
                        break
        
            self.ui.prot_line.setText(prot)
            self.ui.lip_line.setText(lip)
            self.ui.carb_line.setText(carb)
            self.ui.ccal_line.setText(ccal)
            self.ui.glyc_line.setText(glyc)
        elif (i > 1):                        
            complete_window = CompleteWindow (parent=self, search=search, put_search_line=self.ui.search_line, put_prot_line=self.ui.prot_line, put_lip_line=self.ui.lip_line, put_carb_line=self.ui.carb_line, put_ccal_line=self.ui.ccal_line, put_glyc_line=self.ui.glyc_line)
            complete_window.show()
    
    def delete(self):
        global db
        global lang
        
        if (len(self.ui.search_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.search_line.text().toLower()
        
        dbold = db + ".bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    if (subs == line.split(';;')[0]):
                        i = 1
                    else:
                        dbfile.write (line)
        
        os.remove (dbold)
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food \""+search+u"\"<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
        
        self.ui.search_line.clear()
        self.ui.prot_line.setText("0.0")
        self.ui.lip_line.setText("0.0")
        self.ui.carb_line.setText("0.0")
        self.ui.ccal_line.setText("0.0")
        self.ui.glyc_line.setText("0.0")
    
    def edit(self):
        global db
        global lang
        
        if (len(self.ui.search_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            subs = self.ui.search_line.text().toLower()
        
        if (len(self.ui.prot_line.text()) == 0):
            prot = 0.0
        else:
            if (self.ui.prot_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.prot_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.prot_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    prot = self.ui.prot_line.text().toFloat()[0]
        
        if (len(self.ui.lip_line.text()) == 0):
            lip = 0.0
        else:
            if (self.ui.lip_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.lip_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.lip_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    lip = self.ui.lip_line.text().toFloat()[0]
        
        if (len(self.ui.carb_line.text()) == 0):
            carb = 0.0
        else:
            if (self.ui.carb_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.carb_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.carb_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    carb = self.ui.carb_line.text().toFloat()[0]
        
        if (len(self.ui.ccal_line.text()) == 0):
            ccal = 0.0
        else:
            if (self.ui.ccal_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.ccal_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.ccal_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    ccal = self.ui.ccal_line.text().toFloat()[0]
        
        if (len(self.ui.glyc_line.text()) == 0):
            glyc = 0.0
        else:
            if (self.ui.glyc_line.text().toFloat()[1] == False):
                if (lang == 'RUS'):
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" не число</p></body></html>"
                else:
                    inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" isn't a number</p></body></html>"
                not_found = NotFound(parent=self, text=inv_subs)
                not_found.show()
                return
            else:
                if (self.ui.glyc_line.text().toFloat()[0] < 0):
                    if (lang == 'RUS'):
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" отрицательное</p></body></html>"
                    else:
                        inv_subs = u"<html><head/><body><p align=\"center\">\""+self.ui.glyc_line.text()+"\" is negative</p></body></html>"
                    not_found = NotFound(parent=self, text=inv_subs)
                    not_found.show()
                    return
                else:
                    glyc = self.ui.glyc_line.text().toFloat()[0]
        
        dbold = db + ".bckp"
        os.rename(db,  dbold)
        i = 0
        with open (dbold,  'r') as dbfile_old:
            with open (db,  'w') as dbfile:
                for line in dbfile_old:
                    if (subs == line.split(';;')[0]):
                        i = 1
                        dbfile.write (subs+";;"+str(round(prot, 3))+";;"+str(round(lip, 3))+";;"+str(round(carb, 3))+";;"+str(round(ccal, 3))+";;"+str(round(glyc, 3))+"\n")
                    else:
                        dbfile.write (line)
        
        os.remove (dbold)
    
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food \""+search+u"\"<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
        else:
            self.ui.search_line.clear()
            self.ui.prot_line.setText("0.0")
            self.ui.lip_line.setText("0.0")
            self.ui.carb_line.setText("0.0")
            self.ui.ccal_line.setText("0.0")
            self.ui.glyc_line.setText("0.0")
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Редактировать")
            self.ui.cancelbut.setText(u"Отмена")
            self.ui.okbut.setText(u"Ok")
            self.ui.deletebut.setText(u"Удалить")
            self.ui.prot_lab.setText(u"Белки")
            self.ui.lip_lab.setText(u"Жиры")
            self.ui.carb_lab.setText(u"Углеводы")
            self.ui.ccal_lab.setText(u"Калорийность, ккал")
            self.ui.glyc_lab.setText(u"Гликемический индекс")
            self.ui.subs_lab.setText(u"Продукт")
            self.ui.searchbut.setText(u"Окно поиска")
            self.ui.substitutebut.setText(u"Подставить")
        else:
            self.setWindowTitle(u"Edit")
            self.ui.cancelbut.setText(u"Cancel")
            self.ui.okbut.setText(u"Ok")
            self.ui.deletebut.setText(u"Remove")
            self.ui.prot_lab.setText(u"Proteins")
            self.ui.lip_lab.setText(u"Fats")
            self.ui.carb_lab.setText(u"Carbohydrates")
            self.ui.ccal_lab.setText(u"Food energy, kcal")
            self.ui.glyc_lab.setText(u"Glycemic index")
            self.ui.subs_lab.setText(u"Food")
            self.ui.searchbut.setText(u"Search window")
            self.ui.substitutebut.setText(u"Autocomplete")
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class Help(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        global lang
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_Help_Window()
        self.ui.setupUi(self)
        
        self.load_text()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Помощь")
            self.ui.exitbut.setText(u"Закрыть")
            self.ui.text.setHtml(u"""<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О проекте</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Простая программа сделанная &quot;Just-for-fun&quot;. Может оказаться полезной, например, спортсменам, худеющим или просто следящим за своим здоровьем. Не троян и не патч Бармина. При попытке пользователя выстрелить себе в ногу, будет отчаянно сопротивляться.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Что она делает?</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Первоначально она задумывалась, как довольно простая программа (такой она и осталась), в процессе реализации она обросла различными функциями. Таким образом, помимо быстрой оценки &quot;Сколько я получу калорий, если съем %food&quot;, она может считать более сложные составы, составлять меню. А также работа с базой данных и небольшие удобства для пользователя.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Об использовании</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Основное окно:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Вводим название продукта, массу в граммах и жмем &quot;Посчитать&quot;. &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+S - Открыть окно поиска</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+N - Добавить запись в базу данных</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+W - Редактировать запись в базе данных</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+M - Открыть окно с продвинутым калькулятором. Возможность сохранения в файл</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+Q - Выход</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    F1     - Эта справка</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Окно поиска:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Вводим что-нибудь. Что-нибудь получим в ответ.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - аналогично нажатию на кнопку &quot;Искать&quot;</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Добавление записи в базу данных:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Запись в базу данных. Оставлять числовые поля пустыми не возбраняется.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Редактирование записи в базе данных:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Редактирование базы данных. Имя изменить нельзя. Оставлять числовые поля пустыми не возбраняется. &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска, &quot;Удалить&quot; - удалить запись из базы данных.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Создать меню:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Можно посчитать несколько продуктов. И сохранить их в файл (&quot;Сохранить в файл&quot;). &quot;Подставить&quot; откроет меню подстановки (или подставит автоматически), &quot;Окно поиска&quot; откроет окно поиска, &quot;Искать&quot; ищет искомое в базе данных и обновляет числа, &quot;Добавить&quot; - добавляет  продукт и его массу в общий список.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (в строке поиска) - откроет меню подстановки</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Выбрать базу данных:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Выбирает базу данных и пишет в файл настроек.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Г<span style=\" font-style:italic;\">орячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Скопировать базу данных:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Копирует текущую базу данных.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Выбрать язык:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Выбор языка.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Помощь:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Эта справка.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">О программе:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Небольшое окно &quot;About&quot;.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Переключение по объектам</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Окно подстановки:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Подставляет выбранную позицию в строку поиска. Навигация как мышкой, так и стрелочками.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Горячие клавиши:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    DoubleClick, Enter - выбор позиции</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - закрыть окно</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Ошибка:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Мифическое окно. У хороших пользователей его не бывает.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О базе данных</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Существует две базы данных, сделанных в полуавтоматическом режиме - одна на английском (правда, с машинным переводом), другая на русском. Остальное сами. Я бы не советовал вписывать ручками - лучше пользоваться интерфейсом программы. Однако, на всякий случай замечу, что в базе данных строки содержатся в следующем виде:</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  наименование_продукта;;белки;;жиры;;углеводы;;калорийность;;гликемический_индекс</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Все числа хранятся в формате float (то есть что-то вроде 1.23 или 0.0). Названия лучше вводить нижним регистром, пробелы допускаются. Кстати, в оригинальной базе данных отсутствуют данные по гликемическому индексу - вместо него везде 0.0. Все числовые значения заносятся из расчета на 100 весовых единиц.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">О локализациях</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Собственно, тут мне сказать нечего. Существует русский язык и английский. Сильно сомневаюсь, что будет добавлено что-то еще.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Технические характеристики</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Зависимости:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Python2.7</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  PyQt4</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Qt4</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Файл настроек (food_gui.ini):</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Windows</span> - рабочая директория</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux</span>   - ~/.config/food_gui/</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">База данных:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Лучше скопировать ее в рабочую директорию (Windows) или в директорию ~/.config/food_gui/ (Linux). Но, в принципе, она может быть где угодно.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Установка:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Убедиться, что все на месте (зависимости, наличие /usr/bin/python2.7).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Запустить скрипт.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) Можно скопировать куда-нибудь.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    или</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1b) Скачать готовый бинарный файл.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Windows:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Установить все зависимости.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2a) Запустить скрипт</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    или</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2b) Установить pyinstaller.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3b) Запустить скрипт pyinstaller.bat.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4b) Запустить полученный *.exe файл (где-то .\\food_gui\\dist\\).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    или</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1с) Взять уже готовый *.exe файл. Однако, его работа под всеми системами не гарантируется (скомпилен под Windows7-x64).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">MacOS:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Удалить MacOS.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Поставить Linux.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) См. установку для Linux.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    P.S.: или подработать скрипт самостоятельно.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Об ошибках, предложениях</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ошибки буду фиксить по мере возможности. Насчет предложений ничего не обещаю. По всем вопросам стучитесь:</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">e-mail: esalexeev@gmail.com</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Jabber: arcanis@jabber.ru</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  ICQ: 407-398-235</span></p></body></html>""")
        else:
            self.setWindowTitle(u"Help")
            self.ui.exitbut.setText(u"Close")
            self.ui.text.setHtml(u"""<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
p, li { white-space: pre-wrap; }
</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">About</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A simple program that made &quot;Just-for-fun&quot;. It may be useful, for example, athletes, losing weight, or just monitoring their health. It isn\'t Trojan or Barmin\'s patch. When a user attempts to shoot in the leg yourself , it will be resist.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">What does it do?</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">What initially began as a simple program (so it still is) it has acquired different functions. Thus, in addition to rapid evaluation &quot;How many calories do I get when I eat %food&quot;, it can do more complex calculations or create menu. As well as working with a database and a small comfort for a user.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">How to use</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Main window:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Enter name of food, weight in grams and click on &quot;Calculate&quot;. Click on &quot;Autocomlete&quot; will open autocomplete menu (or substitute automatically), click on &quot;Search window&quot; will open search window.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+S - Open search  window</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+N - Add item to the database</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+W - Edit item in the database</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ctrl+M - Open window with advanced calculator. It can save calculations to file.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    F1     - This help</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (in the search line) - Open autocomplete menu</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Search window:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Introduce something. Get something in return.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (in the search line) - Same as click on &quot;Search&quot;</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Add item to the database:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Add item to the database. You may leave numeric fields blank.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Edit item in the database:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Edit database. Name can not be changed. You may leave numeric fields blank. Click on &quot;Autocomlete&quot; will open autocomplete menu (or substitute automatically), click on &quot;Search window&quot; will open search window, click on &quot;Remove&quot; will remove item from the database.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (in the search line) - Open autocomplete menu</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Create menu:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You can do calculations with more number of items. And save it to file (&quot;Save as ...&quot;). Click on &quot;Autocomlete&quot; will open autocomplete menu (or substitute automatically), click on &quot;Search window&quot; will open search window, click on &quot;Search&quot; will search for item in the database and will update values, click on &quot;Add&quot; will add item and its weight in the list.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Enter (in the search line) - Open autocomplete menu</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Select database:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Select database and write it to configuration file.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Copy database:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Copy current database.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Change the language:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You can change the language.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Help:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  This help.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">About:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A small window &quot;About&quot;</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tab    - Switch on objects</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Autocomplete window:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Substitutes selected position to search line. Selection is made mouse or arrow keys.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Hotkeys:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    DoubleClick, Enter - Select position</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Esc    - Close</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Error:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  It is mythical window. A good user doesn\'t see it.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">About database</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There are two databases made ​​in semi-automatic mode. First in English (mechanical translation) and second in Russian. The rest do yourself. I recommend use program interface for adding item to the database. However, I note that the database contains the line as follow string:</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  item_name;;proteins;;fats;;carbohydrates;;food_energy;;glycemic_index</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All numbers are stored as float (that is something like 1.23 or 0.0). I recommend entering item name in lower case. Space are allowed. Also original database doesn't include data on glycemic index (it include 0.0 instead glycemic index). All numeric values ​​are recorded per 100 weight units.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">About localization</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Actually, I have nothing to say here. There are Russian and English. I seriously doubt that anything more will be added.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Specification</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Dependencies:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Python2.7</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  PyQt4</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Qt4</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Configuration file (food_gui.ini):</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Windows</span> - the working directory</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux</span>   - ~/.config/food_gui/</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Database:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  I recommend copy it to your working directory (Windows) or to ~/.config/food_gui/ (Linux). But it could be anywhere.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Installation:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">Linux:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Make sure that everything is in place (dependencies, /usr/bin/python2.7).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Run the script.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) You can copy the script to somewhere.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    or</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1b) Get binary file.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Windows:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Install all dependencies.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2a) Run the script.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    or</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2b) Install pyinstaller.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3b) Run the script &quot;pyinstaller.bat&quot;.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    4b) Run *.exe file (somewhere .\\food_gui\\dist\\).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    or</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1c) Get *.exe file. However its work for all systems isn\'t guatanteed (compiled under Windows7-x64).</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  MacOS:</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1) Remove MacOS.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2) Install Linux.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3) Install for Linux.</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    P.S.: You can also fixed a script yourself.</p>
<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Bugs and offers</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I will fix bugs possibly. I promise nothing about offers. For all questions:</p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  <span style=\" font-style:italic;\">e-mail: esalexeev@gmail.com</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  Jabber: arcanis@jabber.ru</span></p>
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">  ICQ: 407-398-235</span></p></body></html>""")
   
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class Language(QtGui.QMainWindow):
    def __init__(self,  parent=None, aboutwin=None, addwin=None, caclwin=None, dbcpwin=None, dbselwin=None, editwin=None, helpwin=None, notfoundwin=None, searchwin=None, mainwin=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self,  parent)
        self.ui = Ui_Language()
        self.ui.setupUi(self)
        
        self._aboutwin = aboutwin
        self._addwin = addwin
        self._caclwin = caclwin
        self._dbcpwin = dbcpwin
        self._dbselwin = dbselwin
        self._editwin = editwin
        self._helpwin = helpwin
        self._notfoundwin = notfoundwin
        self._searchwin = searchwin
        self._mainwin = mainwin
        
        self.load_text()

        if (lang == 'RUS'):
            self.ui.rus_radio.setChecked(True)
            self.ui.eng_radio.setChecked(False)
        else:
            self.ui.eng_radio.setChecked(True)
            self.ui.rus_radio.setChecked(False)
        
        QtCore.QObject.connect(self.ui.okbut, QtCore.SIGNAL("clicked()"), self.setup_language)
        QtCore.QObject.connect(self.ui.cancelbut, QtCore.SIGNAL("clicked()"), self.close_win)
    
    def close_win(self):
        global lang
        
        if (lang == 'RUS'):
            self.ui.rus_radio.setChecked(True)
            self.ui.eng_radio.setChecked(False)
        else:
            self.ui.eng_radio.setChecked(True)
            self.ui.rus_radio.setChecked(False)
        
        self.close()
    
    def load_text(self):
        global lang        
        
        if (lang =='RUS'):
            self.setWindowTitle(u"Выбор языка")
            self.ui.eng_radio.setText(u"English")
            self.ui.rus_radio.setText(u"Русский")
            self.ui.okbut.setText(u"Ok")
            self.ui.cancelbut.setText(u"Отмена")
        else:
            self.setWindowTitle(u"Change language")
            self.ui.eng_radio.setText(u"English")
            self.ui.rus_radio.setText(u"Русский")
            self.ui.okbut.setText(u"Ok")
            self.ui.cancelbut.setText(u"Cancel")
    
    def setup_language(self):
        global db
        global lang
        
        if (self.ui.rus_radio.isChecked()):
            lang = 'RUS'
        else:
            lang = 'ENG'
        
        if (sys.platform[0:3] == 'win'):
            config_new = os.getcwd()+"\\food_gui.ini"
            config_old = os.getcwd()+"/food_gui.ini.bckp"
        else:
            config_new = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini'))
            config_old = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini.bckp'))
        os.rename(config_new,  config_old)
            
        with open(config_old,  'r') as config_old_file:
            with open(config_new,  'w') as config_new_file:
                for line in config_old_file:
                    if (line.split('==')[0] == 'LANGUAGE'):
                        config_new_file.write('LANGUAGE=='+lang+'==\n')
                    else:
                        config_new_file.write(line)
        
        mainwindow = MainWindow()
        mainwindow.setup_language()
        os.remove (config_old)
        
        self._aboutwin.load_text()
        self._addwin.load_text()
        self._caclwin.load_text()
        self._dbcpwin.load_text()
        self._dbselwin.load_text()
        self._editwin.load_text()
        self._helpwin.load_text()
        self.load_text()
        self._notfoundwin.load_text()
        self._searchwin.load_text()
        self._mainwin.load_text()
        
        if (sys.platform[0:3] == 'win'):
            if (os.path.exists(os.getcwd()+"\\db_rus.dat")):
                db_old = db+".old"
                if (os.path.exists(db_old)):
                    os.remove (db_old)
                os.rename(db,  db_old)
                if (lang=='RUS'):
                    db_standart = os.getcwd()+"\\db_rus.dat"
                    shutil.copy(db_standart, db)
                else:
                    db_standart = os.getcwd()+"\\db_eng.dat"
                    shutil.copy(db_standart, db)
        else:
            if (os.path.exists("/usr/lib/food_gui/db_eng.dat")):
                db_old = db+".old"
                if (os.path.exists(db_old)):
                    os.remove (db_old)
                os.rename(db,  db_old)
                if (lang=='RUS'):
                    db_standart = "/usr/lib/food_gui/db_rus.dat"
                    shutil.copy(db_standart, db)
                else:
                    db_standart = "/usr/lib/food_gui/db_eng.dat"
                    shutil.copy(db_standart, db)
        
        self.close()
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close()


class NotFound(QtGui.QMainWindow):
    def __init__(self, parent=None, text=None):
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NotFound()
        self.ui.setupUi(self)
        
        self.load_text()
        
        if (text != None):
            self.ui.label.setText(text)

    def load_text(self):
        global lang
        
        if (lang =='RUS'):
            self.setWindowTitle(u"Ошибка!")
            self.ui.label.setText(u"<html><head/><body><p align=\"justify\"><br></p></body></html>")
            self.ui.okbut.setText(u"Ok")
        else:
            self.setWindowTitle(u"Error!")
            self.ui.label.setText(u"<html><head/><body><p align=\"justify\"><br></p></body></html>")
            self.ui.okbut.setText(u"Ok")

class SearchWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Search_Window()
        self.ui.setupUi(self)
        
        self.load_text()
        
        QtCore.QObject.connect(self.ui.exitbut, QtCore.SIGNAL("clicked()"), self.close_win)
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), self.search)
        QtCore.QObject.connect(self.ui.search_line, QtCore.SIGNAL("returnPressed()"), self.search)
    
    def close_win(self):
        self.ui.search_line.clear()
        self.ui.search_box.clear()
        
        self.close()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Поиск")
            self.ui.exitbut.setText(u"Закрыть")
            self.ui.searchbut.setText(u"Искать")
        else:
            self.setWindowTitle(u"Search")
            self.ui.exitbut.setText(u"Close")
            self.ui.searchbut.setText(u"Search")
    
    def search(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
        
        if (len(search) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Задано короткое имя</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Set too short food name</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            text=""
            for line in dbfile:
                if (line.split(';;')[0].find(search) > -1):
                    text = text+line.split(';;')[0]+"\n"
                    i = 1
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт, содержащий \""+search+u"\",<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food name with \""+search+u"\",<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        self.ui.search_box.setText(text)
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape):
            self.close_win()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        global db
        global lang
        
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Food()
        self.ui.setupUi(self)

        self.setup_database()
        self.setup_language()
        if (os.path.exists(db) == False):
            if (sys.platform[0:3] == 'win'):
                if (os.path.exists(os.getcwd()+"\\db_rus.dat")):
                    if (lang=='RUS'):
                        db_standart = os.getcwd()+"\\db_rus.dat"
                        shutil.copy(db_standart, db)
                    else:
                        db_standart = os.getcwd()+"\\db_eng.dat"
                        shutil.copy(db_standart, db)
                else:
                    with open(db,  'w') as dbfile:                                      
                        dbfile.write("") 
            else:
                if (os.path.exists("/usr/lib/food_gui/db_eng.dat")):
                    if (lang=='RUS'):
                        db_standart = "/usr/lib/food_gui/db_rus.dat"
                        shutil.copy(db_standart, db)
                    else:
                        db_standart = "/usr/lib/food_gui/db_eng.dat"
                        shutil.copy(db_standart, db)
                else:
                    with open(db,  'w') as dbfile:                                      
                        dbfile.write("") 
        
        self.load_text()

        self.ui.mass_line.setText("100")
        
        about_window = AboutWindow (parent=self)
        add_window = AddWindow (parent=self)
        calc_window = CalcWindow (parent=self)
        dbcp_window = DBcpWindow (parent=self)
        dbselect_window = DBselWindow (parent=self)
        edit_window = EditWindow (parent=self)
        help_window = Help (parent=self)
        notfound_window = NotFound (parent=self)
        search_window = SearchWindow (parent=self)
        lang_window = Language (parent=self, aboutwin=about_window, addwin=add_window, caclwin=calc_window, dbcpwin=dbcp_window, dbselwin=dbselect_window, editwin=edit_window, helpwin=help_window, notfoundwin=notfound_window, searchwin=search_window, mainwin=self)
        
        QtCore.QObject.connect(self.ui.menu_about, QtCore.SIGNAL("triggered()"), about_window.show)
        QtCore.QObject.connect(self.ui.menu_add, QtCore.SIGNAL("triggered()"), add_window.show)
        QtCore.QObject.connect(self.ui.menu_create, QtCore.SIGNAL("triggered()"), calc_window.show)
        QtCore.QObject.connect(self.ui.menu_dbcp, QtCore.SIGNAL("triggered()"), dbcp_window.show)
        QtCore.QObject.connect(self.ui.menu_dbsel, QtCore.SIGNAL("triggered()"), dbselect_window.show)
        QtCore.QObject.connect(self.ui.menu_edit, QtCore.SIGNAL("triggered()"), edit_window.show)
        QtCore.QObject.connect(self.ui.menu_help, QtCore.SIGNAL("triggered()"), help_window.show)
        QtCore.QObject.connect(self.ui.menu_lang, QtCore.SIGNAL("triggered()"), lang_window.show)
        QtCore.QObject.connect(self.ui.menu_search, QtCore.SIGNAL("triggered()"), search_window.show)
        QtCore.QObject.connect(self.ui.calcbut, QtCore.SIGNAL("clicked()"), self.calcucate)
        QtCore.QObject.connect(self.ui.searchbut, QtCore.SIGNAL("clicked()"), search_window.show)
        QtCore.QObject.connect(self.ui.search_line, QtCore.SIGNAL("returnPressed()"), self.complete)
        QtCore.QObject.connect(self.ui.substitutebut, QtCore.SIGNAL("clicked()"), self.complete)
    
    def calcucate(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
    
        if (len(search) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт не задан</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        if (len(self.ui.mass_line.text()) == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Масса не задана</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Weight isn't set</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        else:
            mass = float(self.ui.mass_line.text())
    
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (search == line.split(';;')[0]):
                    prop = [mass/100*float(num) for num in line.split(';;')[1:5]]
                    glyc_fl = float(line.split(';;')[5])
                    i = 1
                    break
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт \""+search+u"\"<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food \""+search+u"\"<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
    
        prot = "<html><head/><body><p align=\"right\">"+str(round(prop[0], 3))+"</p></body></html>"
        lip = "<html><head/><body><p align=\"right\">"+str(round(prop[1], 3))+"</p></body></html>"
        carb = "<html><head/><body><p align=\"right\">"+str(round(prop[2], 3))+"</p></body></html>"
        ccal = "<html><head/><body><p align=\"right\">"+str(round(prop[3], 3))+"</p></body></html>"
        glyc = "<html><head/><body><p align=\"right\">"+str(round(glyc_fl, 3))+"</p></body></html>"
    
        self.ui.prot_sec_lab.setText(prot)
        self.ui.lip_sec_lab.setText(lip)
        self.ui.carb_sec_lab.setText(carb)
        self.ui.ccal_sec_lab.setText(ccal)
        self.ui.glyc_sec_lab.setText(glyc)
    
    def complete(self):
        global db
        global lang
        
        search = self.ui.search_line.text().toLower()
    
        if (len(search) < 3):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Задано короткое имя</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Set too short food name</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        
        with open(db,'r') as dbfile:
            i = 0
            for line in dbfile:
                if (line.split(';;')[0].find(search) > -1):
                    output = line.split(';;')[0]
                    i = i + 1
        
        if (i == 0):
            if (lang == 'RUS'):
                inv_subs = u"<html><head/><body><p align=\"center\">Продукт, содержащий \""+search+u"\",<br>не найден в базе данных</p></body></html>"
            else:
                inv_subs = u"<html><head/><body><p align=\"center\">Food name with \""+search+u"\",<br>isn't found in database</p></body></html>"
            not_found = NotFound(parent=self, text=inv_subs)
            not_found.show()
            return
        elif (i == 1):
            self.ui.search_line.setText(output)
        elif (i > 1):
            complete_window = CompleteWindow (parent=self,  search=search,  put_search_line=self.ui.search_line)
            complete_window.show()
    
    def load_text(self):
        global lang
        
        if (lang == 'RUS'):
            self.setWindowTitle(u"Food_gui")
            self.ui.calcbut.setText(u"Посчитать")
            self.ui.mass_lab.setText(u"Масса, г")
            self.ui.prot_lab.setText(u"Белки")
            self.ui.lip_lab.setText(u"Жиры")
            self.ui.carb_lab.setText(u"Углеводы")
            self.ui.ccal_lab.setText(u"Калорийность, ккал")
            self.ui.glyc_lab.setText(u"Гликемический индекс")
            self.ui.prot_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.lip_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.ccal_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.glyc_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.searchbut.setText(u"Окно поиска")
            self.ui.substitutebut.setText(u"Подставить")
            self.ui.menu.setTitle(u"&Меню")
            self.ui.menu_2.setTitle(u"&Справка")
            self.ui.menu_3.setTitle(u"&Настройки")
            self.ui.menu_add.setText(u"&Добавить продукт в базу данных")
            self.ui.menu_add.setShortcut(u"Ctrl+N")
            self.ui.menu_edit.setText(u"&Редактировать базу данных")
            self.ui.menu_edit.setShortcut(u"Ctrl+W")
            self.ui.menu_create.setText(u"&Создать меню")
            self.ui.menu_create.setShortcut(u"Ctrl+M")
            self.ui.menu_dbcp.setText(u"С&копировать базу данных")
            self.ui.menu_exit.setText(u"&Выход")
            self.ui.menu_exit.setShortcut(u"Ctrl+Q")
            self.ui.menu_about.setText(u"&О программе")
            self.ui.menu_dbsel.setText(u"Выбрать &базу данных")
            self.ui.menu_search.setText(u"&Искать продукт в базе данных")
            self.ui.menu_search.setShortcut(u"Ctrl+S")
            self.ui.menu_lang.setText(u"Выбрать &язык")
            self.ui.menu_help.setText(u"&Помощь")
            self.ui.menu_help.setShortcut(u"F1")
        else:
            self.setWindowTitle(u"Food_gui")
            self.ui.calcbut.setText(u"Calculate")
            self.ui.mass_lab.setText(u"Weight, g")
            self.ui.prot_lab.setText(u"Proteins")
            self.ui.lip_lab.setText(u"Fats")
            self.ui.carb_lab.setText(u"Carbohydrates")
            self.ui.ccal_lab.setText(u"Food energy, kcal")
            self.ui.glyc_lab.setText(u"Glycemic index")
            self.ui.prot_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.lip_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.carb_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.ccal_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.glyc_sec_lab.setText(u"<html><head/><body><p align=\"right\"><br/></p></body></html>")
            self.ui.searchbut.setText(u"Search window")
            self.ui.substitutebut.setText(u"Autocomplete")
            self.ui.menu.setTitle(u"&Menu")
            self.ui.menu_2.setTitle(u"&Help")
            self.ui.menu_3.setTitle(u"&Settings")
            self.ui.menu_add.setText(u"&Add item in database")
            self.ui.menu_add.setShortcut(u"Ctrl+N")
            self.ui.menu_edit.setText(u"&Edit database")
            self.ui.menu_edit.setShortcut(u"Ctrl+W")
            self.ui.menu_create.setText(u"&Create menu")
            self.ui.menu_create.setShortcut(u"Ctrl+M")
            self.ui.menu_dbcp.setText(u"&Copy database")
            self.ui.menu_exit.setText(u"E&xit")
            self.ui.menu_exit.setShortcut(u"Ctrl+Q")
            self.ui.menu_about.setText(u"&About")
            self.ui.menu_dbsel.setText(u"Choose &database")
            self.ui.menu_search.setText(u"&Search item in database")
            self.ui.menu_search.setShortcut(u"Ctrl+S")
            self.ui.menu_lang.setText(u"&Language")
            self.ui.menu_help.setText(u"&Help")
            self.ui.menu_help.setShortcut(u"F1")
    
    def setup_database(self):
        global db
        
        if (sys.platform[0:3] == 'win'):
            config = os.getcwd()+"\\food_gui.ini"
        else:
            config = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini'))
        
        if (os.path.exists(config)):
            i = 0
            with open(config,  'r') as config_file:
                for line in config_file:
                    if (line.split('==')[0] == 'DATABASE'):
                        db = line.split('==')[1]
                        i = 1
            if (i == 0):
                with open(config,  'a') as config_file:
                    if (sys.platform[0:3] == 'win'):
                        db = os.getcwd()+"\\db.dat"
                        config_file.write('DATABASE=='+db+'==\n')
                    else:
                        db = os.path.abspath(os.path.expanduser('~/.config/food_gui/db.dat'))
                        config_file.write('DATABASE=='+db+'==\n')
        else:
            if (sys.platform[0:5] == 'linux' and not os.path.exists(os.path.abspath(os.path.expanduser('~/.config/food_gui')))):
                os.makedirs(os.path.abspath(os.path.expanduser('~/.config/food_gui')))
            with open(config,  'w') as config_file:
                if (sys.platform[0:3] == 'win'):
                    db = os.getcwd()+"\\db.dat"
                    config_file.write('DATABASE=='+db+'==\n')
                else:
                    db = os.path.abspath(os.path.expanduser('~/.config/food_gui/db.dat'))
                    config_file.write('DATABASE=='+db+'==\n')
    
    def setup_language(self):
        global lang
        
        if (sys.platform[0:3] == 'win'):
            config = os.getcwd()+"\\food_gui.ini"
        else:
            config = os.path.abspath(os.path.expanduser('~/.config/food_gui/food_gui.ini'))
        
        if (os.path.exists(config)):
            i = 0
            with open(config,  'r') as config_file:
                for line in config_file:
                    if (line.split('==')[0] == 'LANGUAGE'):
                        lang = line.split('==')[1]
                        i = 1
            if (i == 0):
                with open(config,  'a') as config_file:
                    lang = 'ENG'
                    config_file.write("LANGUAGE=="+lang+"==\n")
        else:
            if (sys.platform[0:5] == 'linux' and not os.path.exists(os.path.abspath(os.path.expanduser('~/.config/food_gui')))):
                os.makedirs(os.path.abspath(os.path.expanduser('~/.config/food_gui')))
            with open(config,  'w') as config_file:
                lang = 'ENG'
                config_file.write("LANGUAGE=="+lang+"==\n")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    codec = QtCore.QTextCodec.codecForName("UTF-8")
    QtCore.QTextCodec.setCodecForCStrings(codec)
    
    FoodGui = MainWindow()
    FoodGui.show()
    sys.exit(app.exec_())
