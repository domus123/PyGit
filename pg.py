#!/usr/bin/env python

import sys 
import functions as fc


def guide():
    print "'pg init Project_name Language' to start a new project"
    print "'pg commit comments' to add a comment to your commit"
    print "'pg add fileName' to add a fileName to the currently selected project"
    print "'pg add * ' to add all local files to the currently selected project"
    print "'pg proj' to see currently selected project"
    print "'pg pull' to list all projects"
    print "'pg getfile fileName' to get the text inside the file " 
    print "'pg get_vers to get all the commits made to the currently dir"
    print "'pg change project_name' to change to the selected project"
    print "'pg get project_name' to see all project files"


def parser(args):

    try:
        args_len = len(args) 
        opc = args[1]
        if args_len == 1 : 
            print "Invalid input"
        if (opc == 'init'):
            try: 
                fc.init(args)
            except :
                pass
                    #print "Missing language"
                    
        elif (opc == 'getfile'):
            if args_len == 2 : 
                fc.get_file(args[2])
            else : 
                print "Missing file name"
        elif (opc == 'get_vers') : 
            fc.get_vers()
        elif (opc == 'clone') : 
            fc.pg_clone(args)
        elif (opc == 'change'):
            fc.cng(args)
        elif (opc == 'commit'):
            fc.set_commit(args,args_len)
        elif (opc == 'ls') :
            fc.ls()
        elif (opc == 'get'):
            fc.get(args[2])
        elif (opc == 'add'):
            fc.add(args)
        elif (opc == 'pull'):
            print fc.pull()
        elif (opc == 'push'):
            print fc.push(args)
        elif (opc == 'proj'):
            print fc.get_proj()
        elif (opc == 'guide'):
            guide()
        else :
            print "Invalid option"
    except:
        print "wrong number of arguments"


if __name__ == '__main__': 
    args = sys.argv
    parser(args)
