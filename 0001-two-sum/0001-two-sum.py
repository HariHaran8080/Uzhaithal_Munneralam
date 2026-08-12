class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            value=nums[i]
            difference=target-value
            if difference in d:
                return [d[difference],i]
            d[value]=i

        return []