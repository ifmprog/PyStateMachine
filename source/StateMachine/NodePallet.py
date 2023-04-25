from PySide2.QtWidgets import QTreeView, QWidget
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import QObject, Qt


class NodePalletView(QTreeView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setDragEnabled(True)


class NodePalletModel(QStandardItemModel):
    def __init__(self, parent) -> None:
        super().__init__(parent)


class NodePalletItem(QStandardItem):
    ...


class NodePallet(QObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.__view: NodePalletView = None
        self.__model: NodePalletModel = None
        self.__initUI()

    def __initUI(self):
        self.__model = NodePalletModel(None)
        v = NodePalletView()
        v.setModel(self.__model)
        self.__view = v

    def getWidget(self) -> QWidget:
        return self.__view

    def setupByDummy(self):
        m: NodePalletModel = self.__model
        m.clear()
        m.setHorizontalHeaderLabels(["id"])
        rows = [
            [NodePalletItem("aaaa")],
            [NodePalletItem("bbbb")],
            [NodePalletItem("cccc")],
        ]
        for row in rows:
            for clmn in row:
                clmn.setEditable(False)
                clmn.setTextAlignment(Qt.AlignTop)
            m.appendRow(row)
