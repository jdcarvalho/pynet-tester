# pynet-tester

This script uses Speedtest software to create a database with Internet speed test data and export it for further analysis

Main creator: Joao Dias de Carvalho Neto. joao.carvalho at maestrus.com

Script simples para gerar uma base de dados sqlite com testes de download e upload de internet. Funciona baseado no speedtest-cli feito em Python. Basicamente uma forma de manter registros de tempos em tempos de velocidade de download e upload a fim de poder provar o quanto nossas operadoras de TELECOM precisam melhorar nos serviços prestados :/


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

    python pynet-tester.py --list
    
Get the best server ID (usually the closest to you) and check internet speed with this command:

    python pynet-tester.py --check SERVER_ID

A database will be created to store the results named speed.db, you can export the data to CSV file with this command

    python pynet-tester.py --export YYYY-MM-DD
