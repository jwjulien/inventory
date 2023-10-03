# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_projects.ui'
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
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from inventory.gui.widgets.projects import ProjectsWidget
from inventory.gui.widgets.revisions import RevisionsWidget

class Ui_TabProjects(object):
    def setupUi(self, TabProjects):
        if not TabProjects.objectName():
            TabProjects.setObjectName(u"TabProjects")
        TabProjects.resize(825, 596)
        self.verticalLayout_2 = QVBoxLayout(TabProjects)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stack = QStackedWidget(TabProjects)
        self.stack.setObjectName(u"stack")
        self.page_projects = QWidget()
        self.page_projects.setObjectName(u"page_projects")
        self.horizontalLayout = QHBoxLayout(self.page_projects)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.projects = ProjectsWidget(self.page_projects)
        self.projects.setObjectName(u"projects")

        self.horizontalLayout.addWidget(self.projects)

        self.revisions = RevisionsWidget(self.page_projects)
        self.revisions.setObjectName(u"revisions")

        self.horizontalLayout.addWidget(self.revisions)

        self.stack.addWidget(self.page_projects)
        self.page_parts = QWidget()
        self.page_parts.setObjectName(u"page_parts")
        self.verticalLayout = QVBoxLayout(self.page_parts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbar = QWidget(self.page_parts)
        self.toolbar.setObjectName(u"toolbar")
        self.horizontalLayout_2 = QHBoxLayout(self.toolbar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.back = QPushButton(self.toolbar)
        self.back.setObjectName(u"back")

        self.horizontalLayout_2.addWidget(self.back)

        self.title = QLabel(self.toolbar)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title)

        self.remove_material = QPushButton(self.toolbar)
        self.remove_material.setObjectName(u"remove_material")
        self.remove_material.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.remove_material)

        self.add_material = QPushButton(self.toolbar)
        self.add_material.setObjectName(u"add_material")

        self.horizontalLayout_2.addWidget(self.add_material)


        self.verticalLayout.addWidget(self.toolbar)

        self.materials = QTableWidget(self.page_parts)
        if (self.materials.columnCount() < 4):
            self.materials.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.materials.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.materials.setObjectName(u"materials")
        self.materials.setAlternatingRowColors(True)
        self.materials.setSelectionMode(QAbstractItemView.SingleSelection)
        self.materials.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.materials.horizontalHeader().setDefaultSectionSize(200)
        self.materials.horizontalHeader().setStretchLastSection(True)
        self.materials.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.materials)

        self.stack.addWidget(self.page_parts)

        self.verticalLayout_2.addWidget(self.stack)


        self.retranslateUi(TabProjects)

        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TabProjects)
    # setupUi

    def retranslateUi(self, TabProjects):
        TabProjects.setWindowTitle(QCoreApplication.translate("TabProjects", u"Form", None))
        self.back.setText(QCoreApplication.translate("TabProjects", u"Select Project", None))
        self.title.setText(QCoreApplication.translate("TabProjects", u"Project Title", None))
        self.remove_material.setText(QCoreApplication.translate("TabProjects", u"Remove Line Item", None))
        self.add_material.setText(QCoreApplication.translate("TabProjects", u"Add Line Item", None))
        ___qtablewidgetitem = self.materials.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TabProjects", u"Designator", None));
        ___qtablewidgetitem1 = self.materials.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TabProjects", u"Description", None));
        ___qtablewidgetitem2 = self.materials.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TabProjects", u"Part Number", None));
        ___qtablewidgetitem3 = self.materials.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TabProjects", u"Price", None));
    # retranslateUi

