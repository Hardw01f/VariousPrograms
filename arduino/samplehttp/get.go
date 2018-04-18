package main


import(
		"fmt"
		"os/exec"
		"strings"
)

func main(){

	out,_ := exec.Command("node","safetemp.js").Output()
	//fmt.Println(string(out))
	temp := string(out)
	res := strings.Fields(temp)
	//fmt.Println(res)
	fmt.Println(res[6])
}
