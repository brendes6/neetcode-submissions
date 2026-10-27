class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer> numSet = new HashSet<>();

        // populate numSet with the numbers in nums
        for (int i=0; i<nums.length; i++){
            numSet.add(nums[i]);
        }

        int result = 0;
        // if we find a num where num-1 not in numSet, remove and increment
        for (int i=0; i<nums.length; i++){
            if (!numSet.contains(nums[i] - 1)){
                int cur = nums[i];
                int res = 0;

                while (numSet.contains(cur)){
                    res++;
                    cur++;
                }

                if (res > result){
                    result = res;
                }
            }
        }

        return result;
    }
}
