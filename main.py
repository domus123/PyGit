import sys 
import functions as fc

def main() :
    str_input =""
    while (True) :
        str_input = raw_input("- ")
        splt = str_input.split()
        if splt[1] == 'exit' :
            print "Bye"
            break
        else :
            parser(splt)


def parser(splited_str):

    opc = splited_str[1]
    if (opc == 'init'):
        try: 
            fc.init(splited_str)
        except :
            print "Faltando linguagem"
    elif (opc == 'getfile'):
        try:
            fc.get_file(splited_str[2])
        except :
            print "Faltando nome do arquivo" 
    elif (opc == 'change'):
        fc.cng(splited_str)
    elif (opc == 'commit'):
        fc.commit(splited_str)
    elif (opc == 'ls') :
        fc.ls()
    elif (opc == 'get'):
        fc.get(splited_str[2])
    elif (opc == 'add'):
        fc.add(splited_str)
    elif (opc == 'pull'):
        print fc.pull()
    elif (opc == 'push'):
        print fc.push(splited_str)
    elif (opc == 'proj'):
        print fc.get_proj()
    elif (opc == 'guide'):
        guide()
    else :
        print "Invalid option"
    
def guide():
    print "'pg init Project_name Language' to start a new project"
    print "'pg commit comments' to add a comment to your commit"
    print "'pg add fileName' to add a fileName to the currently selected project"
    print "'pg add * ' to add all local files to the currently selected project"
    print "'pg proj' to see currently selected project"
    print "'pg pull' to list all projects"
    print "'pg getfile fileName' to get the text inside the file " 
    print "'pg change project_name' to change to the selected project"
    print "'pg get project_name' to see all project files"
    print "'pg ls' list local directorys"
    print "'pg exit' to leave python-git system"


#Todo list
#Add clone, so you can download all the files from the database
#add update, will keep the number of changes in the file and update the code into the database 
#String filter , will read the code and print it right 


if __name__ == '__main__':
    print "Welcome to PythonGit 0.01 (Pg.sys 0.01)"
    print "pg guide -- To show commands"
    print "pg exit to quit"
    main()
