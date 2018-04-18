TEST=`lsusb | grep 054c:06c3`
TEST=(`echo "$TEST" | sed s/"Bus 001 Device "//g | sed s/": ID 054c:06c3 Sony Corp.//g"`)
#echo ${TEST[0]}
#echo ${TEST[1]}

TEST2=`sudo udevadm info -q all -n /dev/bus/usb/001/${TEST[0]} | grep ID_SERIAL_SHORT`
TEST2=`echo "$TEST2" | sed s/"E: ID_SERIAL_SHORT="//g`
#echo $TEST2


TEST3=`sudo udevadm info -q all -n /dev/bus/usb/001/${TEST[1]} | grep ID_SERIAL_SHORT`
TEST3=`echo "$TEST3" | sed s/"E: ID_SERIAL_SHORT="//g`
#echo $TEST3

if [ $TEST2 == "0523814" ];
then
	#echo "INは${TEST[0]}"
	#echo "OUTは${TEST[1]}"
	sed -e "s/"OUT_PASORI"/${TEST[1]}/g" 334out.py > 335out.py
	sed -e "s/"IN_PASORI"/${TEST[0]}/g" 334in.py > 335in.py
	sudo python 335out.py &
	RET2=$?
	sudo python 335in.py
	#echo $?
	RET=$?
	if [ $RET -eq 1 ] ;then
	exit 1
	fi
	
else
	#echo "INは${TEST[1]}"
	#echo "OUTは${TEST[0]}"
	sed -e "s/"OUT_PASORI"/${TEST[0]}/g" 334out.py > 335out.py
	sed -e "s/"IN_PASORI"/${TEST[1]}/g" 334in.py > 335in.py	
        sudo python 335out.py &
	#RET2=$?
        sudo python 335in.py
	#echo $?
	RET=$?
        if [ $RET -eq 1 ] ;then
        exit 1 
	fi
fi


#IN_PASORI
#OUT_PASORI
