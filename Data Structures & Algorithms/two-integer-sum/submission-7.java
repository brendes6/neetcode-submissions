class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();
        int n = nums.length;

        for (int i=0; i<n; i++){
            int num = nums[i];
            int need = target - num;
            if (seen.containsKey(need)){
                int ind = seen.get(need);
                int[] a = {ind, i};
                return a;
            }

            seen.put(num, i);
        }

        int[] a = {-1, -1};
        return a;

        
    }
}
