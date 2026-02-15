from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from .common_functions import CommonFunctions
import time

class MainPage(CommonFunctions):

    driver = webdriver.Firefox

    def __init__(self,driver):
        self.driver=driver

    def declineCookiesIfVisible(self):
        try:
            time.sleep(2)
            self.driver.find_element(By.ID,"wt-cli-reject-btn").click()
            return True
        except NoSuchElementException:
            print("Cookie popup is not accesible")
            return True
        except Exception as e:
            print(e)
            self.quit()
            return False

    def checkIfAllMainBlocksLoaded(self):
        try:
            wait = WebDriverWait(self.driver, 4)
            element = wait.until(EC.visibility_of_element_located((By.ID, "navigation")))
            wait = WebDriverWait(self.driver, 4)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main")))
            wait = WebDriverWait(self.driver, 4)
            element = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            return True
        except Exception as e:
            print(e)
            self.quit()
            return False