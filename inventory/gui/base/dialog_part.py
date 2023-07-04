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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QGraphicsView, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from inventory.gui.widgets.attributes import AttributesWidget
from inventory.gui.widgets.location import LocationWidget

class Ui_DialogPart(object):
    def setupUi(self, DialogPart):
        if not DialogPart.objectName():
            DialogPart.setObjectName(u"DialogPart")
        DialogPart.resize(1091, 650)
        self.horizontalLayout_7 = QHBoxLayout(DialogPart)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.left = QWidget(DialogPart)
        self.left.setObjectName(u"left")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.left)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top = QWidget(self.left)
        self.top.setObjectName(u"top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.properties_widget = QWidget(self.top)
        self.properties_widget.setObjectName(u"properties_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.properties_widget.sizePolicy().hasHeightForWidth())
        self.properties_widget.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.properties_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, -1, 0)
        self.lbl_category = QLabel(self.properties_widget)
        self.lbl_category.setObjectName(u"lbl_category")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_category)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category = QComboBox(self.properties_widget)
        self.category.setObjectName(u"category")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.category)

        self.new_category = QPushButton(self.properties_widget)
        self.new_category.setObjectName(u"new_category")

        self.horizontalLayout.addWidget(self.new_category)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.lbl_value = QLabel(self.properties_widget)
        self.lbl_value.setObjectName(u"lbl_value")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_value)

        self.lbl_number = QLabel(self.properties_widget)
        self.lbl_number.setObjectName(u"lbl_number")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_number)

        self.lbl_package = QLabel(self.properties_widget)
        self.lbl_package.setObjectName(u"lbl_package")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_package)

        self.lbl_price = QLabel(self.properties_widget)
        self.lbl_price.setObjectName(u"lbl_price")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_price)

        self.lbl_weight = QLabel(self.properties_widget)
        self.lbl_weight.setObjectName(u"lbl_weight")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_weight)

        self.value = QLineEdit(self.properties_widget)
        self.value.setObjectName(u"value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.value)

        self.part_number = QLineEdit(self.properties_widget)
        self.part_number.setObjectName(u"part_number")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.part_number)

        self.footprint = QLineEdit(self.properties_widget)
        self.footprint.setObjectName(u"footprint")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.footprint)

        self.price = QDoubleSpinBox(self.properties_widget)
        self.price.setObjectName(u"price")
        self.price.setProperty("showGroupSeparator", True)
        self.price.setDecimals(3)
        self.price.setMaximum(10000.000000000000000)
        self.price.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.price)

        self.lbl_reorder = QLabel(self.properties_widget)
        self.lbl_reorder.setObjectName(u"lbl_reorder")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_reorder)

        self.threshold = QSpinBox(self.properties_widget)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMaximum(100000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.threshold)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.weight = QDoubleSpinBox(self.properties_widget)
        self.weight.setObjectName(u"weight")
        self.weight.setDecimals(3)
        self.weight.setMaximum(1000000.000000000000000)

        self.horizontalLayout_5.addWidget(self.weight)

        self.calibrate = QPushButton(self.properties_widget)
        self.calibrate.setObjectName(u"calibrate")

        self.horizontalLayout_5.addWidget(self.calibrate)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.notes = QPlainTextEdit(self.properties_widget)
        self.notes.setObjectName(u"notes")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.notes)

        self.lbl_notes = QLabel(self.properties_widget)
        self.lbl_notes.setObjectName(u"lbl_notes")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_notes)


        self.horizontalLayout_2.addWidget(self.properties_widget)

        self.attributes = AttributesWidget(self.top)
        self.attributes.setObjectName(u"attributes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.attributes.sizePolicy().hasHeightForWidth())
        self.attributes.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.attributes)


        self.verticalLayout_5.addWidget(self.top)

        self.locations = LocationWidget(self.left)
        self.locations.setObjectName(u"locations")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.locations.sizePolicy().hasHeightForWidth())
        self.locations.setSizePolicy(sizePolicy5)

        self.verticalLayout_5.addWidget(self.locations)

        self.suppliers = QTableWidget(self.left)
        if (self.suppliers.columnCount() < 2):
            self.suppliers.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.suppliers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.suppliers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.suppliers.setObjectName(u"suppliers")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.suppliers.sizePolicy().hasHeightForWidth())
        self.suppliers.setSizePolicy(sizePolicy6)
        self.suppliers.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.suppliers.horizontalHeader().setStretchLastSection(True)
        self.suppliers.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.suppliers)


        self.horizontalLayout_7.addWidget(self.left)

        self.right = QWidget(DialogPart)
        self.right.setObjectName(u"right")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy7)
        self.verticalLayout_4 = QVBoxLayout(self.right)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.image_widget = QWidget(self.right)
        self.image_widget.setObjectName(u"image_widget")
        self.verticalLayout_3 = QVBoxLayout(self.image_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.image = QGraphicsView(self.image_widget)
        self.image.setObjectName(u"image")

        self.verticalLayout_3.addWidget(self.image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.set_image = QPushButton(self.image_widget)
        self.set_image.setObjectName(u"set_image")

        self.horizontalLayout_3.addWidget(self.set_image)

        self.remove_image = QPushButton(self.image_widget)
        self.remove_image.setObjectName(u"remove_image")
        self.remove_image.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.remove_image)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.image_widget)

        self.document_widget = QWidget(self.right)
        self.document_widget.setObjectName(u"document_widget")
        self.verticalLayout = QVBoxLayout(self.document_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.documents = QListWidget(self.document_widget)
        self.documents.setObjectName(u"documents")
        self.documents.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.documents.sizePolicy().hasHeightForWidth())
        self.documents.setSizePolicy(sizePolicy8)

        self.verticalLayout.addWidget(self.documents)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add_document = QPushButton(self.document_widget)
        self.add_document.setObjectName(u"add_document")

        self.horizontalLayout_4.addWidget(self.add_document)

        self.remove_document = QPushButton(self.document_widget)
        self.remove_document.setObjectName(u"remove_document")

        self.horizontalLayout_4.addWidget(self.remove_document)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.document_widget)

        self.buttonBox = QDialogButtonBox(self.right)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout_4.addWidget(self.buttonBox)


        self.horizontalLayout_7.addWidget(self.right)


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
        self.lbl_notes.setText(QCoreApplication.translate("DialogPart", u"Notes:", None))
        ___qtablewidgetitem = self.suppliers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogPart", u"Supplier", None));
        ___qtablewidgetitem1 = self.suppliers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogPart", u"Part Number", None));
        self.set_image.setText(QCoreApplication.translate("DialogPart", u"Set Image", None))
        self.remove_image.setText(QCoreApplication.translate("DialogPart", u"Remove Image", None))
        self.add_document.setText(QCoreApplication.translate("DialogPart", u"Add Document", None))
        self.remove_document.setText(QCoreApplication.translate("DialogPart", u"Remove Document", None))
    # retranslateUi

