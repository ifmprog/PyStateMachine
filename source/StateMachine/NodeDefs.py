from enum import Enum, auto


class NodeType(Enum):
    NONE = auto()
    SIMPLEX_STATE = auto()
    COMPLEX_STATE = auto()
    TRANS_COMMAND = auto()
