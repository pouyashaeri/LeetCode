from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for today in range(len(temperatures)):
            today_temp = temperatures[today]

            while stack and today_temp > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = today - previous_day
            
            stack.append(today)
        
        return result