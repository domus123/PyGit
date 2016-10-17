#!/bin/bash

echo "Creating database ....."
python create_db.py

echo "Creating .commit ....."
touch .commit

#echo "Coping .commit ...."
#sudo cp .commit /usr/local/bin

echo "Cheating .fname ....."
touch .fname

#echo "Coping .fname ....."
#sudo cp .fname /usr/local/bin

#mv pg.py pg
sudo cp pg /usr/local/bin 

sudo cp functions.py /usr/local/bin
#sudo cp pg.db /usr/local/bin


echo ""
echo "Pygit 0.01"
echo "pg guide for more info"

