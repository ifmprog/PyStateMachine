from PySide2.QtWidgets import QTreeView, QWidget, QVBoxLayout
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import QObject, Qt
from StateMachine.NodeDefs import NodeType


class NodePalletView(QTreeView):
    """ノードパレットビュー"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setDragEnabled(True)


class NodePalletModel(QStandardItemModel):
    """ノードパレットモデル"""

    def __init__(self, parent) -> None:
        super().__init__(parent)


class NodePalletItem(QStandardItem):
    """ノードパレットアイテム"""

    @staticmethod
    def type2Name(type: NodeType) -> str:
        d = dict()
        d[NodeType.NONE] = "None"
        d[NodeType.SIMPLEX_STATE] = "SimplexState"
        d[NodeType.COMPLEX_STATE] = "ComplexState"
        d[NodeType.TRANS_COMMAND] = "TransitCommand"
        return d.get(type, "")

    def __init__(self, type: NodeType):
        super().__init__(NodePalletItem.type2Name(type))
        self.__nodeType: NodeType = type


class NodePallet(QObject):
    """ノードパレット"""

    def __init__(self) -> None:
        super().__init__(None)
        self.__widget: QWidget = None
        self.__stateView: NodePalletView = None
        self.__stateModel: NodePalletModel = None
        self.__commandView: NodePalletView = None
        self.__commandModel: NodePalletModel = None
        self.__initUI()

    def __initUI(self):
        self.__initStateViewModel()
        self.__initCommandViewMode()
        # レイアウト.
        layout = QVBoxLayout()
        layout.addWidget(self.__stateView, 1)
        layout.addWidget(self.__commandView, 1)
        layout.addStretch(100)
        self.__widget = QWidget()
        self.__widget.setLayout(layout)

    def __initStateViewModel(self):
        self.__stateModel = NodePalletModel(None)
        v = NodePalletView()
        v.setModel(self.__stateModel)
        v.setHeaderHidden(True)
        self.__stateView = v

    def __initCommandViewMode(self):
        self.__commandModel = NodePalletModel(None)
        v = NodePalletView()
        v.setModel(self.__commandModel)
        v.setHeaderHidden(True)
        self.__commandView = v

    def getWidget(self) -> QWidget:
        return self.__widget

    def setup(self):
        datum = [
            {
                "model": self.__stateModel,
                "items": [
                    [NodePalletItem(NodeType.SIMPLEX_STATE)],
                    [NodePalletItem(NodeType.COMPLEX_STATE)],
                ],
            },
            {
                "model": self.__commandModel,
                "items": [
                    [NodePalletItem(NodeType.TRANS_COMMAND)],
                ],
            },
        ]
        for data in datum:
            m = data["model"]
            m.clear()
            m.setHorizontalHeaderLabels(["id"])
            for items in data["items"]:
                for item in items:
                    item.setEditable(False)
                    item.setTextAlignment(Qt.AlignTop)
                m.appendRow(items)
