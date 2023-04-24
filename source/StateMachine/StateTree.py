from PySide2.QtWidgets import QTreeView, QWidget
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import QObject, Qt


class StateTreeView(QTreeView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)


class StateTreeModel(QStandardItemModel):
    def __init__(self, parent) -> None:
        super().__init__(parent)


class StateTreeItem(QStandardItem):
    ...


class StateTree(QObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.__view: StateTreeView = None
        self.__model: StateTreeModel = None
        self.__initUI()

    def __initUI(self):
        self.__model = StateTreeModel(None)
        v = StateTreeView()
        v.setModel(self.__model)
        self.__view = v

    def getWidget(self) -> QWidget:
        return self.__view

    def setupByDummy(self):
        m: StateTreeModel = self.__model
        m.clear()
        m.setHorizontalHeaderLabels(["id", "aaa"])
        row = [StateTreeItem("a"), StateTreeItem("b")]
        for clmn in row:
            clmn.setEditable(False)
            clmn.setTextAlignment(Qt.AlignTop)
        m.appendRow(row)
