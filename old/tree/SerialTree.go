package main

import "container/list"

func main() {
	list := list.New()
	list.PushBack(0)
	list.PushBack(4)
	list.PushBack(6)
	list.PushBack(2)
	list.PushBack(1)
	list.PushBack(0)
	list.PushBack(6)
	list.PushBack(0)
	list.PushBack(0)
	list.PushBack(3)
	list.PushBack(0)
	list.PushBack(5)
	list.PushBack(7)

	top := CreateTree(list)
}

func MiddleReverse(list *list.List) {
	left := list.Front()
	if left != nil {
		list.Remove(left)
	}
}