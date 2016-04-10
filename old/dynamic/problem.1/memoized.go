package main
import (
	"math"
	"fmt"
)



func main() {
	price := []int{1, 5, 8, 9, 10, 17, 17, 20, 24, 30}

	memo := make([]int, len(price))

	for i := range memo {
		memo[i] = -1;
	}

	back := list_all_memo(price, len(price), memo)

	fmt.Print(back)
}


func list_all_memo(price[] int, n int, memo []int) int {
	if n == 0 {
		return 0
	}

	if memo[n-1] > 0 {
		return memo[n-1]
	}
	var query float64 = -1
	for i := 1; i <= n; i++ {
		query = math.Max(float64(query), float64(price[i - 1] + list_all_memo(price, n - 1, memo)))
	}
	memo[n-1] = int(query)
	return int(query)
}