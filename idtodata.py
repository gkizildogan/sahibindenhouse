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
ad_id = ids[0]