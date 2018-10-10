package main
import "fmt"


func quicksort(array []int, a int, b int) {
	//递归终止
	if a < b {
		i := partition(array, a, b)
		//分治
		quicksort(array, a, i - 1)
		quicksort(array, i + 1, b)
	}
}

func partition(array []int, a int, b int) int {
	//取末尾为主元
	x := array[b]
	//起始位置
	i := a - 1
	//foreach a -> b - 1
	for j := a; j < b; j++ {
		if array[j] <= x {
			i++
			array[i], array[j] = array[j], array[i]
		}
	}
	//填最后一个空
	array[i + 1], array[b] = array[b], array[i + 1]
	return i + 1;
}


func main() {
	array := []int{4, 5, 7, 10, 6, 3, 1, 8, 2, 9};
	quicksort(array, 0, len(array) - 1)
	fmt.Println(array)
}


