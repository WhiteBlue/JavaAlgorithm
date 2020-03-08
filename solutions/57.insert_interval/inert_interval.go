package main

/*
	Id: 57
	Insert Interval

	Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 */


//Definition for an interval.
type Interval struct {
	Start int
	End   int
}

func findMid(intervals []Interval, target Interval) ([]Interval, []Interval) {
	retList := make([]Interval, 0)
	newIntervals := make([]Interval, 0)
	for _, interval := range (intervals) {
		if (interval.Start <= target.Start &&interval.End >= target.Start) ||
		(interval.Start <= target.End&&interval.End >= target.End) ||
		(interval.Start >= target.Start&&interval.End <= target.End) {
			retList = append(retList, interval)
		} else {
			newIntervals = append(newIntervals, interval)
		}
	}
	return retList, newIntervals
}

func combine(intervals []Interval, target Interval) []Interval {
	min := target.Start
	max := target.End
	for _, interval := range (intervals) {
		if interval.Start < min {
			min = interval.Start
		}
		if interval.End > max {
			max = interval.End
		}
	}

	return []Interval{Interval{Start:min, End:max}}
}

func insert(intervals []Interval, newInterval Interval) []Interval {
	targets, listA := findMid(intervals, newInterval)
	listB := combine(targets, newInterval)

	retList := make([]Interval, 0, len(listA) + len(listB))

	iterA, iterB := 0, 0
	for iterA < len(listA)&&iterB < len(listB) {
		if listA[iterA].Start < listB[iterB].Start {
			retList = append(retList, listA[iterA])
			iterA++
		} else {
			retList = append(retList, listB[iterB])
			iterB++
		}
	}

	for ; iterA < len(listA); iterA++ {
		retList = append(retList, listA[iterA])
	}

	for ; iterB < len(listB); iterB++ {
		retList = append(retList, listB[iterB])
	}

	return retList
}

