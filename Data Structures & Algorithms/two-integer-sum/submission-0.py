class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            # ex. 7 - 3 = 4
            difference = target - num
            # if 4 in seen (which it is)
            if difference in seen:
                # return seen[4], i --> gets index of value 4
                return [seen[difference], i]
            # seen[]
            seen[num] = i


            
                
            
                
