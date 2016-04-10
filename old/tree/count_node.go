package tree

func CountNode(node *Node) int {
	if node == nil {
		return 1;
	}
	return CountNode(node.LeftChild) + CountNode(node.RightChild) + 1;
}