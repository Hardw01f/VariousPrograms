ps aux | grep "go run server.go" | grep -v grep | awk '{ print "kill -9", $2 }' | sh
