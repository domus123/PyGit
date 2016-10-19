#PyGit

#Dependencies 

* Python 2.7 
* Sqlite3 

#installing dependencies 

* You can download Python from [HERE](https://www.continuum.io/downloads)
* Sqlite3 can be installed via terminal command 


<h4> Linux </h4> 
```bash
   sudo apt-get install sqlite3 
```

<h4> Mac OSX </h4> 

<p> Download sqlite-autoconf-*.tar.gz from [HERE](http://www.sqlite.org/download.html)

```bash
 
   tar xvfz sqlite-autoconf-3071502.tar.gz
   cd sqlite-autoconf-3071502
   ./configure --prefix=/usr/local
   make
   make install
 
```

#How to use

```bash
   sudo sh ./install.sh

   pg                  #To open menu
   pg --version        #To get version


   pg init project_name Language        #Create a new project
   pg commit comment                    #Set tho commit comment that will be added to this version
   pg guide                             #Show guide menu
   pg clone                             #Clone files from currently project db to local folder
   pg clone vers                        #Get a specific vers of the currently project
   pg get_vers                          #Get all commits made to the curretly project
   pg change project_name               #Change working project
   pg proj                              #Show currently project
   pg ls                                #List all projects 
```

#Bugs 

* Any bug please contact me


#Todo

*  Add folders to project database
*  Show all files that have changed


#What it can do

* Save file into a local database and clone any version from the same db .
* Save multiple projects
* Save multiple project versions
