# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_attributes.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AttributesWidget(object):
    def setupUi(self, AttributesWidget):
        if not AttributesWidget.objectName():
            AttributesWidget.setObjectName(u"AttributesWidget")
        AttributesWidget.resize(423, 313)
        self.verticalLayout = QVBoxLayout(AttributesWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.attributes = QTableWidget(AttributesWidget)
        if (self.attributes.columnCount() < 2):
            self.attributes.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.attributes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.attributes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.attributes.setObjectName(u"attributes")
        self.attributes.setAlternatingRowColors(True)
        self.attributes.horizontalHeader().setStretchLastSection(True)
        self.attributes.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.attributes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(AttributesWidget)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.remove = QPushButton(AttributesWidget)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AttributesWidget)

        QMetaObject.connectSlotsByName(AttributesWidget)
    # setupUi

    def retranslateUi(self, AttributesWidget):
        AttributesWidget.setWindowTitle(QCoreApplication.translate("AttributesWidget", u"Form", None))
        ___qtablewidgetitem = self.attributes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AttributesWidget", u"Attribute", None));
        ___qtablewidgetitem1 = self.attributes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AttributesWidget", u"Value", None));
        self.add.setText(QCoreApplication.translate("AttributesWidget", u"Add", None))
        self.remove.setText(QCoreApplication.translate("AttributesWidget", u"Delete", None))
    # retranslateUi

