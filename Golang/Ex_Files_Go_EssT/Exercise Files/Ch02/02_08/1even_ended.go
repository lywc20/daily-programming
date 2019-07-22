package main

import (
		"fmt"
)

func main() {
		//a,b,c := 1,11,121
		//d := 123
		count := 0
		for i := 1000; i < 10000; i++ {
				for j := i; j < 10000; j++ {
						sum := i * j
						sumToString := fmt.Sprintf("%d", sum)
						length := len(sumToString)
						if sumToString[0] == sumToString[length-1] {
								count++
						}
				}
		}
		newCount := fmt.Sprintf("%d", count)
		fmt.Println("Count = " + newCount)
}
