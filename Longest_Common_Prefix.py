class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        while True:
            for i in range(1, len(strs)):
                if not prefix:
                    return ""
                
                if not strs[i].startswith(prefix):
                    prefix = prefix[:-1]
                    break
            else:
                return prefix
