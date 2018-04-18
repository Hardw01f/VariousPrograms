import MySQLdb

conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
)
c = conn.cursor()

def create():
	sql = 'create table create_table(name varchar(64),uid varchar(10),edyid varchar(100));'
	c.execute(sql)
	conn.commit()

def delete():
	sql = 'drop table create_table'
	c.execute(sql)
	conn.commit()

if __name__ == "__main__":
    delete()


