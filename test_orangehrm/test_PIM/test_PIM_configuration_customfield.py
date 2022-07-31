from random import random
from select import select
from tkinter.tix import Select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class admin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #TC_PIM_configuration_customfield_001
    def test_a_TC_PIM_configuration_customfield_001(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="mainMenuFirstLevelUnorderedList"]/li[3]/ul/li[5]/ul/li[1]').click()
        time.sleep(1)
        browser.find_element(By.ID,"btnEdit").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"leaveperiod[cmbStartMonth]"))
        select.select_by_value("2")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"leaveperiod[cmbStartDate]"))
        select.select_by_value("1")
        time.sleep(1)
        browser.find_element(By.ID,"btnEdit").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"lblEndDate").text

        self.assertIn("January",response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
