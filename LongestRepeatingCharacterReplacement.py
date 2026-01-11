class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        left = 0
        max_len = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            length = right - left + 1
            while length - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                length = right - left + 1
            if length - max_freq <= k:
                max_len = max(max_len, length)
        return max_len