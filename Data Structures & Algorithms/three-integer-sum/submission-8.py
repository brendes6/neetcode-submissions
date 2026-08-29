class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Threesum: the way to do this is by doing two sum II (sorted array) FOR 
        each value in the array. Thus, it is O(n^2) which is good enough for us. 
        We first sort the array, and for each val we do two sum II on the values
        to the right of it. To avoid duplicates, like many other implementations,
        we simply skip any values we reach that are the same as the one befor it.

        """

        ans = []
        nums.sort()

        for i in range(len(nums)):
            # avoid duplicates by skipping vals w num before ==
            if i > 0 and nums[i]==nums[i-1]:
                continue

            target = -nums[i]

            l, r = i+1, len(nums)-1

            while l<r:
                s = nums[l] + nums[r]
                if s==target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            
        
        return ans

