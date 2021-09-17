import pymysql.cursors

def getConnection():
    connection = pymysql.connect(
        host = '127.0.0.1',
        user = 'jred',
        password = 'A912n157tno',
        db = 'asterisk',
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection