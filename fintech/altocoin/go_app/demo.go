package main

import(
		"fmt"
		"net/http"
		"io/ioutil"
		"strconv"
)

//後はmysql接続からの値取り出しと整形

func main(){
		url := "https://coincheck.com/api/ticker"

		resp, _ := http.Get(url)
		defer resp.Body.Close()

		byteArray, _ := ioutil.ReadAll(resp.Body)
		fmt.Println(string(byteArray))
		get := string(byteArray)
		get = get[8:15] 
		fmt.Println(get)
		now_rate, _ := strconv.Atoi(get)
		fmt.Println(now_rate)
}
