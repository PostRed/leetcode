class NestedIterator(object):
    def __init__(self, nestedList):
        self.list =[]
        self.fill(nestedList)
        self.list = self.list[::-1]

    def fill(self, nestedList):
        for elem in nestedList:
            if elem.isInteger():
                self.list.append(elem.getInteger())
            else:
                self.fill(elem.getList())

    def next(self):
        return self.list.pop()

    def hasNext(self):
        return len(self.list) > 0
