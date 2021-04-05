import requests
import sys
import re

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)

    filename = url.split('/')
    filename = filename[-1] if not re.match('index', filename[-1]) else filename[-2]
    with open(f'website/{filename}.html', 'wb') as f:
        f.write(res.content)