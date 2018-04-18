package main

import (
	"fmt"
	"net"
	"os"
	"os/exec"
	"time"
	"strings"
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
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

	db, err := sql.Open("mysql", "milk:kakaobeans@/chocorate")
  		if err != nil {
    		panic(err.Error())
  		}
  	defer db.Close()

	defer conn.Close()
	conn.SetReadDeadline(time.Now().Add(10 * time.Second))
	fmt.Println("client accept!")
	messageBuf := make([]byte, 1024)
	messageLen, err := conn.Read(messageBuf)
	checkError(err)

	message := string(messageBuf[:messageLen])

	slice := strings.Split(message,",")
	timestamp := slice[0]
	location := slice[1]
	fmt.Println("accepted time : " ,timestamp)
	fmt.Println("accepted location : ", location)

	_, err = db.Exec("insert into kokoas(invasion_time, invasion_location) values(?, ?)",timestamp,location,)

	if err != nil {
		fmt.Println(err)
	}

	if message == "hogehoge" {
		res := exec.Command("node", "labo/hello.js").Run()
		fmt.Println(res)
	}

	//message = message + " too!"

	conn.SetWriteDeadline(time.Now().Add(10 * time.Second))
	conn.Write([]byte(message))
}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "fatal: error: %s", err.Error())
		os.Exit(1)
	}
}
