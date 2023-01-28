from typing import List
import itertools

class Solution:
    def permute(nums: List[int]) -> List[List[int]]:

        permute = list(itertools.permutations(nums))

        print(permute)

nums = [1,2,3,8]
Solution.permute(nums)