import sqlite3 as sql


#create a class object, function nested in python class.
class backend():
    def __init__(self,title,keywords,author,year,rows,SEARCH):
        self.title = title
        self.keywords = keywords
        self.author = author
        self.year = year
        self.SEARCH = SEARCH
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
    
# #create a search function connect to the SQLite database
    def search(self,title="",keywords="",author="",year="",rows=""): #=""pass in empty strings
        if self.SEARCH.get() != "":
            # search_title = self.search_title_var.get()
            # search_keywords = self.search_keywords_var.get()
            # search_author = self.search_author_var.get()
            # search_year = self.search_year_var.get()
            
            
            self.conn = sql.connect("C:\Findr\Tkinter_App\DB_Folder\conferencefile.db")
            print(self.conn)
            self.cur = self.conn.cursor()
            print(self.cur)
            self.cur.execute("""SELECT * FROM papers WHERE title LIKE ? 
                                OR keywords LIKE ? OR author LIKE ? 
                                OR year LIKE ?""",
                                ('%' + str(self.SEARCH()) + '%', '%' + str(self.SEARCH()) + '%',
                                '%' + str(self.SEARCH()) + '%', '%' + str(self.SEARCH()) + '%')
                        (title,keywords,author,year))
            rows = self.cur.fetchall()
            self.conn.close()
            return rows
