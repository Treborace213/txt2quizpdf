from dataclasses import dataclass
from enum import Enum, auto
from typing import List
from reportlab.platypus import Flowable

class SectionType(Enum):
    TITLE = auto()
    SUBTITLE = auto()
    PARAGRAPH = auto()
    QUESTION = auto()
    PAGEBREAK = auto()

@dataclass
class SectionItem:
    flowable: Flowable
    type: SectionType

class DocumentFlow:
    def __init__(self):
        self._items: List[SectionItem] = []

    def add(self, flowable: Flowable, section_type: SectionType):
        self._items.append(SectionItem(flowable, section_type))

    def get_flow(self):
        return [item.flowable for item in self._items]
        
    def get_last_added_type(self):
        if self._items:
            return self._items[-1].type
        return None