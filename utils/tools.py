from utils.settings import url_root_, url_prefix_pattern_

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import sys
import os


class driverHandler(object):
    def __init__(self,name):
        self.driver = None
        self.language = ""
        self.numOfQues = None
        self.problemName = name.replace(" ","-")
        self.webLoading()
        self.selectLang()

    def webLoading(self):
        options = Options()
        options.add_argument("headless")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10) # seconds
        self.driver.get(url_prefix_pattern_+self.problemName+"/")

        delay = 1 # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'app')))
            print("Page is ready!")
        except TimeoutException:
            print("Try different keywords or check your internet connection")
            sys.exit("Loading took too much time!")

        print('finish checking loading page')
        return self.driver

    def selectLang(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div[1]/div/div')
        # elements = driver.find_element_by_css_selector('tabindex="0"')

        elements = elements[0]
        # select python3
        for _ in range(4):
            elements.send_keys(Keys.DOWN)
        elements.send_keys(Keys.RETURN)

    def descriptionParser(self):
        # Find question description
        self.soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        for EachPart in self.soup.select('div[class*="question-content"]'):
            content = EachPart.get_text()
        return content

    def starterCodeParser(self):
        # Find starter code
        for EachPart in self.soup.select('div[class*="CodeMirror-code"]'):
            content_starter_code = EachPart.get_text()
        return content_starter_code
        
    def quitDriver(self):
        self.driver.quit()

def writeResutlsToFile(name,question_description,starter_code):
    if os.path.exists(name+'.py'):
        print('{}.py exists'.format(name))
    else:
        try:
            print ("create {} file".format(name))
            with open(name+'.py', "w", encoding="utf-8") as file:
                file.write("''' \n" + question_description + "\n'''" + starter_code)
        except NameError:
            print('content is None. Try again or use different keywords!')
    return