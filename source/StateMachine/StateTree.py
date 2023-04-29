from PySide2.QtWidgets import QTreeView, QWidget, QAbstractItemView
from PySide2.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QDragEnterEvent,
    QDropEvent,
)
from PySide2.QtCore import QObject, Qt, QMimeData, QModelIndex, Signal, QItemSelection
from StateMachine.PropertyDefs import SimpleState


class StateTreeView(QTreeView):
    """ステートツリービュー"""

    def __init__(self, parent=None) -> None:
        """コンストラクタ"""
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        return super().dragEnterEvent(event)

    def dropEvent(self, event: QDropEvent) -> None:
        parent = self.indexAt(event.pos())
        if parent and parent.isValid():
            self.expand(parent)
        return super().dropEvent(event)


class StateTreeModel(QStandardItemModel):
    """ステートツリーモデル"""

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
    """ステートツリーアイテム"""

    def __init__(self, text: str):
        super().__init__(text)
        self.setEditable(False)
        self.setTextAlignment(Qt.AlignTop)


class StateTree(QObject):
    """ステートツリー"""

    """アイテムが選択されたときに発火"""
    onItemSelected = Signal(SimpleState)

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
        m.appendRow([StateTreeItem("a")])

    def __onChangeCurrent(self, current: QModelIndex, previous: QModelIndex):
        item = self.__model.itemFromIndex(current)
        if item:
            state = SimpleState(item.text())
            self.onItemSelected.emit(state)
