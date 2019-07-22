// channels
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int)

	// This will block
/*		<-ch
		fmt.Println("Here")
		*/

	go func() {
			// Send number of the channel
			ch <- 353
	}()
	// Recieve from the channel
	go func() {
			for i:=0;i<3;i++ {
					fmt.Printf("sending %d\n",i)
					ch <- i
					time.Sleep(time.Second)
			}
	}()
	for i :=0;i <3;i++ {
		val := <-ch
		fmt.Printf("got %d\n", val)
	}
}
