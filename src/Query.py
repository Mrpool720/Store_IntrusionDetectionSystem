# All imports here
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg
import psycopg2.extras as ex

import WebUI

import sqlalchemy

WebUI.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Rufus862479513@pdv@localhost/store'
db = SQLAlchemy(WebUI.app)

# class User()

conn = pg.connect("dbname='postgres' user='postgres' password='Rufus862479513@pdv' host='localhost'")

cur = conn.cursor()
cur.execute("INSERT INTO products(ID, USERID, NAME, PRICE, ADDRESS, CATEGORY) VALUES(132, 1081, 'Swapnil', 497.4, 'Delhi', 'laptop');")
conn.commit()
cur.execute("select * from products")

rows = cur.fetchall()

for i in rows:
    print(i)

# # Getting data by their colummn names
# cur2 = conn.cursor(cursor_factory=ex.DictCursor)
# cur2.execute("select * from products")
#
# for i in rows:
#     print(i["userid"])
#
# # inputting data in a file
# fhandle= open('dataExport','w')
# cur3 = conn.cursor()
# cur3.copy_to('fhandle', 'products', sep=",")
#
# # inputting data from a file
# fhandle= open('dataExport','r')
# cur3 = conn.cursor()
# cur3.copy_to('fhandle', 'products', sep=",")
# cur3.commit()

