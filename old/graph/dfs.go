package main
import (
	"fmt"
	"strconv"
	. "github.com/whiteblue/GoAlgorithm/lib"
)


func dfs(node *GraphNode, visited[] *GraphNode, end *GraphNode, count int) (int) {
	for _, cNode := range (node.Neighbours) {
		if cNode == end {
			return count
		}
		if !FindNode(cNode, visited) {
			visited = append(visited, cNode)
			cBack := dfs(cNode, visited, end, count + 1)
			if cBack > 0 {
				return cBack
			}

			visited = DeleteNode(cNode, visited)
		}
	}
	return -1;
}

func findDFS(start *GraphNode, end *GraphNode) (int, bool) {
	visited := make([]*GraphNode, 0)
	back := dfs(start, visited, end, 1)
	return back, back >= 0
}


func main() {
	end := &GraphNode{Val:10, Neighbours:[]*GraphNode{}}

	mid0 := &GraphNode{Val:9, Neighbours:[]*GraphNode{end}}
	mid1 := &GraphNode{Val:8, Neighbours:[]*GraphNode{mid0}}
	mid2 := &GraphNode{Val:7, Neighbours:[]*GraphNode{mid1}}

	start := &GraphNode{Val:0, Neighbours:[]*GraphNode{mid2}}

	fLen, result := findDFS(start, end)

	fmt.Println("Find result:" + strconv.FormatBool(result))

	if result {
		fmt.Println("Go:" + strconv.Itoa(fLen) + " times")
	}
}