package lib

type GraphNode struct {
	Val        int
	Neighbours []*GraphNode
}

func FindNode(node *GraphNode, list []*GraphNode) bool {
	flag := false
	for _, ele := range (list) {
		if ele == node {
			flag = true
		}
	}
	return flag
}


func DeleteNode(node *GraphNode, list []*GraphNode) []*GraphNode {
	for index, ele := range (list) {
		if ele == node {
			return append(list[:index - 1], list[index:len(list)]...)
		}
	}
	return list
}
