#PyGit

#Dependencies 

* Python 2.7 
* Sqlite3 

#installing dependencies 

* You can download Python from here https://www.continuum.io/downloads 
* Sqlite3 can be installed via terminal command 


<h4> Linux </h4> 
<h6> sudo apt-get install sqlite3 


<h4> Mac OSX </h4> 

<p> Download sqlite-autoconf-*.tar.gz from http://www.sqlite.org/download.html 

<h6> 
<p>tar xvfz sqlite-autoconf-3071502.tar.gz
<p>cd sqlite-autoconf-3071502
<p>./configure --prefix=/usr/local
<p>make
<p>make install
</h6> 


#How to use 
* python create_db.py 
* touch .commit
* touch .fname 

* ./pg init project_name Language
* ./pg commit Commit here 
* ./pg guide for more info
* ./pg clone to clone  
* ./pg clone vers to get the version 
* ./pg get_vers to get all versions
* ./pg change project_name to change to other project
* ./pg proj to see currently selected project 
* ./pg ls to list project on database 


#Bugs 

* install.sh working , but lead us to the following erros 
* Database not working outsite the project file 
* .commin and .fname cant be change outsite tho project file 
* Uninstall.sh not working proprely. 
