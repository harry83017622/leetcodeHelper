from utils.crawler import url_problem_, problem_name_
import os
import sys

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)



driver.get(url_problem_)
delay = 1 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'app')))
    print("Page is ready!")
except TimeoutException:
    sys.exit("Loading took too much time!")

print('finish checking loading page')

soup = BeautifulSoup(driver.page_source, features="html.parser")
for EachPart in soup.select('div[class*="question-content"]'):
    content = EachPart.get_text()
driver.quit()

if os.path.exists(problem_name_[:-1]+'.py'):
    print(problem_name_[:-1]+'.py exists')
else:
    print ("{} not exist".format(problem_name_[:-1]))
    with open(problem_name_[:-1]+'.py', "w", encoding="utf-8") as file:
        file.write("''' \n" + content + "\n'''")

