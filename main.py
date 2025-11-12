import psycopg2

creds = {
    'host': 'localhost',
    'database': 'this_does_not_exist',
    #'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    #'client_encoding': 'WIN1252',
    #'client_encoding': 'CP1252',
    #'client_encoding': 'UNICODE',
}

def main():
    # dummy database on localhost
    try:
        with psycopg2.connect(
            **creds
        )as conn:
            print("Connected to database!")
            with conn.cursor() as cursor:
                cursor.execute('SELECT 1') # just to do something
                #cursor.execute('SELECT * FROM table_that_does_not_exist LIMIT 1') # trigger error message   
                print(cursor.fetchone())
    except psycopg2.OperationalError:
        print("OK: Expected error -  does not exist")
    except Exception:
        print("Failed to connect to database")
        import traceback
        traceback.print_exc()
        return


if __name__ == "__main__":
    main()
