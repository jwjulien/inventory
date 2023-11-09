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
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

from inventory.gui.widgets.file_select import FileSelectWidget

class Ui_DocumentDialog(object):
    def setupUi(self, DocumentDialog):
        if not DocumentDialog.objectName():
            DocumentDialog.setObjectName(u"DocumentDialog")
        DocumentDialog.resize(542, 185)
        self.formLayout = QFormLayout(DocumentDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.select_file = QRadioButton(DocumentDialog)
        self.select_file.setObjectName(u"select_file")
        self.select_file.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.select_file)

        self.file = FileSelectWidget(DocumentDialog)
        self.file.setObjectName(u"file")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.file)

        self.select_url = QRadioButton(DocumentDialog)
        self.select_url.setObjectName(u"select_url")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.select_url)

        self.url = QLineEdit(DocumentDialog)
        self.url.setObjectName(u"url")
        self.url.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.url)

        self.lbl_label = QLabel(DocumentDialog)
        self.lbl_label.setObjectName(u"lbl_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)

        self.buttons = QDialogButtonBox(DocumentDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.buttons)

        self.lbl_filename = QLabel(DocumentDialog)
        self.lbl_filename.setObjectName(u"lbl_filename")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_filename)

        self.filename = QLineEdit(DocumentDialog)
        self.filename.setObjectName(u"filename")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.filename)

        self.label = QComboBox(DocumentDialog)
        self.label.addItem("")
        self.label.addItem("")
        self.label.addItem("")
        self.label.addItem("")
        self.label.addItem("")
        self.label.setObjectName(u"label")
        self.label.setEditable(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label)


        self.retranslateUi(DocumentDialog)
        self.buttons.accepted.connect(DocumentDialog.accept)
        self.buttons.rejected.connect(DocumentDialog.reject)

        QMetaObject.connectSlotsByName(DocumentDialog)
    # setupUi

    def retranslateUi(self, DocumentDialog):
        DocumentDialog.setWindowTitle(QCoreApplication.translate("DocumentDialog", u"Add Document", None))
        self.select_file.setText(QCoreApplication.translate("DocumentDialog", u"File:", None))
        self.select_url.setText(QCoreApplication.translate("DocumentDialog", u"URL:", None))
        self.lbl_label.setText(QCoreApplication.translate("DocumentDialog", u"Label:", None))
        self.lbl_filename.setText(QCoreApplication.translate("DocumentDialog", u"Filename:", None))
        self.label.setItemText(0, "")
        self.label.setItemText(1, QCoreApplication.translate("DocumentDialog", u"Datasheet", None))
        self.label.setItemText(2, QCoreApplication.translate("DocumentDialog", u"Drawing", None))
        self.label.setItemText(3, QCoreApplication.translate("DocumentDialog", u"Specifications", None))
        self.label.setItemText(4, QCoreApplication.translate("DocumentDialog", u"Model", None))

    # retranslateUi

