from selenium import webdriver
import time
import pymysql

class MingzhengSpider(object):

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.db = pymysql.connect('localhost', 'root', '546524lk', 'spiderdb', charset='utf8')
        self.cursor = self.db.cursor()
        self.p_list = []
        self.c_list = []
        self.x_list = []

    def is_new(self):
        self.browser.get('http://www.mca.gov.cn/article/sj/xzqh/2019/')
        time.sleep(2)
        r_list = self.browser.find_elements_by_xpath('//a[@class="artitlelist"]')
        for r in r_list:
            if r.text.__contains__('代码'):
                sel = 'select * from version where link="{}"'.format(r.text)
                self.cursor.execute(sel)
                if self.cursor.fetchall():
                    print('数据已是最新,无需重新爬取')
                    break
                else:
                    r.click()
                    title = r.text
                    time.sleep(2)
                    all_handles = self.browser.window_handles
                    self.browser.switch_to_window(all_handles[1])
                    self.write_data()
                    ins = 'insert into version values (%s)'
                    self.cursor.execute(ins, [title])
                    self.db.commit()
                    break
    def write_data(self):
        r_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for r in r_list:
            code = r.find_element_by_xpath('./td[2]').text.strip()
            name = r.find_element_by_xpath('./td[3]').text.strip()
            print(name, code)
            if code[2:] == '0000':
                self.p_list.append([name, code])
            elif code[-2:] == '00':
                self.c_list.append([name, code, code[:2]+'0000'])
            else:
                self.x_list.append([name, code, code[:4]+'00'])
        self.load_data()

    def load_data(self):
        print(self.p_list)
        print(self.c_list)
        print(self.x_list)
        del_pro = 'delete from province'
        del_city = 'delete from city'
        del_county = 'delete from county'
        self.cursor.execute(del_pro)
        self.cursor.execute(del_city)
        self.cursor.execute(del_county)
        ins_pro = 'insert into province values(%s, %s)'
        ins_city = 'insert into city values(%s,%s,%s)'
        ins_county = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins_pro, self.p_list)
        self.cursor.executemany(ins_city, self.c_list)
        self.cursor.executemany(ins_county, self.x_list)
        self.db.commit()
        print('数据存入数据库完毕')

if __name__ == '__main__':
    spider = MingzhengSpider()
    spider.is_new()


