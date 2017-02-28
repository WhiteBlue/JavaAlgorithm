package main

import "fmt"

var result [][]int

func combine(n int, k int) [][]int {
	result = [][]int{}
	innerCombine(1, n, k, []int{})
	return result
}

func innerCombine(now, n, k int, list []int) {
	if now == n + 1 {
		if len(list) == k {
			result = append(result, list)
		}
		return
	}
	innerCombine(now + 1, n, k, list)
	innerCombine(now + 1, n, k, deepCopyAndAppend(list, now))
}

func deepCopyAndAppend(in []int, value int) []int {
	ret := make([]int, len(in) + 1)
	for index, v := range (in) {
		ret[index] = v
	}
	ret[len(in)] = value
	return ret
}

func main() {
	list := combine(1, 1)
	fmt.Println(list)
}
