import logging
import urllib
from datetime import datetime

import mysql.connector
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

# initialize "warnings" table
create_warning_table_sql = """
CREATE TABLE IF NOT EXISTS warnings
(
    warn_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    location VARCHAR(255) NOT NULL,
    warning VARCHAR(255) NOT NULL,
    time DATETIME NOT NULL,
    webcam VARCHAR(255)
)
"""

# add warnings to table
add_warnings_sql = """
INSERT into warnings
VALUES (NULL, "{}", "{}", "{}", "{}")
"""


def get_warnings(url):
    station_warnings = []

    try:
        page = requests.get(url)
    except requests.exceptions.RequestException:
        print("Unable to get content.")
        return station_warnings

    content = BeautifulSoup(page.content, "html.parser")
    tables = content.find_all("tr")

    for row in tables:
        cells = row.find_all("td")
        if cells[0].get_text().endswith("see"):
            warning = (cells[0].get_text(), cells[1].get_text())
            station_warnings.append(warning)

    return station_warnings


def get_webcam(url, target):
    logging.info("downloading {} to {}".format(url, target))
    urllib.request.urlretrieve(url, target)


def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def time_no_whitespace(time):
    t = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return t.strftime("%Y-%m-%d_%H-%M-%S")


def init_database():
    logging.info("connecting to mysql:3306...")
    cnx = mysql.connector.connect(
        user="root",
        password="fFZ37tuLPpGkHGZG",
        host="musiuse-db",
        port="3306",
        database="musiuse",
        charset="utf8",
    )
    cur = cnx.cursor()

    cur.execute(create_warning_table_sql)
    logging.info("successfully initialized database connection")

    return cnx, cur


def finalize_database(cnx, cur):
    cur.close()
    cnx.close()
