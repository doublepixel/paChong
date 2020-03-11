from selenium import webdriver
import time
import re


class DouBanSpider():
    def __init__(self):
        self.url = 'https://movie.douban.com/'
        self.driver = webdriver.Chrome(
            executable_path='/Users/xiaoyuan/Downloads/chromedriver'
        )

    def send_request(self):
        '''
        发起请求
        :return:
        '''
        self.driver.get(self.url)
        input = self.get_input()
        input.send_keys(self.kw)

        btn = self.get_btn()
        btn.click()

        while True:
            time.sleep(2)  # 睡2秒

            div_list = self.driver.find_elements_by_xpath('//div[@class="item-root"]')
            print(len(div_list))

            with open('douban.html', 'w') as f:
                f.write(self.driver.page_source)
            print(div_list)
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            for div in div_list[1:]:
                title = div.find_element_by_xpath('.//a[@class="title-text"]').text
                print(title)
                try:
                    rating = div.find_element_by_xpath('.//span[@class="rating_nums"]').text
                except Exception as e:
                    rating = 0

                pl = div.find_element_by_xpath('.//span[@class="pl"]').text
                '''
                pl = (155人评价)
                pl = '暂无评分'
                '''
                result = re.search('\d+', pl)
                if result:
                    pl = result.group()
                else:
                    pl = 0

                actor = div.find_element_by_xpath('.//div[@class="meta abstract_2"]').text
                print(title, rating, pl, actor)

            try:
                next = self.driver.find_element_by_class_name('next')
                next.click()
            except Exception as e:
                self.driver.quit()

    def get_input(self):
        '''
        获取input对象
        :return:
        '''
        input = self.driver.find_element_by_id('inp-query')
        return input

    def get_btn(self):
        btn = self.driver.find_element_by_class_name('inp-btn')
        return btn

    def start(self):
        self.kw = input('请输入关键字')
        # self.kw = '成龙'
        self.send_request()


if __name__ == '__main__':
    dbs = DouBanSpider()
    dbs.start()
