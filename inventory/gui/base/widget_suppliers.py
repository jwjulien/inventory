# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_suppliers.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_SuppliersWidget(object):
    def setupUi(self, SuppliersWidget):
        if not SuppliersWidget.objectName():
            SuppliersWidget.setObjectName(u"SuppliersWidget")
        SuppliersWidget.resize(887, 179)
        self.horizontalLayout = QHBoxLayout(SuppliersWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.suppliers = QTableWidget(SuppliersWidget)
        if (self.suppliers.columnCount() < 2):
            self.suppliers.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.suppliers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.suppliers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.suppliers.setObjectName(u"suppliers")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.suppliers.sizePolicy().hasHeightForWidth())
        self.suppliers.setSizePolicy(sizePolicy)
        self.suppliers.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.suppliers.setSelectionMode(QAbstractItemView.SingleSelection)
        self.suppliers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.suppliers.horizontalHeader().setStretchLastSection(True)
        self.suppliers.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.suppliers)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.map = QPushButton(SuppliersWidget)
        self.map.setObjectName(u"map")

        self.verticalLayout.addWidget(self.map)

        self.edit = QPushButton(SuppliersWidget)
        self.edit.setObjectName(u"edit")
        self.edit.setEnabled(False)

        self.verticalLayout.addWidget(self.edit)

        self.remove = QPushButton(SuppliersWidget)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)

        self.verticalLayout.addWidget(self.remove)

        self.search = QPushButton(SuppliersWidget)
        self.search.setObjectName(u"search")
        self.search.setEnabled(False)

        self.verticalLayout.addWidget(self.search)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(SuppliersWidget)

        QMetaObject.connectSlotsByName(SuppliersWidget)
    # setupUi

    def retranslateUi(self, SuppliersWidget):
        SuppliersWidget.setWindowTitle(QCoreApplication.translate("SuppliersWidget", u"Form", None))
        ___qtablewidgetitem = self.suppliers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SuppliersWidget", u"Supplier", None));
        ___qtablewidgetitem1 = self.suppliers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SuppliersWidget", u"Part Number", None));
        self.map.setText(QCoreApplication.translate("SuppliersWidget", u"Add New", None))
        self.edit.setText(QCoreApplication.translate("SuppliersWidget", u"Edit", None))
        self.remove.setText(QCoreApplication.translate("SuppliersWidget", u"Remove", None))
        self.search.setText(QCoreApplication.translate("SuppliersWidget", u"Web Search", None))
    # retranslateUi

