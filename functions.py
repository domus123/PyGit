import sqlite3 
import os 

comment = ""
project_name = ""
add = []


def get_proj():
    global project_name
    if project_name == "":
        return "Nenhum projeto selecionado"
    else:
        return "Dir atual: " +  project_name

def init (lst):
    
    global project_name
    name = lst[2]
    lang = lst[3]
    proj = new_project(name,lang)
    project_name = name
    
def commit (lst):
    size = len(lst)
    global comment
    comment = ""
    for i in xrange(2,size):
        comment += lst[i] + " "
    return comment

def get_file(file_name):
    global project_name
    conn = sqlite3.connect('pg.db')
    c = conn.cursor()
    c.execute('SELECT codigo FROM arquivos WHERE projeto = ? AND arqname = ?', (project_name,file_name,))
    
    l = c.fetchall()
    if l == [] :
        print "Arquivo nao encontrado no projeto"
        print "OU"
        print "Projeto selecionado nao existente"
    else:    
        print l 
    conn.close()

def get(project_name):
    conn = sqlite3.connect('pg.db')
    c = conn.cursor()
    c.execute('SELECT arqname FROM arquivos where projeto = ?', (project_name,))
    lst = c.fetchall()
    if lst == [] :
        print "Nao encontrado projeto com este nome"
    else:
        for item in lst :
            print item[0]
    conn.close()

def cng(lst):
    global project_name
    try:
        project_name = lst[2]
        print "Projeto selecionado " + project_name
    except :
        print "Erro"
        
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
        print "Nome:" + item[0] + " Linguagem:" + item[1]
    conn.close()
    return True

    
def push(str):
    name = str[2]
    return "pushing to ... " + name 


#Create now project class
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
           print self.name + " criado com sucesso"
       except :
           print "Erro!! Projeto ja existente"
           self.conn.close()
                    
        
class add_file():
    def __init__(self,f_name):
        self.connect_db()
        self.list = False
        self.f_name = f_name
        self.osc = os_manager()
    
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
        global project_name 
        self.cur.execute("SELECT * FROM arquivos WHERE arqname = ? AND projeto = ?",(f_name,project_name,))
        if self.cur.fetchone() :
            return True
        else :
            return False 
        

    def insert_db(self,f_name):
        global project_name
        global comment
        
        if self.exist(f_name):
            print "Arquivo " + self.f_name + " ja existente"
        else : 
            text = self.read_file(f_name)
            if text != False:
                self.cur.execute("INSERT INTO arquivos (projeto,arqname,comentario,codigo) VALUES (?,?,?,?)", (project_name,f_name,comment,text,))
                print "Sucessfull added " + f_name + " to " + project_name
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

class os_manager():
    def __init__(self):
        self.path = os.getcwd()
    def get_files(self):
        return os.listdir(self.path)
