import sqlite3 as sql


#create a class object, function nested in python class.
class backend():
    def __init__(self,filename,title,keywords,author,year,filepath,rows):
        self.filename = filename
        self.title = title
        self.keywords = keywords
        self.author = author
        self.year = year
        self.filepath = filepath
        self.rows = rows

    #Don't need to have two sql.connect() in the same class, because connect is use in viewall()
    # def connect(self):
    #     self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencepaper.db")
    #     self.cur = self.conn.cursor()
    #     self.cur.execute('''CREATE TABLE IF NOT EXISTS papers (
    #         filename text, title text, keywords text, author text, year integer, filepath text)''')
    #     self.conn.commit()
    #     self.conn.close()

    def viewall(self):
        self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencepaper.db")
        print(self.conn)
        self.cur = self.conn.cursor()
        print(self.cur)
        self.cur.execute("SELECT * FROM papers")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.conn.close()
        return rows

    def search(self,filename="",title="",keywords="",author="",year="",filepath=""): #=""pass in empty strings
        self.conn = sql.connect("conferencepaper.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM papers WHERE filename=? OR title=? OR keywords=? OR author=? OR year=? OR filepath=?", 
                    (filename,title,keywords,author,year,filepath))
        rows = self.cur.fetchall()
        self.conn.close()
        return rows
    
    #testing code
    # def mytest3(self):
    #     print("I am here")
    #     self.connect()
    #     self.viewall()
    #     self.search("test","test","test","test","test","test")
        
# be = backend("test","test","test","test","test","test","test")
# be.viewall()
# #connect the SQLite DB browser conferencepaperDB
# def connect():
#     conn = sql.connect("conferencepaper.db")
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS papers (
#         filename text, title text, keywords text, author text, year integer, filepath text)''')
#     conn.commit()
#     conn.close()

# #View all data from database
# def viewall():
#     conn = sql.connect("conferencepaper.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM papers")
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# connect()

# #create a search function connect to the SQLite database
# def search(filename="",title="",keywords="",author="",year="",filepath=""): #=""pass in empty strings
#     conn = sql.connect("conferencepaper.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM papers WHERE filename=? OR title=? OR keywords=? OR author=? OR year=? OR filepath=?", 
#                 (filename,title,keywords,author,year,filepath))
#     rows = cur.fetchall()
#     conn.close()
#     return rows


#create a cursor instance
# def Cursor(conferencepaperDB):
#     c = conferencepaperDB.cursor()
#     c.execute("SELECT * FROM paper")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)
