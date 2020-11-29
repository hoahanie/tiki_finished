from TikiTarget import TikiTarget
from TikiHelper import *
from bs4 import BeautifulSoup
from TikiItem import TikiItem
from TikiHunterThread import TikiHunterThread
from TikiDisplayThread import TikiDisplayThread
from os import system
import requests
import time

out = open("temp.html", "w", encoding="UTF8") 
TARGET_FILE ='target_list.txt'
targets = getTargetFromFile(TARGET_FILE)
threads =[]
displayThread = TikiDisplayThread()
for t in targets:
    hunter = TikiHunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()

for t in threads:
    t.join()

print("End Main")
