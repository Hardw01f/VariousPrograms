import MySQLdb

conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
)
c = conn.cursor()

idm = '3001011501160155'

sql = "select * from ldap_idm where edyid=%s"
c.execute(sql,[idm])
result = c.fetchall()
print(result)
