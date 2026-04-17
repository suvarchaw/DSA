import java.util.*;

class Solution {
    public int findMaxK(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        
        // Add all elements to set
        for (int num : nums) {
            set.add(num);
        }

        int maxK = -1;

        // Check for k and -k
        for (int num : nums) {
            if (num > 0 && set.contains(-num)) {
                maxK = Math.max(maxK, num);
            }
        }

        return maxK;
    }
}