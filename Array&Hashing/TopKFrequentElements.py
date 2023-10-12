# https://leetcode.com/problems/top-k-frequent-elements/

# Gives the k most frequent elements of the list 
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    resultDict = {}
    # Calculating which elements are the most common
    for i in nums:
        resultDict[i] = resultDict.get(i, 0) + 1
    # Sort based on the most common elements. 
    result = sorted(resultDict.items(), key=lambda x: x[1], reverse=True)
    # Return the k most elements
    return [x[0] for x in result[0:k]]