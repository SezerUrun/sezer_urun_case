from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

class CommonFunctions:
    
    firefoxDriver = webdriver.Firefox

    def loadPage(self,url):
        try:
            self.driver.get(url)
            time.sleep(2)
            self.driver.maximize_window()
            return True
        except Exception as exc:
            print("EXCEPTION: "+str(exc))
            return False
    
    def getElementByXpath(self,xpath):
        return self.driver.find_element(By.XPATH,xpath)

    def getElementById(self,id):
        return self.driver.find_element(By.ID,id)

    def getElementByCssSelector(self,css_selector):
        return self.driver.find_element(By.CSS_SELECTOR,css_selector)

    def getElementByLinkText(self,link_text):
        return self.driver.find_element(By.LINK_TEXT,link_text)
    
    def getElementsByClass(self,class_name):
        return self.driver.find_elements(By.CLASS_NAME,class_name)

    def clickOnByXpath(self,xpath):
        self.driver.find_element(By.XPATH,xpath).click()
        time.sleep(1)
    
    def clickOnById(self,id):
        self.driver.find_element(By.ID,id).click()
        time.sleep(1)

    def clickOnByCssSelector(self,css_selector):
        self.driver.find_element(By.CSS_SELECTOR,css_selector).click()
        time.sleep(1)

    def clickOnByLinkText(self,link_text):
        self.driver.find_element(By.LINK_TEXT,link_text).click()
        time.sleep(1)
    
    def waitForElementToBeVisibleByLinkText(self,link_text):
        search_results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, link_text))
        )

    def waitForElementToBeVisibleById(self,id):
        search_results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, id))
        )

    def waitForElementToBeVisibleByClass(self,class_name):
        search_results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        
    def scrollToElementByCssSelector(self,css_selector):
        element = self.getElementByCssSelector(css_selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def scrollToElementByXpath(self,xpath):
        element = self.getElementByXpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scrollToElementById(self,id):
        element = self.getElementById(id)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def quit(self):
        try:
            self.driver.quit()
            return True
        except Exception as e:
            print(e)
            return False