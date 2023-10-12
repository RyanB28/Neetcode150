# https://leetcode.com/problems/contains-duplicate/

# This function will check if the array contains all unique values
# This is done by using a dictonary, if the item is not in the dict add it, 
# Otherwise return True, because then it already has seen it.
def containsDuplicate(nums: List[int]) -> bool:
    x = {}
    for num in nums:
        if(x.get(num, False)):
            return True
        x[num] = True
    return False

# The unique structure of Sets is that all the elements are unique, 
# So by checking the length of the set with the length of the input array
# We can figure out if there are duplicate values. 
def containsDuplicateUsingSet(nums: List[int]) -> bool:
    return not (len(set(nums)) == len(nums))
