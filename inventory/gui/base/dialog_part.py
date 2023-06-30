# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_part.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_DialogPart(object):
    def setupUi(self, DialogPart):
        if not DialogPart.objectName():
            DialogPart.setObjectName(u"DialogPart")
        DialogPart.resize(989, 764)
        self.buttonBox = QDialogButtonBox(DialogPart)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(630, 720, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.layoutWidget = QWidget(DialogPart)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 781, 200))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_category = QLabel(self.layoutWidget)
        self.lbl_category.setObjectName(u"lbl_category")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_category)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category = QComboBox(self.layoutWidget)
        self.category.setObjectName(u"category")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.category)

        self.new_category = QPushButton(self.layoutWidget)
        self.new_category.setObjectName(u"new_category")

        self.horizontalLayout.addWidget(self.new_category)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.lbl_value = QLabel(self.layoutWidget)
        self.lbl_value.setObjectName(u"lbl_value")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_value)

        self.lbl_number = QLabel(self.layoutWidget)
        self.lbl_number.setObjectName(u"lbl_number")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_number)

        self.lbl_package = QLabel(self.layoutWidget)
        self.lbl_package.setObjectName(u"lbl_package")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_package)

        self.lbl_price = QLabel(self.layoutWidget)
        self.lbl_price.setObjectName(u"lbl_price")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_price)

        self.lbl_weight = QLabel(self.layoutWidget)
        self.lbl_weight.setObjectName(u"lbl_weight")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_weight)

        self.value = QLineEdit(self.layoutWidget)
        self.value.setObjectName(u"value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.value)

        self.part_number = QLineEdit(self.layoutWidget)
        self.part_number.setObjectName(u"part_number")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.part_number)

        self.footprint = QLineEdit(self.layoutWidget)
        self.footprint.setObjectName(u"footprint")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.footprint)

        self.price = QDoubleSpinBox(self.layoutWidget)
        self.price.setObjectName(u"price")
        self.price.setProperty("showGroupSeparator", True)
        self.price.setDecimals(3)
        self.price.setMaximum(10000.000000000000000)
        self.price.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.price)

        self.lbl_reorder = QLabel(self.layoutWidget)
        self.lbl_reorder.setObjectName(u"lbl_reorder")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_reorder)

        self.threshold = QSpinBox(self.layoutWidget)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMaximum(100000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.threshold)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.weight = QDoubleSpinBox(self.layoutWidget)
        self.weight.setObjectName(u"weight")
        self.weight.setDecimals(3)
        self.weight.setMaximum(1000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.weight)

        self.calibrate = QPushButton(self.layoutWidget)
        self.calibrate.setObjectName(u"calibrate")

        self.horizontalLayout_5.addWidget(self.calibrate)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.layoutWidget_2 = QWidget(DialogPart)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 230, 531, 281))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.attributes = QListWidget(self.layoutWidget_2)
        self.attributes.setObjectName(u"attributes")

        self.verticalLayout_2.addWidget(self.attributes)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_attribute = QPushButton(self.layoutWidget_2)
        self.add_attribute.setObjectName(u"add_attribute")

        self.horizontalLayout_2.addWidget(self.add_attribute)

        self.remove_attribute = QPushButton(self.layoutWidget_2)
        self.remove_attribute.setObjectName(u"remove_attribute")
        self.remove_attribute.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.remove_attribute)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.layoutWidget_3 = QWidget(DialogPart)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(807, 10, 171, 201))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.image = QGraphicsView(self.layoutWidget_3)
        self.image.setObjectName(u"image")

        self.verticalLayout_3.addWidget(self.image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.set_image = QPushButton(self.layoutWidget_3)
        self.set_image.setObjectName(u"set_image")

        self.horizontalLayout_3.addWidget(self.set_image)

        self.remove_image = QPushButton(self.layoutWidget_3)
        self.remove_image.setObjectName(u"remove_image")
        self.remove_image.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.remove_image)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.quantities = QListWidget(DialogPart)
        self.quantities.setObjectName(u"quantities")
        self.quantities.setGeometry(QRect(10, 520, 531, 231))
        self.notes = QPlainTextEdit(DialogPart)
        self.notes.setObjectName(u"notes")
        self.notes.setGeometry(QRect(550, 230, 431, 151))
        self.layoutWidget_4 = QWidget(DialogPart)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(550, 390, 431, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.documents = QListWidget(self.layoutWidget_4)
        self.documents.setObjectName(u"documents")
        self.documents.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.documents.sizePolicy().hasHeightForWidth())
        self.documents.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.documents)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add_document = QPushButton(self.layoutWidget_4)
        self.add_document.setObjectName(u"add_document")

        self.horizontalLayout_4.addWidget(self.add_document)

        self.remove_document = QPushButton(self.layoutWidget_4)
        self.remove_document.setObjectName(u"remove_document")

        self.horizontalLayout_4.addWidget(self.remove_document)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(DialogPart)
        self.buttonBox.accepted.connect(DialogPart.accept)
        self.buttonBox.rejected.connect(DialogPart.reject)

        QMetaObject.connectSlotsByName(DialogPart)
    # setupUi

    def retranslateUi(self, DialogPart):
        DialogPart.setWindowTitle(QCoreApplication.translate("DialogPart", u"Dialog", None))
        self.lbl_category.setText(QCoreApplication.translate("DialogPart", u"Category:", None))
        self.new_category.setText(QCoreApplication.translate("DialogPart", u"New Category", None))
        self.lbl_value.setText(QCoreApplication.translate("DialogPart", u"Value:", None))
        self.lbl_number.setText(QCoreApplication.translate("DialogPart", u"Part Number:", None))
        self.lbl_package.setText(QCoreApplication.translate("DialogPart", u"Package:", None))
        self.lbl_price.setText(QCoreApplication.translate("DialogPart", u"Price:", None))
        self.lbl_weight.setText(QCoreApplication.translate("DialogPart", u"Weight:", None))
        self.price.setPrefix(QCoreApplication.translate("DialogPart", u"$", None))
        self.lbl_reorder.setText(QCoreApplication.translate("DialogPart", u"Reorder Threshold:", None))
#if QT_CONFIG(tooltip)
        self.threshold.setToolTip(QCoreApplication.translate("DialogPart", u"Part will appear in the reorder report when total quantity is LESS THAN this threshold.\n"
"\n"
"Set to zero to disable reorder (i.e. non-stocked) or set to one to reorder when completely gone.", None))
#endif // QT_CONFIG(tooltip)
        self.weight.setSuffix(QCoreApplication.translate("DialogPart", u"g", None))
        self.calibrate.setText(QCoreApplication.translate("DialogPart", u"Calibrate", None))
        self.add_attribute.setText(QCoreApplication.translate("DialogPart", u"Add Attribute", None))
        self.remove_attribute.setText(QCoreApplication.translate("DialogPart", u"Delete Attribute", None))
        self.set_image.setText(QCoreApplication.translate("DialogPart", u"Set Image", None))
        self.remove_image.setText(QCoreApplication.translate("DialogPart", u"Remove Image", None))
        self.add_document.setText(QCoreApplication.translate("DialogPart", u"Add Document", None))
        self.remove_document.setText(QCoreApplication.translate("DialogPart", u"Remove Document", None))
    # retranslateUi

