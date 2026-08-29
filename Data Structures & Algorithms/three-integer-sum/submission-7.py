class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        # 3sum - just do two sum 2 for each val other than one we are on
        # Prevent repeats via skipping adjacent vals that are equal

        nums = sorted(nums)
        ans = []
        print(nums)

        for i, num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while (l<r):
                cur = nums[l] + nums[r]
                if cur == -num:
                    ans.append([nums[l], nums[r], num])
                    l += 1
                    while l < r and nums[l] + nums[r] == -num:
                        l += 1
                elif cur < -num:
                    l += 1
                else:
                    r -= 1
        
        return ans
                
