import sqlite3 as sq



db = sq.connect("app.db")
#set up the cusor
cr = db.cursor()
cr.execute ("create table  if not exists users(user_id integer, name text)")

# cr.execute("CREATE TABLE if not exists skills (name TEXT, progress INTEGER, user_id INTEGER)")
# cr.execute("insert into users (user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users (user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osame')")
# cr.execute("insert into users(user_id, name) values(4, 'Osame')")


# cr.execute("update users set name ='Gamal' where name ='Osame'")
cr.execute("update users set name ='Osam' where user_id = 4")



#save changes
db.commit()


#close databse
db.close()