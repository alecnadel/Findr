import tkinter as tk
from tkinter import ttk, Scrollbar
import ttkthemes
#import sqlite3 as sql
from backend import backend

Scrollbar
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
        self.resizable(True, True) #Width, Height
        
        # search fields variables
        title_var = tk.StringVar()
        keywords_var = tk.StringVar()
        author_var = tk.StringVar()
        year_var = tk.StringVar()
        
        
        # window frames (items that nest in the frame)
        self.frm_main = ttk.Frame(self) #Refer to pack the main frame
        self.frm_top = ttk.Frame(self.frm_main) #Refer to pack the Toplevel widgets to the window
        
        self.frm_searchfilter = ttk.Frame(self.frm_top)
        self.frm_title = ttk.Frame(self.frm_top)
        self.frm_keywords = ttk.Frame(self.frm_top)
        self.frm_author = ttk.Frame(self.frm_top)
        self.frm_year = ttk.Frame(self.frm_top)
        
        #Text title
        self.searchfilter_lbl = ttk.Label(self.frm_searchfilter, text='Search filters', width=30)
        self.frm_searchfilter.grid(row=2, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.searchfilter_lbl.pack(side=tk.LEFT)

        #search title input
        self.title_lbl = ttk.Label(self.frm_title, text='Title:', width=10)
        self.title_entry = ttk.Entry(self.frm_title, textvariable=title_var, width=80)
        self.title_entry.focus()
        
        #search keywords input
        self.keywords_lbl = ttk.Label(self.frm_keywords, text='Keywords:', width=10)
        self.keywords_entry = ttk.Entry(self.frm_keywords, textvariable=keywords_var, width=80)
        self.keywords_entry.focus()
        
        #search author input
        self.author_lbl = ttk.Label(self.frm_author, text='Author(s):', width=10)
        self.author_entry = ttk.Entry(self.frm_author, textvariable=author_var, width=80)
        self.author_entry.focus()
        
        #search year input
        self.year_lbl = ttk.Label(self.frm_year, text='Year:', width=10)
        self.year_entry = ttk.Entry(self.frm_year, textvariable=year_var, width=80)
        self.year_entry.focus()
        
        
        # add widgets to the window
        self.frm_top.pack(side=tk.TOP, fill=tk.X) #Toplevel widget in Tkinter, create a window on top of other windows
        
        self.frm_title.grid(row=3, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.title_lbl.pack(side=tk.LEFT)
        self.title_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_keywords.grid(row=3, column=2, padx=6, pady=5, sticky=tk.NSEW)
        self.keywords_lbl.pack(side=tk.LEFT)
        self.keywords_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_author.grid(row=4, column=0, padx=6, pady=5, sticky=tk.NSEW)
        self.author_lbl.pack(side=tk.LEFT)
        self.author_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        self.frm_year.grid(row=4, column=2, padx=6, pady=5, sticky=tk.NSEW)
        self.year_lbl.pack(side=tk.LEFT)
        self.year_entry.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        
        
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
        
        
        self.yscrollbar = ttk.Scrollbar(self.frm_main, orient=tk.VERTICAL) #Vertical Scrollbar for Treeview
        self.xscrollbar = ttk.Scrollbar(self.frm_main, orient=tk.HORIZONTAL) #Horizontal Scrollbar for Treeview
        # search results show in Treeview
        self.tree = ttk.Treeview(self.frm_main)
        self.tree.configure(yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        self.yscrollbar.configure(command=self.tree.yview)
        self.xscrollbar.configure(command=self.tree.xview)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(selectmode="extended")
        self.tree['columns'] = ('title', 'keywords', 'author', 'year')
        self.tree['show'] = 'headings'
        
        self.tree.column('title', width=380, stretch=True, anchor=tk.W)
        self.tree.column('keywords', width=500, stretch=True, anchor=tk.W)
        self.tree.column('author', width=220, stretch=True, anchor=tk.W)  
        self.tree.column('year', width=10, stretch=True, anchor=tk.CENTER) 
        
        self.tree.heading('title', text='Title', anchor=tk.CENTER)
        self.tree.heading('keywords', text='Keywords', anchor=tk.CENTER)
        self.tree.heading('author', text='Author', anchor=tk.CENTER)
        self.tree.heading('year', text='Year', anchor=tk.CENTER)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, anchor=tk.NW) #Display search results in treeview widget.
        
        # create a vertical scrollbar to the right of the treeview
        
        
        
        # right-click menu from Treeview widget
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label='Open file')
        self.menu.add_command(label='Export results to csv')
        
    
    #search all files
    def searchall(self):
        title = self.title_entry.get()
        keywords = self.keywords_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        print(title, keywords, author, year)
        
        ce = backend("title", "keywords", "author", "year", "rows")
        self.tree.delete(*self.tree.get_children())
        for file in ce.search(title, keywords, author, year):
            self.tree.insert('', tk.END, values=file)
        
                
    #clear all Entry inputs.
    def clearall(self):
        self.title_entry.delete(0, tk.END)
        self.keywords_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
    
    
    #view all data from the database.
    def viewall(self):
        print("view all")
        self.tree.delete(*self.tree.get_children())
        be = backend("title","keywords","author","year","rows") #create backend objects
        for row in be.viewall():
            self.tree.insert('', tk.END, values=row)

           
if __name__ == '__main__':
    
    searching = False
    app = Engine()
    print("app")
    app.mainloop()