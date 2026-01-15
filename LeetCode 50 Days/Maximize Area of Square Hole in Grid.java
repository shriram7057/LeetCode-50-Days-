import java.util.*;

class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxH = longestConsecutive(hBars);
        int maxV = longestConsecutive(vBars);
        int side = Math.min(maxH, maxV);
        return side * side;
    }

    private int longestConsecutive(int[] bars) {
        if (bars.length == 0) return 1;
        Arrays.sort(bars);
        int max = 1, cur = 1;
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i - 1] + 1) {
                cur++;
            } else {
                cur = 1;
            }
            max = Math.max(max, cur);
        }
        return max + 1;
    }
}
