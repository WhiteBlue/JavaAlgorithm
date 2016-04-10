package main

import (
	"container/list"
	"fmt"
	"strconv"
	. "github.com/whiteblue/GoAlgorithm/lib"

)


func main() {
	list := list.New()
	list.PushBack(1)
	list.PushBack(2)
	list.PushBack(0)
	list.PushBack(4)
	list.PushBack(0)
	list.PushBack(6)
	list.PushBack(0)
	list.PushBack(0)
	list.PushBack(3)
	list.PushBack(0)
	list.PushBack(5)
	list.PushBack(7)

	top := BuildTree(list)

	Print(top)
}


func Print(top *Node) {
	//初始化last/nextLast
	var (
		last *Node = top
		nextLast *Node
		node *list.Element
	)

	temp := list.New()
	temp.PushBack(top)

	for node = temp.Front(); node != nil; node = temp.Front() {
		temp.Remove(node)
		val, _ := node.Value.(*Node)

		fmt.Print(strconv.Itoa(val.Value) + " ")

		if val.Lchild != nil {
			temp.PushBack(val.Lchild)
			nextLast = val.Lchild
		}

		if val.Rchild != nil {
			temp.PushBack(val.Rchild)
			nextLast = val.Rchild
		}

		//打印到行尾
		if val == last {
			fmt.Print("\n")
			last = nextLast
		}
	}
}
