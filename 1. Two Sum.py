class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        for n in range(len(nums)):
            for o in range(n+1, len(nums)):
                if nums[n] + nums[o] == target:
                    return [n,o]