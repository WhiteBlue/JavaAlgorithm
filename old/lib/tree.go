package lib
import "container/list"


type Node struct {
	Value  int
	Lchild *Node
	Rchild *Node
}


//创建二叉树
func BuildTree(list *list.List) *Node {
	val := list.Front();
	if val == nil {
		return nil
	}
	list.Remove(val)

	intval, _ := val.Value.(int)

	if (intval == 0) {
		return nil
	}

	node := new(Node)

	node.Value = intval
	node.Lchild = BuildTree(list)
	node.Rchild = BuildTree(list)

	return node
}