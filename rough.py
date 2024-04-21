import MySQl.connector as db
con=db.connect(user="root",password="deekShith@25",host="localhost")
print(con)
con.close()
