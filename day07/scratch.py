''' simple composite pattern to represent a file system '''
from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    ''' base component class '''

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._file_size = value

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def get_size(self) -> int:
        pass


class File(Component):
    ''' "leaf" class '''

    def __init__(self, name: str, file_size: int = 0):
        self.name = name
        self.file_size = file_size

    def get_size(self) -> int:
        return self.file_size


class Directory:
    ''' "composite" class '''

    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.file_size = 0
        self.parent = self

    def add(self, component: Component):
        self.children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self.children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def get_size(self) -> int:
        self.file_size = 0
        for item in self.children:
            if isinstance(item, Directory):
                item.get_size()
            self.file_size += item.file_size
        return self.file_size


if __name__ == '__main__':
    # testing
    f1 = File('f1', 10000)
    f2 = File('f2', 150000)
    f3 = File('f3', 2000000)
    d = Directory('d')
    d2 = Directory('d2')
    d3 = Directory('d3')

    d.add(f1)
    d.add(f2)
    d.add(f3)
    d2.add(f1)
    d2.add(f2)
    d2.add(f3)
    d3.add(f1)
    d3.add(f2)
    d3.add(f3)
    d2.add(d3)
    d.add(d2)
