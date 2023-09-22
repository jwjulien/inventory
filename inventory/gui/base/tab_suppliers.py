# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_suppliers.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from inventory.gui.widgets.parts import PartsWidget

class Ui_TabSuppliers(object):
    def setupUi(self, TabSuppliers):
        if not TabSuppliers.objectName():
            TabSuppliers.setObjectName(u"TabSuppliers")
        TabSuppliers.resize(810, 611)
        self.horizontalLayout_2 = QHBoxLayout(TabSuppliers)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.supplier_widget = QWidget(TabSuppliers)
        self.supplier_widget.setObjectName(u"supplier_widget")
        self.verticalLayout = QVBoxLayout(self.supplier_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.suppliers = QListWidget(self.supplier_widget)
        self.suppliers.setObjectName(u"suppliers")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suppliers.sizePolicy().hasHeightForWidth())
        self.suppliers.setSizePolicy(sizePolicy)
        self.suppliers.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.suppliers)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(self.supplier_widget)
        self.add.setObjectName(u"add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.add)

        self.remove = QPushButton(self.supplier_widget)
        self.remove.setObjectName(u"remove")
        sizePolicy1.setHeightForWidth(self.remove.sizePolicy().hasHeightForWidth())
        self.remove.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addWidget(self.supplier_widget)

        self.tabs = QTabWidget(TabSuppliers)
        self.tabs.setObjectName(u"tabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy2)
        self.parts_tab = QWidget()
        self.parts_tab.setObjectName(u"parts_tab")
        self.verticalLayout_2 = QVBoxLayout(self.parts_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.parts = PartsWidget(self.parts_tab)
        self.parts.setObjectName(u"parts")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.parts.sizePolicy().hasHeightForWidth())
        self.parts.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.parts)

        self.tabs.addTab(self.parts_tab, "")
        self.restock_tab = QWidget()
        self.restock_tab.setObjectName(u"restock_tab")
        self.verticalLayout_3 = QVBoxLayout(self.restock_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.restock = PartsWidget(self.restock_tab)
        self.restock.setObjectName(u"restock")
        sizePolicy3.setHeightForWidth(self.restock.sizePolicy().hasHeightForWidth())
        self.restock.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.restock)

        self.tabs.addTab(self.restock_tab, "")

        self.horizontalLayout_2.addWidget(self.tabs)


        self.retranslateUi(TabSuppliers)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabSuppliers)
    # setupUi

    def retranslateUi(self, TabSuppliers):
        TabSuppliers.setWindowTitle(QCoreApplication.translate("TabSuppliers", u"Form", None))
        self.add.setText(QCoreApplication.translate("TabSuppliers", u"Add", None))
        self.remove.setText(QCoreApplication.translate("TabSuppliers", u"Remove", None))
        self.tabs.setTabText(self.tabs.indexOf(self.parts_tab), QCoreApplication.translate("TabSuppliers", u"Parts", None))
        self.tabs.setTabText(self.tabs.indexOf(self.restock_tab), QCoreApplication.translate("TabSuppliers", u"Restock", None))
    # retranslateUi

