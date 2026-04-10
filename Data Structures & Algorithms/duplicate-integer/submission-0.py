class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
            if countMap[num] > 1:
                return True
        return False