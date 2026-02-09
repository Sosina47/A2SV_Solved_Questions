import random

class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        
        return False
        

    def getRandom(self) -> int:
        num = random.choice(list(self.s))
        return num
        
