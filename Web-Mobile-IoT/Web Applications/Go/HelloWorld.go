package main

import "fmt"

func main() {

	var i, j, row, col int
	row = 5
	col = 7
	fmt.Println("Hello World!")
	//fmt.Print("Enter the Rectangle Rows = ")
	//fmt.Scanln(&row)

	//fmt.Print("Enter the Rectangle Columns = ")
	//fmt.Scanln(&col)

	fmt.Println("Rectangle Star Pattern")
	for i = 0; i < row; i++ {
		for j = 0; j < col; j++ {
			fmt.Print("🟦")
		}
		fmt.Println()
	}
}
