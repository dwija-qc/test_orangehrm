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

    
 #TC_dashboard_001
    def test_a_TC_dashboard_001(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)

        response_data1 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a/span').text
        response_data2 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[2]/div/a/span').text
        response_data3 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[3]/div/a/span').text
        response_data4 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[4]/div/a/span').text
        response_data5 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[5]/div/a/span').text
        response_data6 = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[6]/div/a/span').text
        
        self.assertIn("Assign Leave",response_data1)
        self.assertIn("Leave List",response_data2)
        self.assertIn("Timesheets",response_data3)
        self.assertIn("Apply Leave",response_data4)
        self.assertIn("My Leave",response_data5)
        self.assertIn("My Timesheet",response_data6)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
