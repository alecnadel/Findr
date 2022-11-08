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
        
            #'?' is a placehold for SQLite DB, '%s' is a placeholder for MySQL database.
            self.conn = sql.connect("C:\\Findr\\Tkinter_App\\DB_Folder\\conferencefile.db")
            print(self.conn)
            self.cur = self.conn.cursor()
            print(self.cur)
            #self.cur.execute("SELECT * FROM papers WHERE title LIKE '%s' OR keywords LIKE '%s' OR author LIKE '%s' OR year = '%s' ;" %(title, keywords, author, year,))
            sqlstr="SELECT * FROM papers WHERE true" #true means you do not need to change anything if no other WHERE conditions applied.
            paramslist=[]
            if title != "":
                titlesrch="%"+title.lower()+"%"
                paramslist.append(titlesrch)
                sqlstr=sqlstr+" AND title LIKE ?"
            if keywords != "":
                keywordssrch="%"+keywords.lower()+"%"
                paramslist.append(keywordssrch)
                sqlstr=sqlstr+" AND keywords LIKE ?"
            if author != "":
                authorsrch="%"+author.lower()+"%"
                paramslist.append(authorsrch)
                sqlstr=sqlstr+" AND author LIKE ?"
            if year != "":    
                paramslist.append(year)
                sqlstr=sqlstr+" AND year = ?"
            sqlstr=sqlstr+";"
            print(sqlstr)
            params=tuple(paramslist)
            print(params)
            
            if len(params)==0:
                self.cur.execute(sqlstr)
            else:
                self.cur.execute(sqlstr,params)
                
            rows = self.cur.fetchall()
            #print(len(rows))
            #print(rows)
            self.conn.close()
            return rows
