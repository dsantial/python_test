import requests
from bs4 import BeautifulSoup
from lxml import html
import re

url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1'
response = requests.get(url).text

def bs_for_parse(response):
    soup = BeautifulSoup(response, "lxml")
    li_list = soup.find('ul', class_='bang_list clearfix bang_list_mode').find_all('li')
    for li in li_list:
        title = li.find('div', class_='name').find('a')['title']
        print(title)

def css_for_parse(response):
    soup = BeautifulSoup(response, "lxml")
    li_list = soup.select('ul.bang_list.clearfix.bang_list_mode > li')
    for li in li_list:
        title = li.select('div.name > a')[0]['title']
        print(title)

def xpath_for_parse(response):
    selector = html.fromstring(response)
    books = selector.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li")
    for book in books:
        title = book.xpath('div[@class="name"]/a/@title')[0]
        print(title)

def re_for_parse(response):
    # <div class="name"><a href="http://product.dangdang.com/29122655.html" target="_blank" title="少年读徐霞客游记（游中国·地理启蒙，全3册；读万卷书，行万里路！当代著名地质学家、科普作家刘兴诗与古代伟大的旅行家、地理学家徐霞客穿越时空，神奇相遇，趣味解读多姿多彩的中国地理！）">少年读徐霞客游记（游中国·地理启蒙，全3册；读万卷书，行万里路<span class="dot">...</span></a>
    # 匹配上面的字符串,\d+ 匹配多个数字,(.*?)非贪婪匹配任意字符
    reg = '<div class="name"><a href="http://product.dangdang.com/\d+.html" target="_blank" title="(.*?)">'
    for title in re.findall(reg, response):
        print(title)

if __name__ == '__main__':
    # bs_for_parse(response)
    # css_for_parse(response)
    # xpath_for_parse(response)
    re_for_parse(response)
