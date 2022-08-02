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

    
 #TC_time_in_out_004
    def test_b_TC_time_in_out_004(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_time_viewTimeModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_attendance_Attendance").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_attendance_viewMyAttendanceRecord"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(1)

        response_data = browser.find_element(By.XPATH,'//*[@id="employeeRecordsForm"]/table/tbody/tr[1]/td[2]/span').text
        
        self.assertIn("GMT",response_data)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
