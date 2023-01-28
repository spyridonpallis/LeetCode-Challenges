from typing import List

class Solution:
    def lengthOfLastWord(s: str) -> int:

        split_s = s.split()

        print(len(split_s[-1]))


s = 'fun fun'
Solution.lengthOfLastWord(s)