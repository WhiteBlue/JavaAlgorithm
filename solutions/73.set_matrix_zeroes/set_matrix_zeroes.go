package main

func setZeroes(matrix [][]int) {
	resultX := make([]int, len(matrix[0]))
	resultY := make([]int, len(matrix))

	for indexY, arrY := range (matrix) {
		for indexX, target := range (arrY) {
			if target == 0 {
				resultX[indexX] = 1
				resultY[indexY] = 1
			}
		}
	}

	for indexY, arrY := range (matrix) {
		for indexX, _ := range (arrY) {
			if resultX[indexX] == 1 || resultY[indexY] == 1 {
				arrY[indexX] = 0
			}
		}
	}
}

