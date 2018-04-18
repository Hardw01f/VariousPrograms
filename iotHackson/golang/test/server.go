package main

import (
	"fmt"
	"net"
	"os"
	//"os/exec"
	"time"
)

func main() {
	service := ":55555"
	tcpAddr, err := net.ResolveTCPAddr("tcp", service)
	checkError(err)
	listner, err := net.ListenTCP("tcp", tcpAddr)
	checkError(err)
	for {
		conn, err := listner.Accept()
		if err != nil {
			continue
		}

		go handleClient(conn)
	}
}

func handleClient(conn net.Conn) {
	defer conn.Close()
	conn.SetReadDeadline(time.Now().Add(10 * time.Second))
	fmt.Println("client accept!")
	messageBuf := make([]byte, 1024)
	messageLen, err := conn.Read(messageBuf)
	checkError(err)

	message := string(messageBuf[:messageLen])
	fmt.Println("accepted message : " + message)

	//if message == "hogehoge" {
	//	res := exec.Command("node", "labo/hello.js").Run()
	//	fmt.Println(res)
	//}

	//message = message + " too!"

	//conn.SetWriteDeadline(time.Now().Add(10 * time.Second))
	//conn.Write([]byte(message))
}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "fatal: error: %s", err.Error())
		os.Exit(1)
	}
}
