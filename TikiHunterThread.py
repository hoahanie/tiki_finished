from threading import Thread
from TikiTarget import TikiTarget
from TikiItem import TikiItem
from TikiHelper import convertToPrice
import requests
import time
from bs4 import BeautifulSoup
class TikiHunterThread(Thread):
    MAX_PAGE = 1
    def __init__(self, target):
         Thread.__init__(self)
         self.target = target
         self.bestItem =None
         self.name = target.getKeyword()
    
    def __findBestItem(self):
        self.target
        searchLink = self.target.getSearchLink(1)

        response = requests.get(searchLink)
        if (response.status_code)!=200:
            return

        bsoup=BeautifulSoup(response.text,"lxml")

        listElement=bsoup.findAll("a",{"class":"search-a-product-item"})

        i=0
        for e in listElement:
            if (e.get_text().find("Ngừng kinh doanh") >=0 or e.get_text().find("Đã hết hàng")>=0):
                continue

            newItem = TikiItem()
            newItem.title = e.get("title")
            newItem.url = "https://tiki.vn" + e.get("href")
            span = e.find("span", {"class":"final-price"})
            newItem.price= convertToPrice(span.contents[0].strip())
            span = e.find("span", {"class":"price-regular"})
            if span != None:
                newItem.regularPrice = convertToPrice(span.contents[0].strip())

            if newItem.isValidItem(self.target.patterns):
                if self.bestItem ==None:
                    self.bestItem = newItem
                else:
                    if newItem.price< self.bestItem.price:
                        self.bestItem = newItem
            i+=1
        # print("Best Item is" + self.name)
        # if self.bestItem != None:
        #     print(self.bestItem.info())
        # print("------" +"\n")

    def run(self):
        print("Start Thread" + self.name)
        while True:
            try:
                self.__findBestItem()
            except:
                print("something Wrong")
            time.sleep(2)
        print("End Thread " + self.name)
