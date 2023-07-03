# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_categories.ui'
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
    QListWidget, QListWidgetItem, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_TabCategories(object):
    def setupUi(self, TabCategories):
        if not TabCategories.objectName():
            TabCategories.setObjectName(u"TabCategories")
        TabCategories.resize(870, 683)
        self.horizontalLayout = QHBoxLayout(TabCategories)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.categories = QTreeWidget(TabCategories)
        self.categories.setObjectName(u"categories")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categories.sizePolicy().hasHeightForWidth())
        self.categories.setSizePolicy(sizePolicy)
        self.categories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.categories.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout.addWidget(self.categories)

        self.parts = QListWidget(TabCategories)
        self.parts.setObjectName(u"parts")
        sizePolicy.setHeightForWidth(self.parts.sizePolicy().hasHeightForWidth())
        self.parts.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.parts)


        self.retranslateUi(TabCategories)

        QMetaObject.connectSlotsByName(TabCategories)
    # setupUi

    def retranslateUi(self, TabCategories):
        TabCategories.setWindowTitle(QCoreApplication.translate("TabCategories", u"Form", None))
        ___qtreewidgetitem = self.categories.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("TabCategories", u"Designator", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("TabCategories", u"Title", None));
    # retranslateUi

