""" Project websraper_generic
    Created on 15-11-2020, 18:18
    @author Alejo Cain """
# webscraping selenium tutorial using python 3.9 and selenium
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH) # choosing the driver, can also use firefox opera ...

driver.get("https://techwithtim.net")   # opening up the webpage
print(driver.title) # print title of website in terminal

search = driver.find_element_by_name("s")
search.send_keys("test")    # pass string is search box
search.send_keys(Keys.RETURN)   # press enter key

try: # wait code to get to the next page
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()


driver.quit()  # closes tab when driver.close() closes website driver.quit()


# print(driver.page_source) to print source code

# print(main.text) printing everything from the main class