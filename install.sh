#!/bin/bash

echo "Creating database ....."
sqlite3 pg.db < .sqlite3script
chmod 777 pg.db

echo "Creating .pygit file"
mkdir ~/.pygit

echo "Creating .commit ....."
touch ~/.pygit/.commit

echo "Creating .fname ....."
touch ~/.pygit/.fname

sudo mv pg.db ~/.pygit/

#mv pg.py pg
sudo chmod 777 src/pg
sudo cp src/pg /usr/local/bin/
sudo chmod 777 src/functions.py
sudo cp src/functions.py /usr/local/bin/


echo ""
echo "Pygit 0.02"
echo "pg guide for more info"

