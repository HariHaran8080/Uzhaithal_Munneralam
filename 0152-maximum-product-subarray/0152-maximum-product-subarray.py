class Solution:
    def maxProduct(self, nums: List[int]) -> int:
                current_max=nums[0]
                current_min=nums[0]
                ans=nums[0]

                for i in range(1,len(nums)):
                    temp_max=current_max
                    temp_min=current_min
                    current_max=max(
                        nums[i],
                        temp_max*nums[i],
                        temp_min*nums[i]
                    )
                    current_min=min(nums[i],
                    temp_max*nums[i],
                    temp_min*nums[i])
                    ans=max(ans,current_max)
                return ans