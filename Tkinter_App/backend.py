import sqlite3 as sql


#create a class object, function nested in python class.
class backend():
    def __init__(self,title,keywords,author,year,rows):
        self.title = title
        self.keywords = keywords
        self.author = author
        self.year = year
        #self.filepath = filepath
        self.rows = rows

#View all data and connection to the database.
    def viewall(self):
        self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencefile.db")
        print(self.conn)
        self.cur = self.conn.cursor()
        print(self.cur)
        self.cur.execute("SELECT * FROM papers")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.conn.close()
        return rows

    def search(self,title="",keywords="",author="",year="",rows=""): #=""pass in empty strings
        self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencefile.db")
        print(self.conn)
        self.cur = self.conn.cursor()
        print(self.cur)
        self.cur.execute("SELECT * FROM papers WHERE title=? OR keywords=? OR author=? OR year=?", 
                    (title,keywords,author,year))
        rows = self.cur.fetchall()
        self.conn.close()
        return rows


# #create a search function connect to the SQLite database
# def search(filename="",title="",keywords="",author="",year="",filepath=""): #=""pass in empty strings
#     conn = sql.connect("conferencepaper.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM papers WHERE filename=? OR title=? OR keywords=? OR author=? OR year=? OR filepath=?", 
#                 (filename,title,keywords,author,year,filepath))
#     rows = cur.fetchall()
#     conn.close()
#     return rows
