import logging

from helpers import (
    add_warnings_sql,
    finalize_database,
    get_current_time,
    get_warnings,
    get_webcam,
    init_database,
    time_no_whitespace,
)


def main():
    warn_url = "https://zh.stwarn.ch/"
    cam_url = "https://rcz.ch/custom/webcam/snap_med001M.jpg"
    warnings = get_warnings(warn_url)

    unterer_zurichsee = list(filter(lambda x: x[0] == "Unterer Zürichsee", warnings))[0]

    cnx, cur = init_database()
    date = get_current_time()
    save_webcam = "/data/webcam/{}.jpg".format(time_no_whitespace(date))
    get_webcam(cam_url, save_webcam)
    logging.info("scraping {} at time {}".format(warn_url, date))
    field = unterer_zurichsee + (date, save_webcam)
    print(field)
    cur.execute(add_warnings_sql.format(*field))

    logging.info("writing 1 entry to database")
    cnx.commit()

    finalize_database(cnx, cur)


if __name__ == "__main__":
    main()
