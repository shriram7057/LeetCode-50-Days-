import java.util.*;

class Solution {
    public double separateSquares(int[][] squares) {
        double low = Double.MAX_VALUE, high = Double.MIN_VALUE;
        for (int[] s : squares) {
            low = Math.min(low, s[1]);
            high = Math.max(high, s[1] + s[2]);
        }

        double total = areaBelow(squares, high);

        for (int i = 0; i < 100; i++) {
            double mid = (low + high) / 2.0;
            double below = areaBelow(squares, mid);
            if (below * 2 < total) low = mid;
            else high = mid;
        }
        return (low + high) / 2.0;
    }

    private double areaBelow(int[][] squares, double y) {
        List<double[]> events = new ArrayList<>();
        for (int[] s : squares) {
            double bottom = s[1];
            double top = s[1] + s[2];
            if (bottom >= y) continue;
            double up = Math.min(top, y);
            events.add(new double[]{s[0], bottom, up, 1});
            events.add(new double[]{s[0] + s[2], bottom, up, -1});
        }

        events.sort(Comparator.comparingDouble(a -> a[0]));
        double area = 0, prevX = 0;
        TreeMap<Double, Integer> map = new TreeMap<>();

        for (double[] e : events) {
            double x = e[0];
            area += (x - prevX) * coveredY(map);
            prevX = x;
            map.put(e[1], map.getOrDefault(e[1], 0) + (int)e[3]);
            map.put(e[2], map.getOrDefault(e[2], 0) - (int)e[3]);
            if (map.get(e[1]) == 0) map.remove(e[1]);
            if (map.get(e[2]) == 0) map.remove(e[2]);
        }
        return area;
    }

    private double coveredY(TreeMap<Double, Integer> map) {
        double res = 0;
        int cnt = 0;
        Double prev = null;
        for (Map.Entry<Double, Integer> e : map.entrySet()) {
            if (cnt > 0 && prev != null) {
                res += e.getKey() - prev;
            }
            cnt += e.getValue();
            prev = e.getKey();
        }
        return res;
    }
}
