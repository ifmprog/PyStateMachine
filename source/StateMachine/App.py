from PySide2.QtCore import QObject, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget
from StateMachine.NodePallet import NodePallet
from StateMachine.StateTree import StateTree
from StateMachine.PropertyEditor import PropertyEditor
from StateMachine.PropertyDefs import SimpleState


class App(QObject):
    def __init__(self) -> None:
        super().__init__(None)
        self.__app = None
        self.__wnd: QMainWindow = None
        self.__nodePallet: NodePallet = None
        self.__stateTree: StateTree = None
        self.__propertyEditor: PropertyEditor = None

    def run(self) -> int:
        print("app begun")
        self.__app = QApplication()
        self.__wnd = QMainWindow()
        self.__setupObjects()
        self.__layoutObjects()
        self.__wnd.show()
        ret = self.__app.exec_()
        print("app shutdown({})".format(ret))
        return ret

    def __setupObjects(self):
        self.__nodePallet = NodePallet()
        self.__nodePallet.setup()
        self.__stateTree = StateTree()
        self.__stateTree.setupByDummy()
        self.__stateTree.onItemSelected.connect(self.__slotStateTreeOnItemSelected)
        self.__propertyEditor = PropertyEditor()
        wnd = self.__wnd
        wnd.__c = QTextEdit(wnd)
        wnd.__l = QDockWidget("Left", wnd)
        wnd.__r = QDockWidget("Right", wnd)
        wnd.__t = QDockWidget("Top", wnd)
        wnd.__b = QDockWidget("Bottom", wnd)

    def __layoutObjects(self):
        wnd = self.__wnd
        wnd.setCentralWidget(self.__stateTree.getWidget())
        wnd.addDockWidget(Qt.LeftDockWidgetArea, wnd.__l)
        wnd.addDockWidget(Qt.RightDockWidgetArea, wnd.__r)
        wnd.addDockWidget(Qt.TopDockWidgetArea, wnd.__t)
        wnd.addDockWidget(Qt.BottomDockWidgetArea, wnd.__b)
        wnd.__l.setWidget(self.__nodePallet.getWidget())
        wnd.__r.setWidget(self.__propertyEditor.getWidget())
        wnd.setWindowTitle("State Machine")
        wnd.statusBar()

    def __slotStateTreeOnItemSelected(self, state: SimpleState):
        self.__propertyEditor.setSimpleState(state)
