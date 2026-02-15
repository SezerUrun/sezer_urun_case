from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from .common_functions import CommonFunctions
import time

class CareersPage(CommonFunctions):
    
    driver = webdriver.Firefox
    actions = ActionChains(driver)

    def __init__(self,driver):
        self.driver=driver
        
    def declineCookiesIfVisible(self):
        try:
            self.driver.find_element(By.ID,"wt-cli-reject-btn").click()
            time.sleep(2)
            return True
        except NoSuchElementException:
            print("Cookie popup is not accesible")
            return True
        except Exception as e:
            print(e)
            return False
        
    def seeAllQAJobs(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, ".big-title")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(1)
            self.clickOnByXpath("/html/body/div/section[1]/div/div/div/div[1]/div/section/div/div/div[1]/div/div/a")
            return True
        except Exception as e:
            print(e)
            self.quit()
            return False
        
    def applyJobFilter(self,location,department):
        try:
            self.scrollToElementByXpath("/html/body/section[1]/div/div/div/div/p")
            self.clickOnById("filter-by-location")
            self.waitForElementToBeVisibleByClass("job-location")
            time.sleep(10)
            dropdown = Select(self.driver.find_element(By.ID,"filter-by-location"))
            dropdown.select_by_visible_text(location)
            self.clickOnById("filter-by-department")
            dropdown = Select(self.driver.find_element(By.ID,"filter-by-department"))
            time.sleep(1)
            dropdown.select_by_visible_text(department)
            time.sleep(10)
            return True
        except Exception as e:
            print(e)
            self.quit()
            return False
        
    def checkIfJobsAreFilteredAsExpected(self,title_expected,location_expected,department_expected):
        try:
            position_list_items=self.getElementsByClass("position-list-item")
            position_titles=self.getElementsByClass("position-title")
            position_departments=self.getElementsByClass("position-department")
            position_locations=self.getElementsByClass("position-location")
            if(len(position_titles)>0 and len(position_departments)>0 and len(position_locations)>0):
                if(len(position_titles)==len(position_departments)==len(position_locations)):
                    self.scrollToElementById("career-position-list")
                    self.waitForElementToBeVisibleById("jobs-list")
                    for i in range(len(position_list_items)):
                        title_found=position_titles[i].text
                        if(str(title_found).find(title_expected)<0):
                            print("Title at "+str(i+1)+" does not include "+title_expected+", it is "+title_found)
                            self.quit()
                            return False
                        department_found=position_departments[i].text
                        if(department_found!=department_expected):
                            print("Department at "+str(i+1)+" is not "+department_expected+", it is "+department_found)
                            self.quit()
                            return False
                        location_found=position_locations[i].text
                        if(location_found!=location_expected):
                            print("Location at "+str(i+1)+" is not "+location_expected+", it is "+location_found)
                            self.quit()
                            return False
                    return True
        except Exception as e:
            print(e)
            self.quit()
            return False

    def checkIfViewRoleButtonsWorkAsExpected(self):
        try:
            position_list_items=self.driver.find_elements(By.CLASS_NAME,"position-list-item")
            if(len(position_list_items)>0):
                for i in range(len(position_list_items)):
                    original_window=self.driver.current_window_handle
                    self.clickOnByXpath("/html/body/section[2]/div/div[2]/div/div["+str(i+1)+"]/div/a")
                    time.sleep(2)
                    print(str(self.driver.current_url))
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    print(str(self.driver.current_url))
                    time.sleep(2)
                    if(str(self.driver.current_url).find("jobs.lever.co/insiderone")<0):
                        print("View role button for item "+str(i+1)+" is not working as expected")
                        self.quit()
                        return False
                    self.driver.switch_to.window(original_window)
            else:
                print("Position list is empty")
            return True
        except Exception as e:
            print(e.with_traceback)
            self.quit()
            return False