''' represent filesystem with objects '''


class File():

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}, {self.size}'


class Directory():

    def __init__(self, name, size=0):
        self.size = size
        self.name = name
        self.contents = {}

    def add_items(self, *new_items):
        for item in new_items:
            self.contents[item.name] = item
            self.size += item.size

    def recalculate_size(self):
        new_size = 0
        for item in self.contents:
            if isinstance(self.contents[item], Directory):
                self.contents[item].recalculate_size()
            print(f'recalculating: {self.contents[item]}')
            new_size += self.contents[item].size
        self.size = new_size

    def __repr__(self):
        return f'{self.contents}, {self.size}'


if __name__ == '__main__':
    print("test data populated")
    d = Directory('d', 0)
    f1 = File('f1', 101)
    f2 = File('f2', 200)
    f3 = File('test', 48)
    d.add_items(f1, f2, f3)
    d2 = Directory('d2', 0)
    d2.add_items(f1, f3)
    d.add_items(d2)
    #d3 = Directory('d/d2/d3')
    #d2.add_items(d3)
