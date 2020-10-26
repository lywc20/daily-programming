package main

import (
    "fmt"
)
 
func main() {
    fmt.Println(climbStairs(4))
}   

func climbStairs(n int) int {
    memo := make([]int, n+1)
    memo[0] = 1
    memo[1] = 1
    for i:=2; i <= n; i++ {
        memo[i] = memo[i-1] + memo[i-2]
    } 
    return memo[n]
}
