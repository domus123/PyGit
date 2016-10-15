#!/bin/bash

echo "Creating database ....."
python create_db.py
echo "Creating .commit ....."
touch .commit
echo "Cheating .fname ....."
touch .fname

echo ""
echo "Pygit 0.01"
echo "pg guide for more info"

