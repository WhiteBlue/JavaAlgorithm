package tree
import (
	. "github.com/whiteblue/GoAlgorithm/lib"
	"container/list"
	"fmt"
)


type LinkedNode struct {
	father *Node
}


//后序遍历
func buildLinked(target *Node, end int, flag []bool) {
	if target != nil {
		buildLinked(target.Lchild, end, flag)
		if flag[0] {
			fmt.Println(target.Value)
		}

		if target.Value == end {
			flag[0] = true;
		}
		buildLinked(target.Rchild, end, flag)
	}
}


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

	buildLinked(top, 6, []bool{false})
}
