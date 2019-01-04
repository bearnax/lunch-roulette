import psycopg2

class DatabaseController(object):
    def __init__(self):
        pass

    def connect():
        """ Connect to PostgreSQL database server """

        try:
            return psycopg2.connect(
                dbname = os.environ['DATABASE_NAME'],
                user = os.environ['DATABASE_USER'],
                password = os.environ['DATABASE_PASSWORD'],
                host = ['DATABASE_HOST'],
                port = ['DATABASE_PORT']
            )

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_sql_data(query, *args):
        """ retrieve data from the postgresql database
        """

        sql = query
        search_data = (args)

        try:
            assert sql.count('%s') == len(args)
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql, search_data)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            print("SUCCESS: get_sql_data")
            return data

        except AssertionError:
            print("ERROR: get_sql_data(), wrong number of arguments")

    def post_sql_data(query, *args):
        """ insert data into the postgresql database
            This function can be used to post new data or delete data

            Post / Delete should be indicated in the db query

        """

        sql = query
        values = (args)

        try:
            assert sql.count('%s') == len(args)
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
            print("SUCCESS: post_sql_data")

        except AssertionError:
            print("ERROR: post_sql_data(), wrong number of arguments")
