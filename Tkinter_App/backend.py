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
        self.conn = sql.connect("C:\\Findr\\Tkinter_App\\DB_Folder\\conferencefile.db")
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
    def search(self,title="",keywords="",author="",year=""): #=""pass in empty strings as value.
        
            
            self.conn = sql.connect("C:\\Findr\\Tkinter_App\\DB_Folder\\conferencefile.db")
            print(self.conn)
            self.cur = self.conn.cursor()
            print(self.cur)
            # query = f"SELECT * FROM papers WHERE title LIKE "%title%" OR keywords LIKE "%keywords%" OR author LIKE "%author%" OR year LIKE "%year%";"
            # self.cur.execute(query)
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE '%[A-Za-z]%' OR keywords LIKE '%[A-Za-z]%' OR author LIKE '%[A-Za-z]%' OR year LIKE '%[0~9]%'", (title,keywords,author,year))
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE 'a-z' OR keywords LIKE 'a-z'OR author LIKE 'a-z' OR year LIKE '0-9'", (title,keywords,author,year))
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE '[a-z]%' OR keywords LIKE '[a-z]%' OR author LIKE '[a-z]%' OR year LIKE '[0-9]%';", (title,keywords,author,year,))
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE %a% OR keywords LIKE %a% OR author LIKE %a% OR year LIKE %0-9%;" %(title,keywords,author,year,))
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE '%s' OR keywords LIKE '%s' OR author LIKE '%s' OR year LIKE '%s';" %(title,keywords,author,year,))
            myParam = '%s{}%s'.format(title or keywords or author or year)
            sqlQuery = "SELECT * from papers WHERE title LIKE ? OR keywords LIKE ? OR author LIKE ? OR year=?"
            self.cur.execute(sqlQuery, (myParam))
            rows = self.cur.fetchall()
            print(rows)
            self.conn.close()
            return rows
