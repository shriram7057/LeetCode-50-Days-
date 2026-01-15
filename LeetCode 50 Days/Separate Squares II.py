class Solution(object):
    def separateSquares(self, squares):
        import bisect
        events = []
        for x, y, l in squares:
            events.append((y, x, x + l, 1))
            events.append((y + l, x, x + l, -1))

        events.sort()
        xs = []
        active = []
        area_segments = []
        total_area = 0.0

        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            length = 0
            s, e = intervals[0]
            for ns, ne in intervals[1:]:
                if ns > e:
                    length += e - s
                    s, e = ns, ne
                else:
                    e = max(e, ne)
            return length + (e - s)

        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                width = union_length(active)
                area = width * dy
                area_segments.append((prev_y, y, width, total_area))
                total_area += area
                prev_y = y

            while i < len(events) and events[i][0] == y:
                _, x1, x2, t = events[i]
                if t == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))
                i += 1

        half = total_area / 2.0

        for y1, y2, w, acc in area_segments:
            area = w * (y2 - y1)
            if acc + area >= half:
                return y1 + (half - acc) / w

        return events[-1][0]
