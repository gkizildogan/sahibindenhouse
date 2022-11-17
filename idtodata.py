from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
from time import sleep

ids = pd.read_csv("ids.csv", header=None, names=["ids"])
ids = ids.drop_duplicates()
ids = ids["ids"]
ad_id = str(ids[0])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.sahibinden.com/")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='searchText']"))).send_keys(ad_id)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@value='Ara']"))).click()
page_source = driver.page_source
soup = BeautifulSoup(page_source, features="lxml")
driver.close()
