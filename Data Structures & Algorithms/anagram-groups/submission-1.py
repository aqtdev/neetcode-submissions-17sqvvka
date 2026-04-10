class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words = defaultdict(list)

        # iterates through each string
        for s in strs:
            # array of 26 0's
            count = [0] * 26
            # iterates through each char
            for ch in s:
                # goes to count index and adds 1 to it
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            words[key].append(s)
        # returns the list of groups
        return list(words.values())
