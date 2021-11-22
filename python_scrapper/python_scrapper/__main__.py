from helpers import (
    add_warnings_sql,
    finalize_database,
    get_current_time,
    get_warnings,
    init_database,
)


def main():
    url = "https://zh.stwarn.ch/"
    warnings = get_warnings(url)

    cnx, cur = init_database()
    date = get_current_time()
    field = [w + (date,) for w in warnings]
    for f in field:
        print(add_warnings_sql.format(*f))
        cur.execute(add_warnings_sql.format(*f))

    cnx.commit()

    finalize_database(cnx, cur)


if __name__ == "__main__":
    main()
