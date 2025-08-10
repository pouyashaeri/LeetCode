class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # # Strategy 1
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i!=j and numbers[i] + numbers[j] == target:
        #             results.append(i+1)
        #             results.append(j+1)
        #             return results

        # # Strategy 2
        j = len(numbers) - 1
    
        for i in range(len(numbers)):
            while i < j and numbers[i] + numbers[j] > target:
                j -= 1
            if i < j and numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

                if j < len(numbers) - 1:
                    j += 1

        # # Strategy 3
        # i = 0 
        # j = len(numbers) - 1

        # while i < j:
        #     if numbers[i] + numbers[j] < target:
        #         i+=1
        #     if numbers[i] + numbers[j] > target:
        #         j-=1
        #     if numbers[i] + numbers[j] == target:
        #         return [i+1,j+1]
