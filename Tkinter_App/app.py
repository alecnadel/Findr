import tkinter as tk
from tkinter import Scrollbar, ttk
import ttkthemes
#import sqlite3 as sql
from backend import backend

class Engine(tk.Tk):
    def __init__(self):
        super().__init__() #initialize the tk.TK class
        self.title('Findr')
        self.style = ttkthemes.ThemedStyle()
        self.style.set_theme("breeze")
        self.iconbitmap('Dooffy-Characters-Q1.ico')
        self.withdraw()
        self.wm_state('zoomed') #create full screen window
        self.platform = self.tk.call('tk', 'windowingsystem')
        self.geometry("1200x800")
        self.resizable(False, False) #Width, Height
        
        # search fields variables
        self.search_filename_var = tk.StringVar()
        self.search_title_var = tk.StringVar()
        self.search_keywords_var = tk.StringVar()
        self.search_author_var = tk.StringVar()
        self.search_year_var = tk.StringVar()
        self.search_filepath_var = tk.StringVar()
        
        # window frames (items that nest in the frame)
        self.frm_main = ttk.Frame(self) #Refer to pack the main frame
        self.frm_top = ttk.Frame(self.frm_main) #Refer to pack the Toplevel widgets to the window
        
        self.frm_searchfilter = ttk.Frame(self.frm_top)
        self.frm_filename = ttk.Frame(self.frm_top)
        self.frm_title = ttk.Frame(self.frm_top)
        self.frm_keywords = ttk.Frame(self.frm_top)
        self.frm_author = ttk.Frame(self.frm_top)
        self.frm_year = ttk.Frame(self.frm_top)
        self.frm_filepath = ttk.Frame(self.frm_top)
        
        #Text title
        self.searchfilter_lbl = ttk.Label(self.frm_searchfilter, text='Search filters', width=30)
        self.frm_searchfilter.grid(row=2, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.searchfilter_lbl.pack(side=tk.LEFT)
        
        # search filename input
        self.filename_lbl = ttk.Label(self.frm_filename, text='Filename:', width=10)
        self.filename_entry = ttk.Entry(self.frm_filename, textvariable=self.search_filename_var, width=80)
        self.filename_entry.focus()

        #search title input
        self.title_lbl = ttk.Label(self.frm_title, text='Title:', width=10)
        self.title_entry = ttk.Entry(self.frm_title, textvariable=self.search_title_var, width=80)
        self.title_entry.focus()
        
        #search keywords input
        self.keywords_lbl = ttk.Label(self.frm_keywords, text='Keywords:', width=10)
        self.keywords_entry = ttk.Entry(self.frm_keywords, textvariable=self.search_keywords_var, width=80)
        self.keywords_entry.focus()
        
        #search author input
        self.author_lbl = ttk.Label(self.frm_author, text='Author(s):', width=10)
        self.author_entry = ttk.Entry(self.frm_author, textvariable=self.search_author_var, width=80)
        self.author_entry.focus()
        
        #search year input
        self.year_lbl = ttk.Label(self.frm_year, text='Year:', width=10)
        self.year_entry = ttk.Entry(self.frm_year, textvariable=self.search_year_var, width=80)
        self.year_entry.focus()
        
        #search filepath input
        self.filepath_lbl = ttk.Label(self.frm_filepath, text='Filepath:', width=10)
        self.filepath_entry = ttk.Entry(self.frm_filepath, textvariable=self.search_filepath_var, width=80)
        self.filepath_entry.focus()
        
        # add widgets to the window
        self.frm_top.pack(side=tk.TOP, fill=tk.X) #Toplevel widget in Tkinter, create a window on top of other windows
        
        self.frm_filename.grid(row=3, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.filename_lbl.pack(side=tk.LEFT)
        self.filename_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_title.grid(row=3, column=2, padx=6, pady=5, sticky=tk.NSEW)
        self.title_lbl.pack(side=tk.LEFT)
        self.title_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_keywords.grid(row=4, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.keywords_lbl.pack(side=tk.LEFT)
        self.keywords_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_author.grid(row=4, column=2, padx=6, pady=5, sticky=tk.NSEW)
        self.author_lbl.pack(side=tk.LEFT)
        self.author_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_year.grid(row=5, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.year_lbl.pack(side=tk.LEFT)
        self.year_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_filepath.grid(row=5, column=2, padx=6, pady=5, sticky=tk.NSEW)
        self.filepath_lbl.pack(side=tk.LEFT)
        self.filepath_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        
        self.frm_main.pack(fill=tk.BOTH, expand=tk.YES) #Pack main frame in Tkinter
        
        # form buttons
        self.btn_search = ttk.Button(self.frm_top, text='Search', command=self.searchall) #Show data from SQLite database data, add command function to search.
        self.btn_search.grid(row=6, column=0, ipadx=35, padx=15, pady=10, sticky=tk.W)
        self.btn_viewall = ttk.Button(self.frm_top, text='View All', command=self.viewall) #View all data from SQLite database.
        self.btn_viewall.grid(row=6, column=0, ipadx=35, padx=15, pady=10)
        self.btn_reset = ttk.Button(self.frm_top, text="Clear", command=self.clearall)#Reset the search form.
        self.btn_reset.grid(row=6, column=0, ipadx=35, padx=15, pady=10, sticky=tk.E)
        
        #configure columns and rows for resizes
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # search results show in Treeview
        self.tree = ttk.Treeview(self.frm_main)
        self.tree['columns'] = ('filename', 'title', 'keywords', 'author', 'year', 'filepath')
        self.tree.column('#0', width=0, stretch=tk.NO, anchor=tk.E) # hide the first column
        self.tree.column('filename', width=250, stretch=True, anchor=tk.E)
        self.tree.column('title', width=350, stretch=True, anchor=tk.E)
        self.tree.column('keywords', width=350, stretch=True, anchor=tk.E)
        self.tree.column('author', width=220, stretch=True, anchor=tk.E)  
        self.tree.column('year', width=100, stretch=True, anchor=tk.E) 
        self.tree.column('filepath', width=330, stretch=True, anchor=tk.E)
        self.tree.heading('#0', text='', anchor=tk.CENTER) # hide the first column.
        self.tree.heading('filename', text='filename', anchor=tk.CENTER)
        self.tree.heading('title', text='title', anchor=tk.CENTER)
        self.tree.heading('keywords', text='keywords', anchor=tk.CENTER)
        self.tree.heading('author', text='author', anchor=tk.CENTER)
        self.tree.heading('year', text='year', anchor=tk.CENTER)
        self.tree.heading('filepath', text='filepath', anchor=tk.CENTER) 
        # create a vertical scrollbar to the right of the treeview
        # tree_scroll = Scrollbar(self.frm_main, orient=tk.VERTICAL, command=self.tree.yview)
        # tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        # tree_scroll.config(command=self.tree.yview)
        # self.tree = ttk.Treeview(yscrollcommand=tree_scroll.set)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, anchor=tk.E) #Display search results in treeview widget.
        
        # right-click menu from Treeview widget
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label='Open file')
        self.menu.add_command(label='Export results to csv')
        
    
    #search all files
    def searchall(self):
        #self.tree.delete(0, tk.END)
        for file in backend.search():
            self.tree.insert('', tk.END, values=file)
            
    #clear all Entry inputs.
    def clearall(self):
        self.filename_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.keywords_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.filepath_entry.delete(0, tk.END)
    
    #view all data from the database.
    def viewall(self):
        print("view all")
        #self.tree.delete(0, tk.END)
        be = backend("filename","title","keywords","author","year","filepath","rows") #create backend objects
        for row in be.viewall():
            self.tree.insert('', tk.END, text=row[0], values=row[1:])
        
    # #search the files based on the entry inputs.
    # def render_search_result(self):
    #     # get search values
    #     search_filename = self.search_filename_var.get()
    #     search_title = self.search_title_var.get()
    #     search_keywords = self.search_keywords_var.get()
    #     search_author = self.search_author_var.get()
    #     search_year = self.search_year_var.get()
    #     search_filepath = self.search_filepath_var.get()
        
    #     # clear previous search results
    #     for i in self.tree.get_children():
    #         self.tree.delete(i)
        
    #     # search database
    #     self.conn = sql.connect("conferencepaper.db")
    #     self.cur = self.conn.cursor()
    #     self.cur.execute("""SELECT * FROM papers 
    #                         WHERE filename LIKE ? OR title LIKE ? 
    #                         OR keywords LIKE ? OR author LIKE ? 
    #                         OR year LIKE ? OR filepath LIKE ?""",
    #                         ('%' + search_filename + '%', '%' + search_title + '%', 
    #                         '%' + search_keywords + '%', '%' + search_author + '%', 
    #                         '%' + search_year + '%', '%' + search_filepath + '%'))
    #     rows = self.cur.fetchall()
    #     self.conn.close()
        
    #     # display search results
    #     for row in rows:
    #         self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    #         print(row)
   
        
       

           
if __name__ == '__main__':
    
    searching = False
    app = Engine()
    print("app")
    app.mainloop()