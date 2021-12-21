import sqlite3

conn = sqlite3.connect('assignment222.db')
newfilelist = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        words TEXT, \
        )")
    conn.commit()
conn.close()


for x in newfilelist:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (words) VALUES (?)", (x,))
            print(x)
conn.close()



with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah',"Jones",'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname, col_email) VALUES (?,?,?)", \
                ('Sally',"May",'msmith@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname,col_lname, col_email)  VALUES (?,?,?)", \
                ('Kevin',"Bacon",'kbacon@gmail.com'))

    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = 'First Name: {}\nLast Name: {}\nEmail: {}'.format(item[0],item[1],item[2])
    print(msg)
