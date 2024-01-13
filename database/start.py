import sqlite3 as sq

def get_all_data():
    try:
        #connect to database
        db = sq.connect("app.db")
        print("connected succesfully")

        #set the cursor
        cr = db.cursor()

        # fetch data from database
        cr.execute("select *from users")

        # assign data to a variable
        result = cr.fetchall()

        # print the number of rows
        print(f"Databaseee Has {len(result)} Rows")

        print("showing data")

        #showing data
        for row in result:
            print(f"UserId => {row[0]}, UserName => {row[1]}")
           

    except sq.Error as er:
        print (f'cant read data {er}')


    finally:
        if(db):
            db.close()
            print ("database closed successfully")

get_all_data()
