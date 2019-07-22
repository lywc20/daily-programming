//A program that queries a github user's api for a given login
//Returns {User,name,number of public repositories}

package main

import(
		"fmt"
		"net/http"
		"io/ioutil"
		"log"
		"encoding/json"
		"time"
)

type dat struct{
		User string `json:"login"`
		Name string `json:"name"`
		Public_Repos int `json:"public_repos"`
}

func query(login string) *dat{
		val := dat{}
		url := fmt.Sprintf("https://api.github.com/users/%s", login)
//		resp, err := http.Get(url)

		client := http.Client{
				Timeout: time.Second * 2,
		}

		req, err := http.NewRequest(http.MethodGet, url, nil)
		if err != nil {
				log.Fatalf("error: can't call %s",url)
		}

		res, getErr := client.Do(req)
		if getErr != nil {
				log.Fatalf("error: can't get")
		}

		body, readErr := ioutil.ReadAll(res.Body)
		if readErr != nil {
				log.Fatal(readErr)
		}

		jsonErr := json.Unmarshal(body, &val)
		if jsonErr != nil {
				log.Fatalf("error: can't unmarshal")
		}

		return &val

}

func main() {
	fmt.Println(query("tebeka"))

}
