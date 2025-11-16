from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ex_in: [1,5,3,1,2,3,2,2,3,4,6,6,6], k = 3
        # ex_out: [6,3,2]
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        top_k = []
        for _ in range(k):
            key_max = max(counts, key=counts.get)
            max_value = counts.pop(key_max)
            top_k.append(key_max)
        return top_k