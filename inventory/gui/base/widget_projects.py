# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_projects.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_WidgetProjects(object):
    def setupUi(self, WidgetProjects):
        if not WidgetProjects.objectName():
            WidgetProjects.setObjectName(u"WidgetProjects")
        WidgetProjects.resize(379, 541)
        self.verticalLayout = QVBoxLayout(WidgetProjects)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(WidgetProjects)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove = QPushButton(WidgetProjects)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.projects = QTreeWidget(WidgetProjects)
        self.projects.setObjectName(u"projects")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.projects.sizePolicy().hasHeightForWidth())
        self.projects.setSizePolicy(sizePolicy)
        self.projects.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.projects.setAlternatingRowColors(True)
        self.projects.setRootIsDecorated(False)
        self.projects.setColumnCount(2)

        self.verticalLayout.addWidget(self.projects)


        self.retranslateUi(WidgetProjects)

        QMetaObject.connectSlotsByName(WidgetProjects)
    # setupUi

    def retranslateUi(self, WidgetProjects):
        WidgetProjects.setWindowTitle(QCoreApplication.translate("WidgetProjects", u"Form", None))
        self.add.setText(QCoreApplication.translate("WidgetProjects", u"Add Project", None))
        self.remove.setText(QCoreApplication.translate("WidgetProjects", u"Remove Project", None))
        ___qtreewidgetitem = self.projects.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("WidgetProjects", u"Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("WidgetProjects", u"Project", None));
    # retranslateUi

