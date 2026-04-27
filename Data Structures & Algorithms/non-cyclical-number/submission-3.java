class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<Integer>();

        while (n != 1) {
            String number = String.valueOf(n);
            int new_n = 0;
            for (char c : number.toCharArray()) {
                int digit = c - '0';
                new_n += digit * digit;
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
