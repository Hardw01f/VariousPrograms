package main

import (
	"fmt"
	"os/exec"
)

func main() {
	//fmt.Println("処理開始: ", time.Now().Format("15:04:05"))
	//cmd := exec.Command("sleep", "5s")
	//cmd.Start()
	//fmt.Println("sleep中: ", time.Now().Format("15:04:05"))
	//cmd.Wait()
	//fmt.Println("sleep終了: ", time.Now().Format("15:04:05"))

	out, err := exec.Command("ls", "-la").Output()
	fmt.Println(string(out))
	fmt.Println(err)

	err02 := exec.Command("node", "hello.js").Run()
	fmt.Println(err02)
}
