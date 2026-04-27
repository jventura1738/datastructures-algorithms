class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<Integer>();

        while (n != 1) {
            String number = String.valueOf(n);
            int new_n = 0;
            for (char c : number.toCharArray()) {
                new_n += Math.pow(Integer.parseInt(String.valueOf(c)), 2);
            }
            n = new_n;
            if (seen.contains(n)) {
                return false;
            }
            seen.add(new_n);
        }
        return true;
    }
}
