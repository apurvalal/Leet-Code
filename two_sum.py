class Solution:
    def twoSum(self, nums: List[int], target: int):
        solution = {}
        for index in range(len(nums)):
            solution[index] = nums[index]

        for index in range(len(nums)):
            if (target - nums[index]) in solution.values():
                for key, value in solution.items():
                    if value == (target - nums[index]) and key!=index:
                        required_value = key
                        return [index, key]
