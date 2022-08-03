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

    
 #TC_directory_002
    def test_a_TC_directory_002(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("Prajakta Dhumal")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn("Prajakta Dhumal",response_data)

#TC_directory_003
    def test_b_TC_directory_003(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("asdff")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]').text
        
        self.assertIn("No Records Found",response_data)

 #TC_directory_004
    def test_c_TC_directory_004(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"searchDirectory[job_title]"))
        select.select_by_value("3")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn("Odis Adalwin",response_data)

#TC_directory_005
    def test_d_TC_directory_005(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"searchDirectory[location]"))
        select.select_by_value("3")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn("Linda Jane Anderson",response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
