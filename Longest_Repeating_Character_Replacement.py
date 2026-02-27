class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_len = left = max_freq = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            if right - left + 1 - max_freq <= k:
                max_len = max(max_len, right - left + 1)
            
            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1 
                left += 1

        return max_len 
