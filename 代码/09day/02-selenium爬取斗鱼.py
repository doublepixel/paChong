from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyecharts.charts import Bar, Page
from pyecharts import options as opts
import jieba
import wordcloud
from matplotlib import pyplot as plt


class DouYuSpider():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/xiaoyuan/Downloads/chromedriver'
        )
        self.url = 'https://www.douyu.com/g_LOL'

        self.data = {">200万": 0, ">150万": 0, ">100万": 0, ">50万": 0, ">30万": 0, ">10万": 0, ">1万": 0, "1万以下": 0}
        self.title = ""
        self.page = 1

    def send_request(self):
        self.driver.get(self.url)

        time.sleep(3)
        # 滑动底部

        while True:
            time.sleep(2)
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            hot_nums = self.driver.find_elements_by_css_selector('.DyListCover-hot')
            titles = self.driver.find_elements_by_css_selector('.DyListCover-intro')

            for info in zip(hot_nums, titles):
                num = info[0].text
                if "万" in num:
                    num = float(num.replace('万', "")) * 10000
                else:
                    num = int(num)

                if num >= 2000000:
                    self.data[">200万"] = self.data[">200万"] + 1
                elif num >= 1500000 and num < 2000000:
                    self.data[">150万"] = self.data[">150万"] + 1
                elif num >= 1000000 and num < 1500000:
                    self.data[">100万"] = self.data[">100万"] + 1
                elif num >= 500000 and num < 1000000:
                    self.data[">50万"] = self.data[">50万"] + 1
                elif num >= 300000 and num < 500000:
                    self.data[">30万"] = self.data[">30万"] + 1
                elif num >= 100000 and num < 300000:
                    self.data[">10万"] = self.data[">10万"] + 1
                elif num >= 10000 and num < 100000:
                    self.data[">1万"] = self.data[">1万"] + 1
                elif num >= 0 and num < 10000:
                    self.data["1万以下"] = self.data["1万以下"] + 1

                self.title += info[1].text
            # 获取下一页
            self.page += 1
            if self.page == 3:
                break
            next = self.driver.find_element_by_class_name('dy-Pagination-next')
            if next.get_attribute('aria-disabled') == 'false':
                next.click()
            else:
                break
        # 最后生成表格
        self.create_bar()
        # 词云
        self.create_wordcloud()

    def create_bar(self):
        c = Bar().add_xaxis(list(self.data.keys())).add_yaxis("斗鱼热度", list(self.data.values())).set_global_opts(
            title_opts=opts.TitleOpts(title="热度分析", subtitle="斗鱼"))
        Page().add(c).render()

    def create_wordcloud(self):
        # 中国 人民 共和国
        # 富婆 不行 太短
        words = list(jieba.cut(self.title))  # 分词
        fnl_words = [word for word in words if len(word) > 1]  # 去掉单字
        wc = wordcloud.WordCloud(width=1000, font_path='Fonts/font1.ttf', height=800)  # 设定词云画的大小字体，一定要设定字体，否则中文显示不出来
        wc.generate(' '.join(fnl_words))
        wc.to_file("danmu_pic.png")  # 保存
        # plt.imshow(wc)  # 看图

    def start(self):
        self.send_request()


if __name__ == '__main__':
    dys = DouYuSpider()
    dys.start()
