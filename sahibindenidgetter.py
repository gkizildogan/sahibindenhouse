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

pages_to_visit = [str(item) for item in np.linspace(0, 950, 20, dtype=int)]
str1 = "https://www.sahibinden.com/satilik/eskisehir-tepebasi?pagingOffset="
str3 = "&pagingSize=50"

for i in pages_to_visit:
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        str2 = i
        link = str1 + str2 + str3
        driver.get(link)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchResultsTable")))
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, features="lxml")
        table = soup.find("table", id="searchResultsTable")
        ids = [item["data-id"] for item in table.find_all(attrs={"data-id": True})]
        ids_ser = pd.Series(ids)
        ids_ser.to_csv("ids.csv", mode="a", index=False, header=False)
    finally:
        driver.close()

    sleep(10)

