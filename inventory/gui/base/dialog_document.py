# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_document.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from inventory.gui.widgets.file_select import FileSelectWidget

class Ui_DocumentDialog(object):
    def setupUi(self, DocumentDialog):
        if not DocumentDialog.objectName():
            DocumentDialog.setObjectName(u"DocumentDialog")
        DocumentDialog.resize(400, 146)
        self.verticalLayout = QVBoxLayout(DocumentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.file = FileSelectWidget(DocumentDialog)
        self.file.setObjectName(u"file")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.file)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_title = QLabel(DocumentDialog)
        self.lbl_title.setObjectName(u"lbl_title")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_title)

        self.title = QLineEdit(DocumentDialog)
        self.title.setObjectName(u"title")
        self.title.setMaxLength(40)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.title)

        self.lbl_mime = QLabel(DocumentDialog)
        self.lbl_mime.setObjectName(u"lbl_mime")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_mime)

        self.mime = QComboBox(DocumentDialog)
        self.mime.addItem("")
        self.mime.addItem("")
        self.mime.setObjectName(u"mime")
        self.mime.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mime)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttons = QDialogButtonBox(DocumentDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(DocumentDialog)
        self.buttons.accepted.connect(DocumentDialog.accept)
        self.buttons.rejected.connect(DocumentDialog.reject)

        QMetaObject.connectSlotsByName(DocumentDialog)
    # setupUi

    def retranslateUi(self, DocumentDialog):
        DocumentDialog.setWindowTitle(QCoreApplication.translate("DocumentDialog", u"Document", None))
        self.lbl_title.setText(QCoreApplication.translate("DocumentDialog", u"Title:", None))
        self.lbl_mime.setText(QCoreApplication.translate("DocumentDialog", u"Mime:", None))
        self.mime.setItemText(0, QCoreApplication.translate("DocumentDialog", u"application/pdf", None))
        self.mime.setItemText(1, QCoreApplication.translate("DocumentDialog", u"application/markdown", None))

    # retranslateUi

