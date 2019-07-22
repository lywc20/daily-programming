
package main

import (
		"fmt"
)
/*
func fizzBuzz(inp) {
		if inp % 3 == 0 {
				fmt.Println("fizz")
		} else if inp % 5 == 0 {
				fmt.Println("buzz")
		} else if inp % 5 == 0 && inp % 3 == 0{
				fmt.Println("fizz buzz")
		} else {
				fmt.Println(inp)
		}
}
*/
func main() {
		for inp := 1; inp <= 20; inp++ {
				if inp % 3 == 0 && inp % 5 == 0 {
						fmt.Println("fizz buzz")
				} else if inp % 5 == 0 {
						fmt.Println("buzz")
				} else if inp % 3 == 0 {
						fmt.Println("fizz")
				} else {
						fmt.Println(inp)
				}
		}
}
