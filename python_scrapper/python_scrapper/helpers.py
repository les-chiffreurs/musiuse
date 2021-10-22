import requests
import requests.exceptions
from bs4 import BeautifulSoup


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




