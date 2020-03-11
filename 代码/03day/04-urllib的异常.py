import urllib.request
from urllib.error import HTTPError, URLError

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.baidu.com/search/error.html'

try:
    response = urllib.request.urlopen(url=url)
    print(response.status)
except HTTPError as error:
    print(error.code)
    print(error.reason)
    print(error.headers)
except URLError as error:
    print(error.reason)
