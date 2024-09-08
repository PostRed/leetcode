class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.data = []

    def insert(self, val):
        if val in self.dict:
            return False
        self.data.append(val)
        self.dict[val] = len(self.data) - 1
        return True
        

    def remove(self, val):
        if val not in self.dict:
            return False
        last = self.data[-1]
        ind = self.dict[val]
        self.dict[last] = ind
        self.data[ind] = last
        self.data.pop()
        self.dict.pop(val)
        return True
        

    def getRandom(self):
        return random.choice(self.data)
