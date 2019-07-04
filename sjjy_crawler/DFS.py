import requests
from lxml import etree
import pytesseract


# 深度优先搜索 DFS
class DFS(object):
    # 属性
    # 1.有一个可以存和取未采集的url的容器（栈）
    # 2.有一个保存已经采集的url的容器（列表，set集合）
    def __init__(self):
        self.unvisited = [] # 未采集url的容器
        self.visited = [] # 已采集url的容器

    # 方法
    # 3.可以存未采集的url(排除掉重复的url)
    def add_url_to_unvisited(self, url):
        if url not in self.unvisited and url not in self.visited and url.startswith('http'):
            self.unvisited.append(url)

    # 4.可以取未采集的url
    def get_url_from_unvisited(self):
        print(self.unvisited)
        return self.unvisited.pop()

    # 5.可以存已经采集的url
    def add_url_to_visited(self, url):
        self.visited.append(url)

    # 6. 判断调度器是否为空
    def isempty(self):
        return self.unvisited is None


class Crawler(object):
    # 1. 需要一个url的调度器
    # 2. 主页的url
    def __init__(self):
        self.dfs=DFS()

    # 3. 采集的方法
    def crawler(self, url):
        # 将主页的url放入调度器
        self.dfs.add_url_to_unvisited(url)
        # 	5. 重复1-4步，直到调度器为空，停止
        while not self.dfs.isempty():
            # 	1. 从调度器中获取一个url
            cur_url=self.dfs.get_url_from_unvisited()
            # 	2. 发请求，获取响应，抽取新的urls
            text=self.get_page(url=cur_url)
            urls=self.get_urls(text)
            #   3. 将当前url存入调度器
            self.dfs.add_url_to_visited(cur_url)
            # 	4. 将urls存入调度器
            for u in urls:
                self.dfs.add_url_to_unvisited(u)
            #   5. 抽取数据并入库
            datas = self.get_datas_from_page(text)
            print(datas)

    # 发请求，获取响应，抽取新的urls
    def get_urls(self, text):
        html = etree.HTML(text)
        return html.xpath('//a/@href')

    def get_page(self, url):
        return requests.get(url).content

    def get_datas_from_page(self, text):
        html = etree.HTML(text)
        return html.xpath('//title/text()')[0]


def main(url):
    c = Crawler()
    c.crawler(url)


if __name__ == '__main__':
    url='http://www.baidu.com'
    main(url)