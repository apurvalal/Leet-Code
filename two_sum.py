class Solution:
    def twoSum(self, nums: List[int], target: int):
        solution = {}
        for index,value in enumerate(nums):
            if (target - value) in solution:
                return [solution[target - value], index]
            else:
                solution[value] = index
