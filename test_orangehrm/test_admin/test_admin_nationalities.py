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

    #TC_admin_nationalities_002
    def test_a_TC_admin_nationalities_002(self):

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
        browser.find_element(By.ID,"menu_admin_nationality").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME,"nationality[name]").send_keys("Timor Leste")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertIn("Timor Leste", response_data)

    #TC_admin_nationalities_003
    def test_b_TC_admin_nationalities_003(self):

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
        browser.find_element(By.ID,"menu_admin_nationality").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME,"nationality[name]").send_keys("Timor Leste")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error").text

        self.assertIn("Already", response_data)

    #TC_admin_nationalities_004
    def test_c_TC_admin_nationalities_004(self):

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
        browser.find_element(By.ID,"menu_admin_nationality").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.NAME,"nationality[name]").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        response_data = browser.find_element(By.CSS_SELECTOR,"span.validation-error").text

        self.assertIn("Required", response_data)

#TC_admin_nationalities_005
    def test_d_TC_admin_nationalities_005(self):

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
        browser.find_element(By.ID,"menu_admin_nationality").click()
        time.sleep(1)
        nation = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[2]/a').text
        browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[2]/a').click()
        time.sleep(1)
        browser.find_element(By.NAME,"nationality[name]").clear()
        time.sleep(1)
        browser.find_element(By.NAME,"nationality[name]").send_keys(nation+" edit")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"search-results").text

        self.assertIn(nation+" edit",response_data)

#TC_admin_nationalities_007
    def test_d_TC_admin_nationalities_007(self):

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
        browser.find_element(By.ID,"menu_admin_nationality").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[1]').click()
        nation = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[2]').text
        time.sleep(1)
        browser.find_element(By.ID,"btnDelete").click()
        time.sleep(3)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"search-results").text

        self.assertNotIn(nation,response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
