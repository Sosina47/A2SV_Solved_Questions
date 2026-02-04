#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        a_counter = Counter(a)
        b_counter = Counter(b)
        
        n = len(b_counter)
        if n > len(a_counter):
            return False
            
        for key, value in b_counter.items():
            if key not in a_counter or a_counter[key] < value:
                return False
        
        return True
