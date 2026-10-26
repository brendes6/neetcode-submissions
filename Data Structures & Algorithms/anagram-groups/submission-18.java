class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> to_lst = new HashMap<>();

        for (int i=0; i<strs.length; i++){

            String cur = strs[i];

            char[] asArr = cur.toCharArray();

            Arrays.sort(asArr);

            String newStr = new String(asArr);

            to_lst.computeIfAbsent(newStr, k -> new ArrayList<>()).add(cur);

        }

        return new ArrayList<>(to_lst.values());
        
    }
}
