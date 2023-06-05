from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller

from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import pickle
import codecs
import os
import time
from selenium.common.exceptions import NoSuchElementException 

def download():
    """
    using selenium, the program open the website, select all states, fill the form(full name, email, and company), download the files.
    """
    #chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    """chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)"""
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://www.avalara.com/taxrates/en/download-tax-tables.html?gclid=EAIaIQobChMI4vSoscTB9QIVFiCtBh2H3QIfEAMYASAAEgKHQfD_BwE&CampaignID=7010b0000013cje&utm_source=paid_search&utm_medium=gppc&ef_id=EAIaIQobChMI4vSoscTB9QIVFiCtBh2H3QIfEAMYASAAEgKHQfD_BwE:G:s&s_kwcid=AL!5131!3!338273650061!e!!g!!free%20sales%20tax&gclsrc=aw.ds&&lso=Paid%20Digital&lsmr=Paid%20Digital")

    states = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.state-content'))
                )
    for state in states:
        driver.execute_script("arguments[0].click();", state)

    continueButton = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#sales-table-download-step-1-bottom-continue > div > button'))
                )
    driver.execute_script("arguments[0].click();", continueButton)
    time.sleep(3)


    name = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#fullname'))
                )
    name.location_once_scrolled_into_view
    #ActionChains(driver).move_to_element(name).perform()
    name.send_keys('Khalil Khalilovic')

    email = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))
                )
    email.location_once_scrolled_into_view
    email.send_keys('khalilo@gmail.com')
    company = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#company'))
                )
    company.location_once_scrolled_into_view
    company.send_keys('makeData')
    body = driver.find_element_by_xpath("//body")
    body.send_keys(Keys.UP)
    
    
    time.sleep(3)
    download = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#NAMEEMAILCOMPANYONLY > div > form > div.sc-hHEiqL.clIRY > button'))
                )
    ActionChains(driver).move_to_element(download).click(download).perform()
    time.sleep(10)
    driver.quit()