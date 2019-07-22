package main

import (
		"fmt"
		"net/http"
)

func contentType(url string) (string, error) {
		// a function that gets a URL and returns the value of content-type response http header or an error if it can't get a get request
		resp, err := http.Get(url)
		if err != nil {
				return "", err
		}

		defer resp.Body.Close()

		val := resp.Header.Get("Content-type")
		if val == "" {
				return "", fmt.Errorf("Can't find content-type header")
		}

		return val, nil
}

func main() {
		ctype, err := contentType("https://linkedin.com")
		if err != nil {
				fmt.Printf("ERROR: %s\n", err)
		} else {
				fmt.Println(ctype)
		}
}
