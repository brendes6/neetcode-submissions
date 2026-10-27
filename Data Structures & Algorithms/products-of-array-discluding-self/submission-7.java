class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] ans = new int[n];

        int prefix_1 = 1;

        for (int i=0; i<n; i++){
            ans[i] = prefix_1;
            prefix_1 *= nums[i];
        }

        int prefix_2 = 1;

        for (int i = n-1; i>=0; i--){
            ans[i] *= prefix_2;
            prefix_2 *= nums[i];
        }

        return ans;
        
    }
}  
