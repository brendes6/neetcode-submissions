class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> cur = new HashSet<>();

        int l = 0;
        int r = 0;
        int n = s.length();
        int result = 0;
        
        while (r < n){
            while (cur.contains(s.charAt(r))){
                cur.remove(s.charAt(l));
                l++;
            }

            cur.add(s.charAt(r));

            if (r-l + 1 > result){
                result = r-l + 1;
            }
            r++;

        }

        return result;
        
    }
}
