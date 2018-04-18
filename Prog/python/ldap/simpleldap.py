# -*- coding: utf-8 -*-
from ldap3 import Server,Connection,AUTO_BIND_NO_TLS,SUBTREE,ALL_ATTRIBUTES
s = Server('ldap://LDAPDOMEIN', 389)

# 認証
c = Connection( s, user='uid=UID,ou=**,ou=**,o=**,c=**', password='PASSWORD', check_names=True, read_only=True, auto_bind=AUTO_BIND_NO_TLS)

print('result',c.result)

# さらに属性情報を抽出する1（全ての属性を取り出す場合 -> ALL_ATTRIBUTESを指定 ）例
#c.search(search_base='ou=cc,ou=ie,o=u-ryukyu,c=jp', search_filter='(&(samAccountName=e155728))', search_scope=SUBTREE, attributes=ALL_ATTRIBUTES, get_operational_attributes=True)
#print( c.response_to_json())

# さらに属性情報を抽出する2（指定した属性のみを取り出す場合 -> 属性名を配列で指定 ）例
#c.search(search_base='dc=ad,dc=[DOMAIN],dc=co,dc=jp', search_filter='(&(samAccountName=[UserID]))', search_scope=SUBTREE, attributes=('displayName','mail','department'), get_operational_attributes=True)
#print( c.response_to_json())
