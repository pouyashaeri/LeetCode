from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        current_dists = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if i + 1 < len(temperatures):
                right_index = i + 1
                while t >= temperatures[right_index]:
                    if right_index + 1 < len(temperatures):
                        right_index = right_index + 1 
                    else:
                        break
                if t < temperatures[right_index] and right_index < len(temperatures):
                    current_dists[i] = right_index - i
            # print(f"current_dists: {current_dists}")
        
        return current_dists