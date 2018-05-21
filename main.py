import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passw0rd',
                             db='chris_example',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `test_data` (`first_name`, `last_name`, `some_other_data`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('steve', 'cirelli', 'some data'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `first_name`, `last_name`, `some_other_data` FROM `test_data`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
