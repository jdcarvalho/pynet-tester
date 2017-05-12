from speedtest import Speedtest
from datetime import datetime
import sqlite3
import os, sys, getopt, csv


HELP = """
    This script use Speedtest software to create a database with Internet speed test data and export it for analysis
    Main creator: Joao Dias de Carvalho Neto. joao.carvalho <at> maestrus.com
    
    Usage:
    
    * Show this help message: "pynet-tester --help" o "pynet-tester -h"
    * To list all disponible servers: "pynet-tester --list" or "pynet-tester -l"
    * Check Internet Speed: "pynet-tester --check SERVER_ID" or "pynet-tester --c SERVER_ID".
    * Export results: "pynet-tester --export YYYY-MM-DD" or "pynet-tester -e YYYY-MM-DD"

"""

def list_servers():
    s = Speedtest()
    print(s.get_servers())

def check_speed(default_server):
    s = Speedtest()
    try:
        if default_server:
            s.get_servers([default_server])
        else:
            s.get_servers()
        print('Starting test...')
        server = s.get_best_server()
        v_down = s.download()
        v_uplo = s.upload()
    except:
        server = 'Server Offline'
        v_down = 0
        v_uplo = 0

    db = sqlite3.connect('speed.db')
    c = db.cursor()
    c.execute(' CREATE TABLE IF NOT EXISTS speed (date TIMESTAMP, provider text, d_speed real, u_speed real)')
    c.execute('INSERT INTO speed (date, provider, d_speed, u_speed) VALUES ("{0}", "{1}", {2}, {3})'.format(datetime.now(), server['sponsor'], v_down, v_uplo))
    db.commit()
    c.close()
    print('Done! :)')


def export_data(date):
    if not date:
        print('A export date needs to be inputed')
        sys.exit(2)
    
    try:
        d = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Export date is not in YYYY-MM-DD format')
        sys.exit(2)
        
    db = sqlite3.connect('speed.db')
    c = db.cursor()
    c.execute(' CREATE TABLE IF NOT EXISTS speed (date TIMESTAMP, provider text, d_speed real, u_speed real)')
    
    di = date + ' 00:00:00'
    df = date + ' 23:59:59'
    
    with open("{0}.csv".format(date), 'w', newline='', encoding='utf-8') as exp_file:
        w = csv.writer(exp_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        for row in c.execute('''
            select 
                `date`, 
                provider, 
                printf("%.2f", ((d_speed / 1024)/ 1024)) as download, 
                printf("%.2f", ((u_speed / 1024)/ 1024)) as upload 
            from 
                speed 
            where 
                `date` BETWEEN "{0}" AND "{1}" ORDER BY `date`
            '''.format(di, df)):
            d = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f" )            
            w.writerow([d.strftime('%d/%m/%Y %H:%M'), row[1], row[2], row[3] ])
            
    db.commit()
    c.close()

    
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hlc:e:",['help', 'list', 'check=', 'export='])
    except getopt.GetoptError:
        print("Argument invalid!, Please call --help for a complete list")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ['-h','--help']:
            print(HELP)
            sys.exit()
        if opt in ['-l','--list']:
            list_servers()
        elif opt in ("-c", "--check"):
            if arg:
                print('Testing server: {0}'.format(arg))
            check_speed(arg)
        elif opt in ("-e", "--export"):
            export_data(arg)
            sys.exit()
        else:
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
