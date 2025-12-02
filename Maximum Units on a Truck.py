class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:-x[1]) # sort by units descending

        total_units = 0

        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            take = min(boxes, truckSize)
            total_units += take * units
            truckSize -= take

        return total_units
        