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
    reg = '<div class="name"><a href="http://product.dangdang.com/\d+.html" target="_blank" title="(.*?)">'
    for title in re.findall(reg, response):
        print(title)

if __name__ == '__main__':
    # bs_for_parse(response)
    # css_for_parse(response)
    # xpath_for_parse(response)
    re_for_parse(response)
