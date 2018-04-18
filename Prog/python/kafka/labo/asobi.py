import MySQLdb
import sys

conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
)
c = conn.cursor()



def get_num(idm):
        sql = 'select * from ldap_idm where uid=%s'
        c.execute(sql,[idm])
        result = c.fetchall()
        #result = str(result[0])
        #result = result.split(",")
        #result = result[0]
        #result = result.replace("(","")
        return result
        #c.commit()






if __name__ == "__main__":
    num = 1
    flag=1
    while(flag):
    	if num < 10:
		ban = "0" + str(num)
		uid = "e1557"+ban
		print(uid)
		print(get_num(uid))
		num = num + 1
    	else:
        	ban = str(num)
		uid = "e1557"+ban
		print(uid)
		print(get_num(uid))
		num = num + 1
		if num > 68:
			sys.exit()	
