import psycopg2

creds = {
    'host': 'localhost',
    'database': 'this_does_not_exist',
    #'database': 'this_does_not_exist',
    'user': 'postgres',
    'password': 'postgres'
}

def to_url(creds):
    return f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}/{creds['database']}"

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
    except Exception:
        print("Failed to connect to database")
        import traceback
        traceback.print_exc()
        return


if __name__ == "__main__":
    main()
