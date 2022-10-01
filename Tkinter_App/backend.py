import sqlite3 as sql


#create a class object, function nested in python class.
class backend():
    def __init__(self,title,keywords,author,year,rows):
        self.title = title
        self.keywords = keywords
        self.author = author
        self.year = year
        self.rows = rows

#View all data and connection to the database.
    def viewall(self):
        self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencefile.db")
        print(self.conn)
        self.cur = self.conn.cursor()
        print(self.cur)
        self.cur.execute("SELECT * FROM papers")
        rows = self.cur.fetchall()
        # for row in rows:
        #     print(row)
        self.conn.close()
        return rows
    
#create a search function connect to the SQLite database
    def search(self,search_title="",search_keywords="",search_author="",search_year=""): #=""pass in empty strings as value.
        
            
            self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencefile.db")
            print(self.conn)
            self.cur = self.conn.cursor()
            print(self.cur)
            
            self.cur.execute("""SELECT * FROM papers WHERE title LIKE %s
                                OR keywords LIKE %s OR author LIKE %s 
                                OR year LIKE %s""")
                            #     ('%' + search_title + '%', 
                            # '%' + search_keywords + '%', '%' + search_author + '%', 
                            # '%' + search_year + '%'))
            
            #self.cur.execute("select * from papers where title like '%Plant%' ", search_title)
            rows = self.cur.fetchall()
            print(rows)
            self.conn.close()
            return rows
