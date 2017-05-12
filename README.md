# pynet-tester

This script use Speedtest software to create a database with Internet speed test data and export it for analysis

Main creator: Joao Dias de Carvalho Neto. joao.carvalho at maestrus.com


# Installation

Clone this repository

    git clone https://github.com/jdcarvalho/pynet-tester.git

Create an empty python3 virtualenv environment with:

    virtualenv ENV_NAME -p python3

activate it with
    
    source ./ENV_NAME/bin/activate

install all dependecies:

    pip install -r requirements.txt

# Usage:

On the source directory execute this command to list all servers available:

    python pynet-tester --list
    
Get your best server and check internet speed with this command:

    python pynet-tester --check SERVER_ID

A database will be created to store the results named speed.db, you can export the data to CSV file with this command

    python pynet-tester --export YYYY-MM-DD
