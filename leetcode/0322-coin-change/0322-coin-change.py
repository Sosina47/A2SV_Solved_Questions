class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(k):
            if k == 0: 
                return 0

            if k < 0: 
                return float("inf")

            if k in memo: 
                return memo[k]

            mn = float("inf")

            for c in coins: 
                val = dp(k - c) 
                mn = min(mn, val)

            memo[k] = mn + 1
            return memo[k]


        k = dp(amount) 
        return k if k != float("inf") else -1