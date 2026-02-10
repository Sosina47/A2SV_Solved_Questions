class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            c = []
            for i in str(n):
                c.append(int(i) ** 2)
            n = sum(c)
            if n in s:
                return False

            s.add(n)

        return True
