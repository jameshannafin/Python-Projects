import sqlite3 #import the sqlite3 DB module

conn = sqlite3.connect('assignment222.db')#Connect to the database (this will create one if  that name does not exist) and store it in a variable
newfilelist = ('information.docx','Hello.txt','myImage.png',\#Create a tuples of new files to sift through
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('assignment222.db')#Connect to the database (this will create one if  that name does not exist)
with conn:#state we are using the database within this variable 
    cur = conn.cursor() #create a variable to control our cursor
    """
        The following code will use the execute method to run SQL code
        that will create a table (if it does not exist) named tbl_files.
        It will have a primary ID key that will autoincrement and also
        a column named words that contains text
    """
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,words TEXT)")
    conn.commit()#commit these changes to the database 
conn.close()#close the connection

conn = sqlite3.connect('assignment222.db')#Connect to the database (this will create one if  that name does not exist)
for x in newfilelist: #a for loop that automatically iterates trough the newfiles tuple
    if x.endswith('.txt'):
        with conn:#state we are using the database within this variable 
            cur = conn.cursor()#create a variable to control our cursor
            cur.execute("INSERT INTO tbl_files (words) VALUES (?)", (x,))#run SQL code interating X for (?) 
            print(x)#Pring result
conn.close()#close the connection





