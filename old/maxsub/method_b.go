package main
import (
	"fmt"
	"strconv"
)

func maxSub(array[] int) int {
	length, max, temp := len(array), array[0], 0
    
    for i := 0; i < length; i++{
        temp += array[i]
        //当前子序列为负
        if temp < 0{
            //舍弃子序列
            temp = 0
            continue
        }
        
        //替换最大值
        if temp > max{
            max=temp
        }
        
    }
	return max;
}


func main() {
	array := []int{2, 3, -1, 4, -1, -7, -8, 4, 9};

	back := maxSub(array)

	fmt.Println("Back:" + strconv.Itoa(back))
}