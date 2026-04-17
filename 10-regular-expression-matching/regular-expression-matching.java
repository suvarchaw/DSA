import java.util.*;

class Solution {
    Boolean[][] dp;

    public boolean isMatch(String s, String p) {
        dp = new Boolean[s.length() + 1][p.length() + 1];
        return match(s, p, 0, 0);
    }

    private boolean match(String s, String p, int i, int j) {
        if (dp[i][j] != null) return dp[i][j];

        if (j == p.length()) {
            return dp[i][j] = (i == s.length());
        }

        boolean firstMatch = (i < s.length() &&
                (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.'));

        if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
            dp[i][j] = match(s, p, i, j + 2) ||
                       (firstMatch && match(s, p, i + 1, j));
        } else {
            dp[i][j] = firstMatch && match(s, p, i + 1, j + 1);
        }

        return dp[i][j];
    }
}