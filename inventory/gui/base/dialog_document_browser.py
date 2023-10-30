# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_document_browser.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DocumentBrowserDialog(object):
    def setupUi(self, DocumentBrowserDialog):
        if not DocumentBrowserDialog.objectName():
            DocumentBrowserDialog.setObjectName(u"DocumentBrowserDialog")
        DocumentBrowserDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DocumentBrowserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filter = QLineEdit(DocumentBrowserDialog)
        self.filter.setObjectName(u"filter")

        self.verticalLayout.addWidget(self.filter)

        self.documents = QListWidget(DocumentBrowserDialog)
        self.documents.setObjectName(u"documents")

        self.verticalLayout.addWidget(self.documents)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(DocumentBrowserDialog)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.remove = QPushButton(DocumentBrowserDialog)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttons = QDialogButtonBox(DocumentBrowserDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(DocumentBrowserDialog)
        self.buttons.accepted.connect(DocumentBrowserDialog.accept)
        self.buttons.rejected.connect(DocumentBrowserDialog.reject)

        QMetaObject.connectSlotsByName(DocumentBrowserDialog)
    # setupUi

    def retranslateUi(self, DocumentBrowserDialog):
        DocumentBrowserDialog.setWindowTitle(QCoreApplication.translate("DocumentBrowserDialog", u"Document Browser", None))
        self.filter.setPlaceholderText(QCoreApplication.translate("DocumentBrowserDialog", u"Filter...", None))
        self.add.setText(QCoreApplication.translate("DocumentBrowserDialog", u"Add Document", None))
        self.remove.setText(QCoreApplication.translate("DocumentBrowserDialog", u"Delete Document", None))
    # retranslateUi

