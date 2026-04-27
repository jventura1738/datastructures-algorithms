class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int m = word.length(), n = abbr.length();
        int word_idx = 0;
        int abbr_idx = 0;

        while (word_idx < m && abbr_idx < n) {
            char w = word.charAt(word_idx);
            char a = abbr.charAt(abbr_idx);

            // no leading zeroes
            if (a == '0') {
                return false;
            }

            StringBuilder sb = new StringBuilder();
            while (abbr_idx < n && a >= '0' && a <= '9') {
                sb.append(a);    
                abbr_idx += 1;
                if (abbr_idx < n) {
                    a = abbr.charAt(abbr_idx);
                }
            }
            int jump = sb.length() == 0 ? 0 : Integer.parseInt(sb.toString());

            word_idx += jump;
            if (word_idx == m && abbr_idx == n) {
                break;
            }

            if (word_idx >= m) {
                return false;
            }

            w = word.charAt(word_idx);

            if (w != a) {
                return false;
            }
            word_idx++;
            abbr_idx++;
        }
        return true;
    }
}