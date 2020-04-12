import mysql.connector, os

path = '/usr/bin/'
pwd_file = os.path.join(path, "dbpw.txt")


with open(pwd_file, 'r') as f:
    dbpwd = f.read().replace('\n', '')

def getData(dbSelect, dbFrom, conditons = ''):
    query = f'SELECT {dbSelect} FROM {dbFrom} {conditons}'
    cnx = mysql.connector.connect(
            host='localhost',
            database='babibot',
            user='babipoki',
            password=dbpwd
        )
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    if cursor.rowcount == 0:
        return 'No Results'
    else:
        return cursor.fetchall()[0]
    cursor.close()
    cnx.close()


def setData(table, setQuery, where):
    '''Set data of the database. First entry is the name of the table...'''
    query = f'UPDATE {table} SET {setQuery} WHERE {where}'
    cnx = mysql.connector.connect(
            host='localhost',
            database='babibot',
            user='babipoki',
            password=dbpwd
        )
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    cnx.commit()
    print(cursor.rowcount, "record(s) affected")
    cursor.close()
    cnx.close()