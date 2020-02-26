import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports"

folder_location = 