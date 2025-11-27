from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10, position = [1,4], speed = [3,2]
        # 1 -> 4 -> 7 -> 10
        # 4 -> 6 -> 8 -> 10
        # fleets = [[1, 4]]

        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # 4 -> 6 -> 8 -> 10
        # 1 -> 3 -> 5 -> 7
        # 0 -> 1 -> 2 -> 3
        # 7 -> 8 -> 9 -> 10
        # fleets = [[4, 7], [1], [0]]
        
        cars = sorted(zip(position, speed), reverse = True)
        # print(cars)

        fleets = 0
        last_time = 0

        # [(7, 1), (4, 2), (1, 2), (0, 1)]
        for pos, spd in cars:
            time = (target - pos) / spd # 3
            if time > last_time:
                last_time = time # 3
                fleets += 1 # 1
            
        return fleets
