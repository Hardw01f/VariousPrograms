# -*- coding: utf-8 -*-

# searchテスト
import ldap
import MySQLdb

conn = MySQLdb.connect(
        user='USERNAME',
        passwd='PASSWORD',
        host='HOSTNAME',
        db='DBNAME'
)
c = conn.cursor()


# LDAP接続

ldaphost  = "ldap://DOMEINADDRESSS:389"

baseDN    = "ou=**,ou=**,o=**,c=**"

username  = "uid=UID"

password  = "PASSWORD"

# 検索条件 とりあえずuid全部取得

searchFilter = "(uid=*)"

count     = 0



# LDAPサーバ接続

try:

    l = ldap.initialize(ldaphost)

    l.protocol_version = ldap.VERSION3

    l.simple_bind_s(username, password)


except ldap.LDAPError, e:


    print e



# サブツリー配下取得

searchScope = ldap.SCOPE_SUBTREE

# 全属性取得

retrieveAttributes = None 



try:

    search_results = l.search_s(baseDN, searchScope, searchFilter, retrieveAttributes)

    print "検索結果 %d 件" % len(search_results)



    if len(search_results) == 0:

        print "検索結果0件のため、処理なし"

    else:    

        for base_dn, search_result in search_results:

            try:

                gecos = search_result.get('gecos')

                uid = search_result.get('uid')

                #ldapedyid = search_result.get('ldapedyid')

                #print "gecos = %s,uid = %s,ldapedyid = %s" % (gecos,uid,ldapedyid)
		
		print(gecos)
		print(uid)
		#print(ldapedyid)

		#id = ','.join(ldapedyid)
		
		#print(id)

                sql='insert into name_uid values(%s,%s)'
                c.execute(sql,(uid,gecos))
                conn.commit()
            except:

                pass

except ldap.LDAPError, error_message:

    print error_message



# LDAPサーバ切断

l.unbind_s()
