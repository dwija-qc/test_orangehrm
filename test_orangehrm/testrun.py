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

    #TC_admin_job_titles_008
    def test_f_TC_admin_job_titles_008(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_Job").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_admin_viewJobTitleList"]').click()
        time.sleep(1)
        titledel = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[2]/a').text
        browser.find_element(By.XPATH,'//*[@id="ohrmList_chkSelectRecord_26"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"btnDelete").click()
        time.sleep(1)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertNotIn(titledel,response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
