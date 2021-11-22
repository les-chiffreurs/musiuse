from helpers import get_warnings, get_current_time, init_database, add_warnings_sql


def main():
    url = "https://zh.stwarn.ch/"
    warnings = get_warnings(url)

    con, cur = init_database()
    date = get_current_time()
    field = [w + (date,) for w in warnings]
    cur.executemany(add_warnings_sql, field)

    cur.execute("SELECT warning FROM warnings WHERE location='Unterer Zürichsee'")
    print(cur.fetchall())
    con.commit()
    con.close()
    

if __name__ == '__main__':
    main()
