from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import webbrowser
from playsound import playsound
import time

class AddCourse:


    def __init__(self, path, link):
        self.path = path
        self.link = link

    def run(self):
        driver = webdriver.Chrome(self.path)
        driver.get(self.link)
        time.sleep(2)

        while(True):
            try:
                lst = []
                content = driver.find_elements_by_xpath('//td[@colspan="3"]//td[@align="center"]')
                for i in content:
                    try:
                        a = int(i.text)
                        lst.append(a)
                    except:
                        pass
                
                cap1 = lst[2]
                tot1 = lst[3]
                cap2 = lst[8]
                tot2 = lst[9]

                print("Feedback: {}/{}".format(cap1+cap2, tot1+tot2))

                if cap1 != tot1 or cap2 != tot2:
                    self.warn()
                    break
                
                driver.refresh()

            except Exception as e:
                self.warn()
                print(e)
    
    def warn(self):

        website = "https://quest.pecs.uwaterloo.ca/psc/SS/ACADEMIC/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?orig_reqid=-1bc36125%3A1720afff165%3A-48f5"
        webbrowser.get('chrome').open_new(website)

        while(True):
            playsound("/Users/hans/Desktop/warn.mp3")
        
        

PATH = '/Users/hans/Desktop/chromedriver'
LINK = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1205&subject=CS&cournum=330"

add = AddCourse(PATH, LINK)
add.run()
        

        

    
