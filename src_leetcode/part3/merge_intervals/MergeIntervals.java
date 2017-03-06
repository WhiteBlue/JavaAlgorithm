import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/**
 * id: 56
 * <p>
 * Given a collection of intervals, merge all overlapping intervals.
 */

class Interval {
    int start;
    int end;

    Interval() {
        start = 0;
        end = 0;
    }

    Interval(int s, int e) {
        start = s;
        end = e;
    }

    @Override
    public String toString() {
        return "Interval{" +
                "start=" + start +
                ", end=" + end +
                '}';
    }
}

public class MergeIntervals {

    public List<Interval> merge(List<Interval> intervals) {
        if (intervals.size() == 0) {
            return intervals;
        }

        intervals.sort(Comparator.comparingInt(o -> o.start));
        LinkedList<Interval> retList = new LinkedList<>();

        Interval tmp = intervals.get(0);
        for (int i = 1; i < intervals.size(); i++) {
            Interval target = intervals.get(i);
            if (target.end < tmp.start || target.start > tmp.end) {
                // can not combine
                retList.push(tmp);
                tmp = target;
            } else {
                tmp.start = Integer.min(tmp.start, target.start);
                tmp.end = Integer.max(tmp.end, target.end);
            }
        }
        retList.push(tmp);
        return retList;
    }

}
