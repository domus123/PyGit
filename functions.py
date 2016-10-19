import sqlite3 
import os , sys , shutil
import random as rd 
import datetime as dt
import time 

add = []
home = os.environ['HOME']
db_path = home + "/.pygit/pg.db"
fname_path = home + "/.pygit/.fname"
commit_path = home + "/.pygit/.commit"


#Create a new project
#Get project name and language 
class new_project():

    def __init__ (self,name,linguagem):
        self.name = name
        self.ling = linguagem
        self.connect_db()
        self.create_project()
        
    def connect_db(self):
        global db_path
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def create_project(self):
        #try:
        
        self.cur.execute("INSERT INTO projects (nome,linguagem) VALUES (?,?)" ,(self.name,self.ling,))
        self.conn.commit()
        self.conn.close()
        print self.name + " sucessfull created"
        #except :
        #   print "Project already exist"
        #   self.conn.close()
                    
#Add files to the currently project
class add_file():
    def __init__(self,f_name):
        self.connect_db()
        self.list = False
        self.f_name = (f_name)
        self.osc = os_manager()
        self.vers = rand_vers()
        self.time = get_time()

    def connect_db(self):
        global db_path
        self.conn = sqlite3.connect(db_path)
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
        comment = get_commit()
        text = self.read_file(f_name)
        if text != False:
            self.cur.execute("INSERT INTO arquivo (date,vers,projeto,arqname,comentario,codigo) VALUES (?,?,?,?,?,?)", (self.time,self.vers,project_name,f_name,comment,text,))
            print "Sucessfull added " + f_name + " to " + project_name + " version:" + str(self.vers)
        else :
            pass
        

    def insert_file(self):
        if self.f_name == 'all':
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
        global db_path
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
    def close_db(self):
        self.conn.close() 
    def get_c (self):
        return self.c
    def get_conn(self): 
        return self.conn 


def get_project(): 

    global fname_path 
    file = open(fname_path, 'r')  #if the file doens't exist it will create
    name = file.read() 
    file.close()
    return name

def set_project(project_name): 
    global fname_path
    file = open(fname_path, 'w') 
    file.write(project_name)
    file.close

def get_commit():
    global commit_path
    file = open(commit_path, 'r+') 
    commit = ""
    for line in file : 
        commit += line
    file.close()
    return commit 

def set_commit(words,size) : 
    
    commit = ""
    global commit_path
    file = open(commit_path, 'w')
    for i in xrange(2,size):
        commit += words[i] + " "
    file.write(commit)
    file.close()
    
    
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
def pg_clone(lst): 
    try: 
        vers = lst[2]          
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
    cur = db_connect()
    c = cur.get_c()
    c.execute('SELECT DISTINCT vers,date FROM arquivo WHERE projeto = ? ORDER BY date DESC LIMIT 1 ',(project_name,))
    result = c.fetchone() 
    print "Vers:{0} Date:{1}".format(result[0],result[1])
    return result[0] #Version number
    

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

    name = lst[2]
    lang = lst[3]
    print "Name:", name
    print "Lang:", lang
   
    proj = new_project(name,lang)
    set_project(name)
   # except : 
   #     pass 

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

    global db_path
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT arqname FROM arquivo where projeto = ?', (project_name,))
    lst = c.fetchall()
    if lst == [] :
        print "Project not founded"
        print "OR"
        print "Empty project"
    else:
        for item in lst :
            print item[0]
    conn.close()

def cng(lst):
    
    try:
        project_name = lst[2]
        set_project(project_name)
        print "Selected project " + project_name
    except :
        print "Error"
        
def add  (lst):
    try:
        add_constr = add_file(lst[2])
        add_constr.insert_file()
    except: 
        print "Error adding files"


def ls():
    global db_path
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * FROM projects')
    lst = c.fetchall()
    for item in lst :
        print "Name:" + item[0] + " Language:" + item[1]
    conn.close()
    return True



