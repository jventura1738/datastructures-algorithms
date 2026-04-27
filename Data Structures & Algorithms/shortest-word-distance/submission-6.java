class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        int last_idx1 = -1;
        int last_idx2 = -1;
        int ans = wordsDict.length;

        for (int i = 0; i < wordsDict.length; i++) {
            String word = wordsDict[i];
            if (word.equals(word1)) {
                last_idx1 = i;
            }
            if (word.equals(word2)) {
                last_idx2 = i;
            }
            if (last_idx1 > -1 && last_idx2 > -1) {
                ans = Math.min(ans, Math.abs(last_idx1 - last_idx2));
            }
        }
        return ans;
    }
}
