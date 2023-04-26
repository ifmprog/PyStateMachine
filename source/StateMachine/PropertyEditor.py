from PySide2.QtWidgets import QTreeView, QWidget, QAbstractItemView
from PySide2.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QDragEnterEvent,
    QDropEvent,
)
from PySide2.QtCore import QObject, Qt, QMimeData, QModelIndex


class PropertyEditorView(QTreeView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


class PropertyEditorModel(QStandardItemModel):
    def __init__(self, parent) -> None:
        super().__init__(parent)


class PropetyEditorItem(QStandardItem):
    ...


class PropertyEditor(QObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.__view: PropertyEditorView = None
        self.__model: PropertyEditorModel = None
        self.__initUI()

    def __initUI(self):
        self.__model = PropertyEditorModel(None)
        v = PropertyEditorView()
        v.setModel(self.__model)
        self.__view = v

    def getWidget(self) -> QWidget:
        return self.__view



