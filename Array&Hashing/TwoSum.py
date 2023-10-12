# https://leetcode.com/problems/two-sum/


# Gives the indexes of 2 items in the list as the result of the target. 
# This uses a dictionary with the remainder as key and the index as value. 
# Whenever we get a hit on the dictonary we have found the combi.
def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultDict = {}
        for i in range(len(nums)):
            finder = target - nums[i]
            indexfound = resultDict.get(finder, -1)
            if indexfound != -1:
                return [i, indexfound]
            resultDict[nums[i]] = i
        return [-1]
