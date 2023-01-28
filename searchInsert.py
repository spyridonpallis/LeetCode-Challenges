from typing import List

class Solution:
    def searchInsert(nums: List[int], target: int) -> int:


        print(nums, target)

        nums.append(target)
        nums.sort()

        print(nums)


        for i in range(0, len(nums)):
            #print(nums[i])
            if nums[i] == target:
                print(i)
                break

        print(nums)

nums = [1, 2, 2, 2, 3, 5, 7]
target = 8

Solution.searchInsert(nums, target)