""" Project page_nav_click
    Created on 15-11-2020, 19:30
    @author Alejo Cain """
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try: # wait code to get to the next page
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    #sow - button - 19310003
except:
    driver.quit()