class Solution {
    int[] w;
    int total;
    
    public Solution(int[] w) {
        this.w = w;
        for (int weight : this.w) {
            this.total += weight;
        }
    }

    public int pickIndex() {
        double target = total * Math.random();
        int cumulative = 0;
        for (int i = 0; i < this.w.length; i++) {
            cumulative += w[i];
            if (cumulative > target) {
                return i;
            }
        }
        return -1;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */