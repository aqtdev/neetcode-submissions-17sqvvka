class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # establish 2 dicts
        from collections import defaultdict
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        # traverse through s
        for letter in s:
            # adds 1 for the respective letter
            s_count[letter] += 1

        # traverse through t
        for letter in t:
            # adds 1 for the respective letter
            t_count[letter] += 1
        
        return s_count == t_count
        # if t_count == s_count:
            # return True