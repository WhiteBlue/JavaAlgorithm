package main

import (
	"container/list"
	"fmt"
	"strconv"
	. "github.com/whiteblue/GoAlgorithm/lib"
)



func findBFS(start *GraphNode, end *GraphNode) (int, bool) {
	//访问过的
	visited := make([]*GraphNode, 0)

	queue := list.New()

	//推入首节点
	queue.PushFront(start)

	fLen := 0

	//当前队列不为空
	for queue.Len() > 0 {
		fLen++;

		ele := queue.Front()
		queue.Remove(ele)

		node, _ := ele.Value.(*GraphNode)

		visited = append(visited, node)

		for _, nigh := range (node.Neighbours) {
			if nigh == end {
				//找到目标
				return fLen, true;
			}

			//未访问过
			if !FindNode(nigh, visited) {
				queue.PushFront(nigh)
			}
		}
	}
	return -1, false;
}



func main() {
	end := &GraphNode{Val:10, Neighbours:[]*GraphNode{}}

	mid0 := &GraphNode{Val:9, Neighbours:[]*GraphNode{end}}
	mid1 := &GraphNode{Val:8, Neighbours:[]*GraphNode{mid0}}
	mid2 := &GraphNode{Val:7, Neighbours:[]*GraphNode{mid1}}

	start := &GraphNode{Val:0, Neighbours:[]*GraphNode{mid2}}

	fLen, result := findBFS(start, end)

	fmt.Println("Find result:" + strconv.FormatBool(result))

	if result {
		fmt.Println("Go:" + strconv.Itoa(fLen) + " times")
	}
}