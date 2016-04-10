package main
import (
	"math"
	"fmt"
)



func main() {
	price := []int{1, 5, 8, 9, 10, 17, 17, 20, 24, 30}

	back := list_all(price, len(price))

	fmt.Print(back);
}


func list_all(price[] int, n int) int {
	if n == 0 {
		return 0
	}
	var query float64 = -1
	for i := 1; i <= n; i++ {
		query = math.Max(float64(query), float64(price[i - 1] + list_all(price, n - 1)))
	}
	return int(query)
}