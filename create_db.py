import sqlite3 



class create_db():
    
    def __init__ (self): 
        self.conn = sqlite3.connect('pg.db') 
        self.c = self.conn.cursor()
        self.create_projects()
        self.create_arquivo()
        self.conn.commit()
        self.conn.close()
        
    def create_projects(self):
        self.c.execute('CREATE TABLE projects (nome text PRIMARY KEY, linguagem TEXT)')
 
    def create_arquivo(self): 
        self.c.execute('CREATE TABLE arquivo (date DATETIME,vers int,projeto text, arqname text ,comentario text, codigo text, foreign key (projeto) references projects(nome))')


if __name__ == '__main__': 
    db_ = create_db() 
    
