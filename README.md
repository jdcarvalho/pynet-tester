# pynet-tester

This script use Speedtest software to create a database with Internet speed test data and export it for analysis

Main creator: Joao Dias de Carvalho Neto. joao.carvalho <at> maestrus.com


# Installation

Create an empty python3 virtualenv environment with:

    virtualenv ENV_NAME -p python3

activate it with
    
    source ./ENV_NAME/bin/activate

install all dependecies:

    pip install -r requirements.txt

Usage:

On source directory execute:

    python pynet-tester --list
    
Get your best server and check internet speed

    python pynet-tester --check SERVER_ID

A database will be created to store the results, you can export it to CSV file with

    python pynet-tester --export YYYY-MM-DD
