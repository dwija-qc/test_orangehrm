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

    
    #TC_time_in_out_002
    def test_a_TC_time_in_out_002(self):

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
        browser.find_element(By.XPATH,'//*[@id="menu_attendance_punchIn"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").send_keys("Late")
        time.sleep(1)
        browser.find_element(By.ID,"btnPunch").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/h1').text
        
        self.assertIn("Punch Out",response_data)

#TC_time_in_out_005
    def test_b_TC_time_in_out_005(self):

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
        browser.find_element(By.XPATH,'//*[@id="menu_attendance_punchIn"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_date").clear()
        browser.find_element(By.ID,"attendance_date").send_keys("2020-07-31")
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").send_keys("Go Home")
        time.sleep(1)
        browser.find_element(By.ID,"btnPunch").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="timeErrorHolder"]').text
        
        self.assertIn("Should Be Higher",response_data)

#TC_time_in_out_004
    def test_c_TC_time_in_out_004(self):

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
        browser.find_element(By.XPATH,'//*[@id="menu_attendance_punchIn"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"attendance_note").send_keys("Go Home")
        time.sleep(1)
        browser.find_element(By.ID,"btnPunch").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/h1').text
        
        self.assertIn("Punch In",response_data)

        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
