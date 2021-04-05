import re
from utils import load_site_path
from config import siteurl
from bs4 import BeautifulSoup

pages = load_site_path(siteurl)

summary = list()
for page in pages:
    with open(page, 'r') as f:
        content = ''.join(f.readlines())
    
    soup = BeautifulSoup(content, 'html5lib')
    patients = soup.select('tbody tr')
    
    patients_detail = [
        row.select('td')
            for row in patients
    ]
    info = [
        (info[0].text, info[-1].text)
            for info in patients_detail
    ]

    info_parsed = [
        (int(re.sub('\D+', '', person)), list(set(int(re.sub('\D+', '', relative)) for relative in re.findall('[\D^]\d+例', relatives))))
            for person, relatives in info
    ]
    
    summary += info_parsed

pertain = dict(sorted(summary, key=lambda x: x[0]))

print(pertain)