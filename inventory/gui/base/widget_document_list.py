# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_document_list.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DocumentListWidget(object):
    def setupUi(self, DocumentListWidget):
        if not DocumentListWidget.objectName():
            DocumentListWidget.setObjectName(u"DocumentListWidget")
        DocumentListWidget.resize(274, 300)
        self.verticalLayout = QVBoxLayout(DocumentListWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.group = QGroupBox(DocumentListWidget)
        self.group.setObjectName(u"group")
        self.verticalLayout_2 = QVBoxLayout(self.group)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.documents = QListWidget(self.group)
        self.documents.setObjectName(u"documents")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.documents.sizePolicy().hasHeightForWidth())
        self.documents.setSizePolicy(sizePolicy)
        self.documents.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.documents.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.documents)

        self.add = QPushButton(self.group)
        self.add.setObjectName(u"add")

        self.verticalLayout_2.addWidget(self.add)


        self.verticalLayout.addWidget(self.group)


        self.retranslateUi(DocumentListWidget)

        QMetaObject.connectSlotsByName(DocumentListWidget)
    # setupUi

    def retranslateUi(self, DocumentListWidget):
        DocumentListWidget.setWindowTitle(QCoreApplication.translate("DocumentListWidget", u"Form", None))
        self.group.setTitle(QCoreApplication.translate("DocumentListWidget", u"Documents:", None))
        self.add.setText(QCoreApplication.translate("DocumentListWidget", u"Add Document", None))
    # retranslateUi

