#from __future__ import annotations
#from abc import ABC, abstractmethod
#from typing import List

class Test:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Howdy, {self.name}!")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._age = value

#class Component:
#    pass

class File:
    def __init__(self, name, file_size = 0):
        self.name = name
        self.file_size = file_size

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
    def file_size(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._file_size = value

    def is_composite(self):
        return False

    def operation(self) -> int:
        return self.file_size


class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.file_size = 0
        self.parent = self

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
    def file_size(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._file_size = value
    
    def add(self, component):
        self.children.append(component)
        component.parent = self

    def remove(self, component):
        self.children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self) -> int:
        self.file_size = 0
        for item in self.children:
            if isinstance(item,Directory):
                item.operation()
            self.file_size += item.file_size
        return self.file_size

    def special_operation(self):
        output = []
        for item in self.children:
            if isinstance(item, Directory):
                print((item.name,item.file_size))
                item.special_operation()
                #item.special_operation()
                #if item.file_size >= 100000:
                    #output.append((item.file_size,item.special_operation()))
        #return output

if __name__ == '__main__':
    # test it out
    person = Test('matt')
    person.greeting()

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
