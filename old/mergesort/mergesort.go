package main
import "fmt"


func mergesort(arr []int, begin int, end int) []int {
	if begin == end {
		return []int{arr[begin]}
	}
	index := (begin + end) / 2
	l := mergesort(arr, begin, index)
	r := mergesort(arr, index + 1, end)
	return merge(l, r)
}


func merge(arr0 []int, arr1 []int) []int {
	l := len(arr0)
	r := len(arr1)

	max := l
	if l < r {
		max = r
	}
	returnArr := make([]int, 0, max)

	a, b := 0, 0;
	for a < l&&b < r {
		if (arr0[a] > arr1[b]) {
			returnArr = append(returnArr, arr1[b])
			b++
		}else {
			returnArr = append(returnArr, arr0[a])
			a++
		}
	}

	for a < l {
		returnArr = append(returnArr, arr0[a])
		a++
	}

	for b < r {
		returnArr = append(returnArr, arr1[b])
		b++
	}
	return returnArr
}


func main() {
	array := []int{4, 5, 7, 10, 6, 3, 1, 8, 2, 9};
	array = mergesort(array, 0, len(array) - 1)
	fmt.Println(array)
}
