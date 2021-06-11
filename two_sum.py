class Solution:
    def twoSum(self, target: int):
        nums = []
        solution = []
        for index_start in range(len(nums)):
            for index_next in range(index_start + 1, len(nums)):
                if nums[index_start] + nums[index_next] == target:
                    solution.append(index_start)
                    solution.append(index_next)
                    return solution
