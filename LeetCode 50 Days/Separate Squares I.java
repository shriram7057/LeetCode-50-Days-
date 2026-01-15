class Solution {
    public double separateSquares(int[][] squares) {
        double low = Double.MAX_VALUE, high = Double.MIN_VALUE;
        for (int[] s : squares) {
            low = Math.min(low, s[1]);
            high = Math.max(high, s[1] + s[2]);
        }

        for (int iter = 0; iter < 100; iter++) {
            double mid = (low + high) / 2.0;
            double above = 0, below = 0;

            for (int[] s : squares) {
                double y = s[1], l = s[2];
                double top = y + l;

                if (top <= mid) {
                    below += l * l;
                } else if (y >= mid) {
                    above += l * l;
                } else {
                    below += (mid - y) * l;
                    above += (top - mid) * l;
                }
            }

            if (below < above) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return (low + high) / 2.0;
    }
}
