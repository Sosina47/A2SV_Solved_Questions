from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        a_counter = Counter(a)
        b_counter = Counter(b)

        n = len(a_counter)
        if n != len(b_counter):
            return False
        
        for key, value in a_counter.items():
            if b_counter[key] != value:
                return False

        return True
