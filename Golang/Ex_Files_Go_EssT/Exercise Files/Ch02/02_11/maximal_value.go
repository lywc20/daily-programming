package main

import( "fmt" )

func main() {
		list := []int{16, 8, 42, 4, 23, 15}
		max := list[0]
		for _, val := range list[1:] {
				if val > max {
						max = val
				}
		}
		fmt.Println(max)
}
