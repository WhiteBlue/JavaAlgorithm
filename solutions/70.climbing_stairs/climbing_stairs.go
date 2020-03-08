package main

func climbStairs(n int) int {
	arr := make([]int, n + 1)
	arr[0], arr[1] = 1, 1
	if n < 2 {
		return arr[n]
	}
	for i := 2; i <= n; i++ {
		arr[i] = arr[i - 1] + arr[i - 2]
	}
	return arr[n]
}
