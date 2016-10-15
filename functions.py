import sqlite3 
import os , sys , shutil
import random as rd 
import datetime as dt
import time 

comment = ""
project_name = ""
add = []


#Create a new project
#Get project name and language 
class new_project():

    def __init__ (self,name,linguagem):
        self.name = name
        self.ling = linguagem
        self.connect_db()
        self.create_project()
        
    def connect_db(self):
        self.conn = sqlite3.connect("pg.db")
        self.cur = self.conn.cursor()

    def create_project(self):
       try:
           self.cur.execute("INSERT INTO projects (nome,linguagem) VALUES (?,?)",( self.name,self.ling,))
           self.conn.commit()
           self.conn.close()
           print self.name + " sucessfull created"
       except :
           print "Project already exist"
           self.conn.close()
                    
#Add files to the currently project
class add_file():
    def __init__(self,f_name):
        self.connect_db()
        self.list = False
        self.f_name = f_name
        self.osc = os_manager()
        self.vers = rand_vers()
        self.time = get_time()

    def connect_db(self):
        self.conn = sqlite3.connect("pg.db")
        self.conn.text_factory = str
        self.cur = self.conn.cursor()
            
    def read_file(self,f_name):
        str = ""
        try:
            file = open(f_name, 'r')
            for lines in file :  
                str += lines
            return str
        except :
            return False

    def exist(self,f_name):
        project_name = get_project() 
        self.cur.execute("SELECT * FROM arquivo WHERE arqname = ? AND projeto = ?",(f_name,project_name,))
        if self.cur.fetchone() :
            return True
        else :
            return False 
        

    def insert_db(self,f_name):
        project_name = get_project()
        global comment
        

        text = self.read_file(f_name)
        if text != False:
            self.cur.execute("INSERT INTO arquivo (date,vers,projeto,arqname,comentario,codigo) VALUES (?,?,?,?,?,?)", (self.time,self.vers,project_name,f_name,comment,text,))
            print "Sucessfull added " + f_name + " to " + project_name + " version:" + str(self.vers)
        else :
            pass
        

    def insert_file(self):
        if self.f_name == '*':
            for item in self.osc.get_files():
                self.insert_db(item) 
        else :
            self.insert_db(self.f_name)
        self.conn.commit()
        self.conn.close()


#Get dir file 
#get dir path 
class os_manager():
    def __init__(self):
        self.path = os.getcwd()
    def get_files(self):
        return os.listdir(self.path)
    def get_path(self): 
        return self.path 


#Connect to database 
#Just for avoid use a lot of the same 
class db_connect (): 
    def __init__(self): 
        self.conn = sqlite3.connect('pg.db')
        self.c = self.conn.cursor()
    def close_db(self):
        self.conn.close() 
    def get_c (self):
        return self.c
    def get_conn(self): 
        return self.conn 


def get_project(): 
    file = open('.fname', 'r+')  #if the file doens't exist it will create
    name = file.read() 
    file.close()
    return name

def change_project(project_name): 
    file = open('.fname', 'w+') 
    file.write(project_name)
    file.close

#Get the file list
#Create a directory with the project name
#And copy all files from database to local directory
def write_clone(file_lst): 
    project_name = get_project()
    osc = os_manager() 
    path = osc.get_path() + "/" + project_name
    try: 
        os.mkdir(path, 0755)
    except : 
        print "Directory founded,deleting it and cloning the new one"
        shutil.rmtree(path) 
        os.mkdir(path, 0755) 
        time.sleep(0.5)

    for item in file_lst: 
        arq_path = path + "/" + item[0] 
        try: 
            code = item[1]
            with open(arq_path, "w") as text_file: 
                text_file.write(code)
                text_file.close()
                print "Cloning ... " + item[0]
        except: 
            print "Could not write " + item[0]

#Get the version passed by the clone function
#Fetch all the matches in database (filename,code) 
#Send to write_clone() 
def clone_query(vers) : 
    cur = db_connect()
    cur.conn.text_factory = str
    c = cur.get_c()
    c.execute('SELECT arqname,codigo FROM arquivo WHERE vers = (?)',(vers,))
    
    result = c.fetchall() 
    write_clone(result) 
    
#Parse the version 
#If none is passed it will clone the last one
#If one is passed it will clone it 
def pg_clone(str): 
    try: 
        trs = str[2]          
        vers = trs
    except: 
        vers = get_last() 
    clone_query(vers)

#Get local time 
#used for insert db 
def get_time() : 
    t = dt.datetime.now() 
    str = "{0}-{1}-{2} {3}:{4}:{5}".format(t.year , t.month , t.day, t.hour , t.minute , t.second)
    return str

#Get last version of the project 
def get_last(): 
    project_name = get_project()
    project_name = "teste2"
    cur = db_connect()
    c = cur.get_c()
    c.execute('SELECT DISTINCT vers,date FROM arquivo WHERE projeto = ? ORDER BY date DESC LIMIT 1 ',(project_name,))
    result = c.fetchone() 
    last = result[0] 
    print "Vers:{0} Date:{1}".format(result[0],result[1])
    return last
get_last()

#Get all the versions and commit from project 
def get_vers(): 
    project_name = get_project()
    cur = db_connect()
    c = cur.get_c()
    c.execute('SELECT DISTINCT vers,comentario,date FROM arquivo WHERE projeto= ? ORDER BY date DESC', (project_name,))
    result = c.fetchall()
    for item in result: 
        print "Vers:" + str(item[0]) + " Commit:" + item[1] + " Date:" + item[2]
    cur.close_db()     


#Generate a random number between  0 100000
def rand_vers() : 
    return rd.randrange(0,100000)


def get_proj():
    project_name = get_project()
    if project_name == "":
        return "No project sellected"
    else:
        return "Actual dir: " +  project_name

#Initialize a new project 
def init (lst):    
    project_name = get_project()
    name = lst[2]
    lang = lst[3]
    proj = new_project(name,lang)
    project_name = name

#Create a commit     
def commit (lst):
    size = len(lst)
    global comment
    comment = ""
    for i in xrange(2,size):
        comment += lst[i] + " "
    return comment

def get_file(file_name):
    project_name = get_project()
    cur = db_connect()
    c = cur.get_c()
    c.execute('SELECT codigo FROM arquivos WHERE projeto = ? AND arqname = ?', (project_name,file_name,))
    l = c.fetchall()
    if l == [] :
        print "File not founded"
        print "OR"
        print "Selected project not founded"
    else:    
        return l 
    cur.close_db()

def get(project_name):
    conn = sqlite3.connect('pg.db')
    c = conn.cursor()
    c.execute('SELECT arqname FROM arquivos where projeto = ?', (project_name,))
    lst = c.fetchall()
    if lst == [] :
        print "Project not founded"
    else:
        for item in lst :
            print item[0]
    conn.close()

def cng(lst):
    project_name = get_project()
    try:
        project_name = lst[2]
        print "Sellected project " + project_name
    except :
        print "Error"
        
def add  (lst):
    add_constr = add_file(lst[2])
    add_constr.insert_file()

def ls ():
    osc = os_manager()
    for item in osc.get_files():
        print item
        
def pull():
    conn = sqlite3.connect('pg.db')
    c = conn.cursor()
    c.execute('SELECT * FROM projects')
    lst = c.fetchall()
    for item in lst :
        print "Name:" + item[0] + " Language:" + item[1]
    conn.close()
    return True

    
def push(str):
    name = str[2]
    return "pushing to ... " + name 


