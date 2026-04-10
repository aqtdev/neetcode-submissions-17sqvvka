class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        result = sorted_nums[:k]
        return result

        

            
            
