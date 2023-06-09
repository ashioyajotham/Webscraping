#!/bin/bash

# This script downloads the velib dataset from the velib website
# and converts it to a csv file

# The script requires the following dependencies:
# - wget
# - csvkit
sudo apt-get update && sudo apt-get install -y wget
sudo pip install csvkit
# sudo command not found? Install pip with the following command:
# sudo apt-get install python-pip
DIR=$(dirname $0) # Get the directory of the script

# Download the dataset
wget https://opendata.paris.fr/explore/dataset/velib-disponibilites-en-temps-reel/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B -O $DIR/velib.csv

# Convert the dataset to csv
in2csv -I $DIR/velib.csv > $DIR/velib.csv

# Remove the original file
rm $DIR/velib.csv

# Rename the file
mv $DIR/velib.csv $DIR/velib.csv

# Remove the first line of the file
sed -i '1d' $DIR/velib.csv

# Remove the last line of the file
sed -i '$d' $DIR/velib.csv

# To run this script, run the following command:
# bash velib.sh