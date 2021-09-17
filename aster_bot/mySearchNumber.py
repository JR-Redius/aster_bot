import myConnect
from pymysql import cursors
def getSearchNumber(phone_number):
    list_number =[]
    sql = 'SELECT extension FROM users;'
    connection = myconsql.getConnection()
    cursor = connection.cursor()
    cursor.execute(sql)
    for id in cursor:
        list_number.append(id['extension'])
    
    if list_number.count(str(phone_number)):
        cursor.execute('SELECT extension , name, password FROM users WHERE extension="'+str(phone_number)+'";')
        return cursor.fetchone()
    else:
        return ('Номер не найден')