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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QSizePolicy, QSpacerItem, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from inventory.gui.widgets.parts import PartsWidget

class Ui_TabCategories(object):
    def setupUi(self, TabCategories):
        if not TabCategories.objectName():
            TabCategories.setObjectName(u"TabCategories")
        TabCategories.resize(870, 683)
        self.horizontalLayout_2 = QHBoxLayout(TabCategories)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.category_widget = QWidget(TabCategories)
        self.category_widget.setObjectName(u"category_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_widget.sizePolicy().hasHeightForWidth())
        self.category_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.category_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbox = QWidget(self.category_widget)
        self.toolbox.setObjectName(u"toolbox")
        self.horizontalLayout = QHBoxLayout(self.toolbox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.insert_sibling = QToolButton(self.toolbox)
        self.insert_sibling.setObjectName(u"insert_sibling")

        self.horizontalLayout.addWidget(self.insert_sibling)

        self.insert_child = QToolButton(self.toolbox)
        self.insert_child.setObjectName(u"insert_child")

        self.horizontalLayout.addWidget(self.insert_child)

        self.line = QFrame(self.toolbox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.delete_category = QToolButton(self.toolbox)
        self.delete_category.setObjectName(u"delete_category")

        self.horizontalLayout.addWidget(self.delete_category)

        self.line_2 = QFrame(self.toolbox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.make_sibling = QToolButton(self.toolbox)
        self.make_sibling.setObjectName(u"make_sibling")

        self.horizontalLayout.addWidget(self.make_sibling)

        self.make_child = QToolButton(self.toolbox)
        self.make_child.setObjectName(u"make_child")

        self.horizontalLayout.addWidget(self.make_child)

        self.line_3 = QFrame(self.toolbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.collapse_all = QToolButton(self.toolbox)
        self.collapse_all.setObjectName(u"collapse_all")

        self.horizontalLayout.addWidget(self.collapse_all)

        self.expand_all = QToolButton(self.toolbox)
        self.expand_all.setObjectName(u"expand_all")

        self.horizontalLayout.addWidget(self.expand_all)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.toolbox)

        self.categories = QTreeWidget(self.category_widget)
        self.categories.setObjectName(u"categories")
        self.categories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.categories.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.categories.setIndentation(12)
        self.categories.setExpandsOnDoubleClick(False)

        self.verticalLayout.addWidget(self.categories)


        self.horizontalLayout_2.addWidget(self.category_widget)

        self.parts = PartsWidget(TabCategories)
        self.parts.setObjectName(u"parts")
        sizePolicy.setHeightForWidth(self.parts.sizePolicy().hasHeightForWidth())
        self.parts.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.parts)


        self.retranslateUi(TabCategories)

        QMetaObject.connectSlotsByName(TabCategories)
    # setupUi

    def retranslateUi(self, TabCategories):
        TabCategories.setWindowTitle(QCoreApplication.translate("TabCategories", u"Form", None))
#if QT_CONFIG(tooltip)
        self.insert_sibling.setToolTip(QCoreApplication.translate("TabCategories", u"Insert sibling", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.insert_child.setToolTip(QCoreApplication.translate("TabCategories", u"Insert child", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.delete_category.setToolTip(QCoreApplication.translate("TabCategories", u"Delete category", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.make_sibling.setToolTip(QCoreApplication.translate("TabCategories", u"Make selected a sibling", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.make_child.setToolTip(QCoreApplication.translate("TabCategories", u"Make selected a child of first selected category", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.collapse_all.setToolTip(QCoreApplication.translate("TabCategories", u"Collapse all", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.expand_all.setToolTip(QCoreApplication.translate("TabCategories", u"Expand all", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.categories.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("TabCategories", u"Parts", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("TabCategories", u"Designator", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("TabCategories", u"Title", None));
    # retranslateUi

