# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_areas.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_WidgetAreas(object):
    def setupUi(self, WidgetAreas):
        if not WidgetAreas.objectName():
            WidgetAreas.setObjectName(u"WidgetAreas")
        WidgetAreas.resize(379, 541)
        self.verticalLayout_2 = QVBoxLayout(WidgetAreas)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.group = QGroupBox(WidgetAreas)
        self.group.setObjectName(u"group")
        self.verticalLayout = QVBoxLayout(self.group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.areas = QListWidget(self.group)
        self.areas.setObjectName(u"areas")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.areas.sizePolicy().hasHeightForWidth())
        self.areas.setSizePolicy(sizePolicy)
        self.areas.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.areas.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.areas)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(self.group)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.remove = QPushButton(self.group)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.group)


        self.retranslateUi(WidgetAreas)

        QMetaObject.connectSlotsByName(WidgetAreas)
    # setupUi

    def retranslateUi(self, WidgetAreas):
        WidgetAreas.setWindowTitle(QCoreApplication.translate("WidgetAreas", u"Form", None))
        self.group.setTitle(QCoreApplication.translate("WidgetAreas", u"Areas:", None))
        self.add.setText(QCoreApplication.translate("WidgetAreas", u"Add", None))
        self.remove.setText(QCoreApplication.translate("WidgetAreas", u"Remove", None))
    # retranslateUi

