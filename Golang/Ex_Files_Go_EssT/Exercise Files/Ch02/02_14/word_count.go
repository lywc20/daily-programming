package main

import (
		"fmt"
		"strings"
)

func main() {
		text := `
		Needles and pins
		Needles and pins
		Sew me a sail
		To catch me the wind
		`
		arr := strings.Fields(text)
		counts := map[string]int{} //empty kv map
		for _, word := range arr {
				counts[strings.ToLower(word)]++
		}
		fmt.Println(counts)
}
