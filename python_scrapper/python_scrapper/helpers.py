import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_warnings(url):
    station_warnings = []

    try:
        page = requests.get(url)
    except requests.exceptions.RequestException:
        print("Unable to get content.")
        return station_warnings

    content = BeautifulSoup(page.content, 'html.parser')
    tables = content.find_all("tr")

    for row in tables:
        cells = row.find_all("td")
        if cells[0].get_text().endswith("see"):
            warning = (cells[0].get_text(), cells[1].get_text())
            station_warnings.append(warning)

    return station_warnings

def get_current_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")




