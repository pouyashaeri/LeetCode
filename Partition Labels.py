from typing import List

class Solution:
    # My Solution
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i, ch in enumerate(s):
            last_seen[ch] = i

        left = 0
        right = 0
        max_len = 0
        partitions = []
        for i, ch in enumerate(s):
            if last_seen[ch] >= right:
                right = last_seen[ch]

            max_len = max(max_len, right - left + 1)

            if i == right:
                partitions.append(max_len)
                left = i + 1
                right = i + 1
                max_len = 0

        return partitions
                
    # # Optimal Code:
    # def partitionLabels(self, s: str) -> List[int]:
    #     last = {}
    #     for i, ch in enumerate(s):
    #         last[ch] = i
            
    #     partitions = []
    #     start = 0
    #     end = 0
    #     for i, ch in enumerate(s):
    #         end = max(end, last[ch])
    #         if i == end:
    #             partitions.append(end - start + 1)
    #             start = i + 1

    #     return partitions