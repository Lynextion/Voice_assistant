import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def youtube(data):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    search = data.split()
    searched = []
    removed_senteces = ["youtube","aç"]
    for split in search:
        if split not in removed_senteces or split not in removed_senteces:
            searched.append(split)
    result = " ".join(searched)
    driver.get("https://www.youtube.com/results?search_query=" +result)
    search = driver.find_element_by_id("video-title")
    search.click()