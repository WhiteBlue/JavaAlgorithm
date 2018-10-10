package main
import (
	"fmt"
)

//小根堆
func buildminheap(heap []int) {
	for i := len(heap) / 2; i > 0; i-- {
		for j := i; j > 0; j-- {
			heapify(heap, j)
		}
	}
}

func heapify(heap []int, index int) {
	if 2 * index + 1 > len(heap) {
		//上下交换
		if heap[2 * index - 1] < heap[index - 1] {
			heap[2 * index - 1], heap[index - 1] = heap[index - 1], heap[2 * index - 1]
		}
	} else {
		largest := 2 * index - 1
		//左右比较
		if heap[2 * index] < heap[2 * index - 1] {
			largest = 2 * index
		}
		//上下比较
		if heap[largest] < heap[index - 1] {
			heap[index - 1], heap[largest] = heap[largest], heap[index - 1]
		}
	}
}

func main() {
	array := []int{4, 5, 7, 10, 6, 3, 1, 8, 2, 9};
	buildminheap(array)
	fmt.Println(array)
}