package main

import (
	"fmt"
)

/*
	id: 65

	Validate if a given string is numeric
 */

func isNumber(s string) bool {
	arr := []int32(s)
	for _, b := range arr {

		fmt.Println(b)
	}
	fmt.Println(arr)
	return true
}

func main() {
	isNumber("233")
}
