from typing import Any, Optional


class Node:
    def __init__(self, data: Any = 0):
        self.data: Any = data
        self.ref: Optional[Node] = None
