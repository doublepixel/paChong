from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import requests
from bs4 import BeautifulSoup
import re

from fontTools.ttLib import TTFont  # pip install fontTools
from io import BytesIO

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}


# 发送请求
def request(url):
    print(url)
    response = requests.get(url=url, headers=headers)
    return response


# 发起字体请求
def get_font(url):
    response = requests.get(url)
    font = TTFont(BytesIO(response.content))
    cmap = font.getBestCmap()
    font.close()
    return cmap


# 字体转小写
def get_encode(cmap, values):
    WORD_MAP = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9', 'period': '.'}
    word_count = ''
    for value in values.split(';'):
        value = value[2:]
        key = cmap[int(value)]
        word_count += WORD_MAP[key]
    return word_count


def parse(response):
    soup = BeautifulSoup(response.text, 'lxml')
    li_list = soup.select('.all-img-list li')
    results = []
    for index, li in enumerate(li_list):
        title = li.select('h4')[0].get_text()
        print(title)
        author = ",".join([a.get_text() for a in li.select('.author a')])
        status = li.select('.author span')[0].get_text()
        intro = "".join([a.get_text().replace(" ", "") for a in li.select('.intro')])
        src = li.select('.book-img-box img')[0].attrs['src']
        pattern = re.compile(r"<style>.*?font-family:(.*?);", re.S)
        font_urls = re.findall(pattern, response.text)
        font_full_url = 'https://qidian.gtimg.com/qd_anti_spider/' + font_urls[0].lstrip() + '.ttf'
        print(font_full_url)
        pattern1 = re.compile('<span.*?class="{}">(.*?)</span>'.format(font_urls[0].lstrip()), re.S)
        result = re.findall(pattern1, response.text)
        d = {
            'title': title,
            'author': author,
            'status': status,
            'intro': intro,
            'src': src,
            'font_full_url': font_full_url,
            'num': result[index][:-1],
        }
        results.append(d)
        # cmap = get_font(font_full_url)
        #

        # num = get_encode(cmap, result[index][:-1])
        # print(title, num)
    return results


def main():
    url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page='
    with ThreadPoolExecutor(max_workers=28) as executor:
        url_list = []
        for i in range(1, 2):
            full_url = url + str(i)
            url_list.append(full_url)
        future = executor.map(request, url_list)  # map 返回的结果顺序是一样的
        for result in future:
            # print(result)
            results = parse(result)  # 返回解析的结果
            font_urls = [i['font_full_url'] for i in results]
            print(font_urls)
            future = executor.map(get_font, font_urls)  # 字体对应的数据有了

            for index, res in enumerate(future):
                count = get_encode(res, results[index]['num'])  # 解析字体
                results[index]['num'] = count
            print(results)
    # with ThreadPoolExecutor(max_workers=28) as executor:  submit返回的结果顺序不一样
    #     future_list = []
    #     for i in range(1, 11):  # 一共发起10也
    #         full_url = url + str(i)
    #         future = executor.submit(request, full_url)
    #         future_list.append(future)
    #     for res in as_completed(future_list):
    #         print(res.result())


if __name__ == '__main__':
    main()
