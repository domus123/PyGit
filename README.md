#PyGit

#Dependencies 

* Python 2.7 
* Sqlite3 

#installing dependencies 

* You can download Python from here https://www.continuum.io/downloads 
* Sqlite3 can be installed via terminal command 


<h4> Linux </h4> 
```bash
   sudo apt-get install sqlite3 
```

<h4> Mac OSX </h4> 

<p> Download sqlite-autoconf-*.tar.gz from http://www.sqlite.org/download.html 

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


   pg init project_name Language
   pg commit Commit  
   pg guide             
   pg clone 
   pg clone vers
   pg get_vers
   pg change project_name
   pg proj 
   pg ls 
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
