# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_revisions.ui'
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

class Ui_WidgetRevisions(object):
    def setupUi(self, WidgetRevisions):
        if not WidgetRevisions.objectName():
            WidgetRevisions.setObjectName(u"WidgetRevisions")
        WidgetRevisions.resize(379, 541)
        self.verticalLayout = QVBoxLayout(WidgetRevisions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(WidgetRevisions)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove = QPushButton(WidgetRevisions)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)

        self.view_bom = QPushButton(WidgetRevisions)
        self.view_bom.setObjectName(u"view_bom")

        self.horizontalLayout.addWidget(self.view_bom)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.revisions = QTreeWidget(WidgetRevisions)
        self.revisions.setObjectName(u"revisions")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.revisions.sizePolicy().hasHeightForWidth())
        self.revisions.setSizePolicy(sizePolicy)
        self.revisions.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.revisions.setAlternatingRowColors(True)
        self.revisions.setRootIsDecorated(False)
        self.revisions.setColumnCount(2)
        self.revisions.header().setDefaultSectionSize(150)

        self.verticalLayout.addWidget(self.revisions)


        self.retranslateUi(WidgetRevisions)

        QMetaObject.connectSlotsByName(WidgetRevisions)
    # setupUi

    def retranslateUi(self, WidgetRevisions):
        WidgetRevisions.setWindowTitle(QCoreApplication.translate("WidgetRevisions", u"Form", None))
        self.add.setText(QCoreApplication.translate("WidgetRevisions", u"Add Revision", None))
        self.remove.setText(QCoreApplication.translate("WidgetRevisions", u"Remove Revision", None))
        self.view_bom.setText(QCoreApplication.translate("WidgetRevisions", u"View BOM", None))
        ___qtreewidgetitem = self.revisions.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("WidgetRevisions", u"Date", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("WidgetRevisions", u"Revision", None));
    # retranslateUi

