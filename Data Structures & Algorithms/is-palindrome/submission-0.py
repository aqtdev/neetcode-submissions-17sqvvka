class Solution:
    def isPalindrome(self, s: str) -> bool:
        # intialize empty list
        lst = []

        # iterate through given string
        for ch in s:

            # append each char to the new list
            if ch.isalnum():
                lst.append(ch.lower())

            # check if first value = to last value
        return lst == lst[::-1]


                
