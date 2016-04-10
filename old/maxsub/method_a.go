package main
import (
	"fmt"
	"strconv"
)


func maxSub(array[] int) int {
	length, max := len(array), 0

	tempArr := make([]int, length)
	tempArr[0] = array[0]

	for pre := 1; pre < length; pre++ {
		tempArr[pre] = tempArr[pre - 1] + array[pre]
	}

	for a := 0; a < length; a++ {
		for b := a; b < length; b++ {
			temp := tempArr[b] - tempArr[a]
			if temp >= max {
				max = temp
			}
		}
	}

	return max;
}


func main() {
	array := []int{2, 3, -1, 4, -1, -7, -8, 4, 9};

	back := maxSub(array);

	fmt.Println("Back:" + strconv.Itoa(back));
}
