from PySide2.QtWidgets import QTreeView, QWidget, QAbstractItemView
from PySide2.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QDragEnterEvent,
    QDropEvent,
)
from PySide2.QtCore import QObject, Qt, QMimeData, QModelIndex, Signal, QItemSelection


class StateTreeView(QTreeView):
    """
    ステートツリー.
    """

    def __init__(self, parent=None) -> None:
        """コンストラクタ"""
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        return super().dragEnterEvent(event)
        # if event.mimeData().hasText():
        #     event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        parent = self.indexAt(event.pos())
        if parent and parent.isValid():
            self.expand(parent)
        return super().dropEvent(event)
        # item = event.source().itemAt(event.pos())
        # if item:
        #    ...


class StateTreeModel(QStandardItemModel):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def dropMimeData(
        self,
        data: QMimeData,
        action: Qt.DropAction,
        row: int,
        column: int,
        parent: QModelIndex,
    ) -> bool:
        return super().dropMimeData(data, action, row, column, parent)


class StateTreeItem(QStandardItem):
    ...


class StateTree(QObject):
    onItemSelected = Signal()

    def __init__(self) -> None:
        super().__init__(None)
        self.__view: StateTreeView = None
        self.__model: StateTreeModel = None
        self.__initUI()

    def __initUI(self):
        self.__model = StateTreeModel(None)
        v = StateTreeView()
        v.setModel(self.__model)
        v.selectionModel().currentChanged.connect(self.__onChangeCurrent)
        self.__view = v

    def getWidget(self) -> QWidget:
        return self.__view

    def setupByDummy(self):
        m: StateTreeModel = self.__model
        m.clear()
        m.setHorizontalHeaderLabels(["id"])
        row = [StateTreeItem("a")]
        for clmn in row:
            clmn.setEditable(False)
            clmn.setTextAlignment(Qt.AlignTop)
        m.appendRow(row)

    def __onChangeCurrent(self, current: QModelIndex, previous: QModelIndex):
        item = self.__model.itemFromIndex(current)
        if item:
            print(item.text())
