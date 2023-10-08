# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_materials.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MaterialWidget(object):
    def setupUi(self, MaterialWidget):
        if not MaterialWidget.objectName():
            MaterialWidget.setObjectName(u"MaterialWidget")
        MaterialWidget.resize(806, 187)
        self.verticalLayout = QVBoxLayout(MaterialWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.materials = QTableWidget(MaterialWidget)
        if (self.materials.columnCount() < 3):
            self.materials.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.materials.setObjectName(u"materials")
        self.materials.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.materials.setSelectionMode(QAbstractItemView.SingleSelection)
        self.materials.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.materials.horizontalHeader().setDefaultSectionSize(250)
        self.materials.horizontalHeader().setStretchLastSection(True)
        self.materials.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.materials)


        self.retranslateUi(MaterialWidget)

        QMetaObject.connectSlotsByName(MaterialWidget)
    # setupUi

    def retranslateUi(self, MaterialWidget):
        MaterialWidget.setWindowTitle(QCoreApplication.translate("MaterialWidget", u"Form", None))
        ___qtablewidgetitem = self.materials.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MaterialWidget", u"Project", None));
        ___qtablewidgetitem1 = self.materials.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MaterialWidget", u"Revision", None));
        ___qtablewidgetitem2 = self.materials.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MaterialWidget", u"Designator", None));
    # retranslateUi

