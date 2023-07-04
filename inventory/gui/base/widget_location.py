# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_location.ui'
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

class Ui_LocationWidget(object):
    def setupUi(self, LocationWidget):
        if not LocationWidget.objectName():
            LocationWidget.setObjectName(u"LocationWidget")
        LocationWidget.resize(925, 187)
        self.horizontalLayout = QHBoxLayout(LocationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.locations = QTableWidget(LocationWidget)
        if (self.locations.columnCount() < 3):
            self.locations.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.locations.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.locations.setObjectName(u"locations")
        self.locations.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.locations.setSelectionMode(QAbstractItemView.SingleSelection)
        self.locations.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.locations.horizontalHeader().setStretchLastSection(True)
        self.locations.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.locations)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.map = QPushButton(LocationWidget)
        self.map.setObjectName(u"map")

        self.verticalLayout.addWidget(self.map)

        self.edit = QPushButton(LocationWidget)
        self.edit.setObjectName(u"edit")
        self.edit.setEnabled(False)

        self.verticalLayout.addWidget(self.edit)

        self.remove = QPushButton(LocationWidget)
        self.remove.setObjectName(u"remove")
        self.remove.setEnabled(False)

        self.verticalLayout.addWidget(self.remove)

        self.relocate = QPushButton(LocationWidget)
        self.relocate.setObjectName(u"relocate")
        self.relocate.setEnabled(False)

        self.verticalLayout.addWidget(self.relocate)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(LocationWidget)

        QMetaObject.connectSlotsByName(LocationWidget)
    # setupUi

    def retranslateUi(self, LocationWidget):
        LocationWidget.setWindowTitle(QCoreApplication.translate("LocationWidget", u"Form", None))
        ___qtablewidgetitem = self.locations.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LocationWidget", u"Quantity", None));
        ___qtablewidgetitem1 = self.locations.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LocationWidget", u"Last Counted", None));
        ___qtablewidgetitem2 = self.locations.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LocationWidget", u"Location", None));
        self.map.setText(QCoreApplication.translate("LocationWidget", u"Add New", None))
        self.edit.setText(QCoreApplication.translate("LocationWidget", u"Edit", None))
        self.remove.setText(QCoreApplication.translate("LocationWidget", u"Remove", None))
        self.relocate.setText(QCoreApplication.translate("LocationWidget", u"Relocate", None))
    # retranslateUi

