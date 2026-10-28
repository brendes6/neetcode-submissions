class Solution {

    private int eat(int[] piles, int k){

        int num_hours = 0;

        for (int ban : piles){
            num_hours += Math.ceilDiv(ban, k);
        }

        return num_hours;
    }

    public int minEatingSpeed(int[] piles, int h) {

        int l = 1;
        int r = Arrays.stream(piles).max().getAsInt();

        while (l<r){

            int m = l + (r - l) / 2;

            int res = eat(piles, m);

            if (res > h){
                l = m + 1;
            }
            else {
                r = m;
            }
        }

        return l;
        
    }
}
