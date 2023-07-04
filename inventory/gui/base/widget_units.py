# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_units.ui'
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
    QHeaderView, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_WidgetUnits(object):
    def setupUi(self, WidgetUnits):
        if not WidgetUnits.objectName():
            WidgetUnits.setObjectName(u"WidgetUnits")
        WidgetUnits.resize(336, 535)
        self.verticalLayout_2 = QVBoxLayout(WidgetUnits)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.group = QGroupBox(WidgetUnits)
        self.group.setObjectName(u"group")
        self.verticalLayout = QVBoxLayout(self.group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.units = QTableWidget(self.group)
        if (self.units.columnCount() < 3):
            self.units.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.units.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.units.setObjectName(u"units")
        self.units.setAlternatingRowColors(True)
        self.units.setSelectionMode(QAbstractItemView.SingleSelection)
        self.units.horizontalHeader().setStretchLastSection(True)
        self.units.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.units)

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


        self.retranslateUi(WidgetUnits)

        QMetaObject.connectSlotsByName(WidgetUnits)
    # setupUi

    def retranslateUi(self, WidgetUnits):
        WidgetUnits.setWindowTitle(QCoreApplication.translate("WidgetUnits", u"Form", None))
        self.group.setTitle(QCoreApplication.translate("WidgetUnits", u"Units:", None))
        ___qtablewidgetitem = self.units.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WidgetUnits", u"Name", None));
        ___qtablewidgetitem1 = self.units.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WidgetUnits", u"Rows", None));
        ___qtablewidgetitem2 = self.units.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WidgetUnits", u"Columns", None));
        self.add.setText(QCoreApplication.translate("WidgetUnits", u"Add", None))
        self.remove.setText(QCoreApplication.translate("WidgetUnits", u"Remove", None))
    # retranslateUi

